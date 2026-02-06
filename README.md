# Voice Recognition Droid

Simple voice-echo assistant: listens, converts speech to text, then speaks it back.

Files
- controller.py — orchestration: calls listener and speaker.
- listener.py — captures microphone audio and uses Google Speech API.
- droid_gui.py — Tkinter GUI with "Start Listening" button.
- speaker.cpp — Windows SAPI program that reads stdin and speaks.

Requirements
- Python 3.8+ virtual environment
- Install Python deps (in your venv):

```bash
python -m pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install:

```bash
python -m pip install SpeechRecognition pyaudio
```

Build speaker (once):

```bash
# on Windows with MinGW/MSYS (example)
g++ -g speaker.cpp -o speaker.exe -lole32 -luuid -lsapi
```

Run

1. Compile `speaker.cpp` (above) to produce `speaker.exe`.
2. Create and activate a Python venv and install dependencies.
3. Start the GUI:

```bash
python droid_gui.py
```

Click "Start Listening" — speech is recognized and piped to `speaker.exe` which speaks via your system audio.

Notes about tracked binaries
- The repository should not track large binary files (like `speaker.exe` or a virtualenv). Binaries increase repo size, make pushes slow or fail, and can't be diffed.
- Preferred options:
  - Keep `speaker.exe` out of the repo and build it locally from `speaker.cpp`.
  - Or publish `speaker.exe` on GitHub Releases and download it as an artifact.

License
Add a license if you want to share this project publicly.
