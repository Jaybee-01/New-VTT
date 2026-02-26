from flask import Flask, request, jsonify, render_template_string
from faster_whisper import WhisperModel
import tempfile
import os

app = Flask(__name__)

# Load model once at startup — using "base" for speed/accuracy balance
# Options: tiny, base, small, medium, large-v2
print("Loading Whisper model... please wait.")
model = WhisperModel("base", device="cpu", compute_type="int8")
print("Model loaded!")

# HTML = open("templates/index.html").read()
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML = open(os.path.join(BASE_DIR, "templates", "index.html"), encoding="utf-8").read()
# HTML = open(os.path.join(BASE_DIR, "templates", "index.html")).read()


@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    suffix = ".wav" if audio_file.filename.endswith(".wav") else ".mp3"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        audio_file.save(tmp.name)
        tmp_path = tmp.name

    try:
        segments, info = model.transcribe(tmp_path, beam_size=5)
        transcript = " ".join([seg.text.strip() for seg in segments])
        language = info.language
        return jsonify({"transcript": transcript, "language": language})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.unlink(tmp_path)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
