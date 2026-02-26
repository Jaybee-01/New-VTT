# 🎙️ Whisper Voice-to-Text App
A web app for transcribing audio files and live microphone recordings using faster-whisper + Flask.

---

## ✅ Requirements
- Python 3.8 or newer
- A microphone (for live recording)

---

## 🚀 Setup — Step by Step

### Step 1 — Open a terminal / command prompt
Navigate to this folder:
```
cd whisper-app
```

### Step 2 — (Recommended) Create a virtual environment
```
python -m venv venv
```
Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Step 3 — Install dependencies
```
pip install -r requirements.txt
```
This installs only 2 packages: `faster-whisper` and `flask`.

> ⚠️ If you get an error about `ctranslate2`, run:
> `pip install ctranslate2 --upgrade`

### Step 4 — Run the app
```
python app.py
```
The first time it runs, it will download the Whisper "base" model (~145MB). This only happens once.

### Step 5 — Open your browser
Go to: **http://localhost:5000**

---

## 🎯 How to Use

**Upload a file:**
1. Drag & drop an audio file (MP3, WAV, M4A, OGG, FLAC) onto the upload box
2. Click "Transcribe Audio"
3. Wait a few seconds for the result

**Live recording:**
1. Click the red circle button to start recording
2. Allow microphone access when the browser asks
3. Click again to stop
4. Click "Transcribe Audio"

---

## ⚙️ Changing the Model Size
In `app.py`, change `"base"` to one of:

| Model | Size | Speed | Accuracy |
|-------|------|-------|----------|
| `tiny` | ~75MB | Very fast | Lower |
| `base` | ~145MB | Fast | Good ✅ |
| `small` | ~465MB | Medium | Better |
| `medium` | ~1.5GB | Slow | Great |
| `large-v2` | ~3GB | Very slow | Best |

For a final year project demo, `small` is recommended for the best balance.

---

## 📁 Project Structure
```
whisper-app/
├── app.py              ← Flask backend
├── requirements.txt    ← Dependencies
├── README.md           ← This file
└── templates/
    └── index.html      ← Frontend UI
```
