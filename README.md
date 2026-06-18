# Audio Transcription Utility
The project originated from a real-world requirement brought to me by an acquaintance. He regularly conducted interviews for a own project and needed an efficient way to transcribe them. After exploring existing solutions, we found that most available options relied on paid models or subscription-based services. This motivated me to develop a more accessible and cost-effective alternative.
Small utility to transcribe audio files using OpenAI's Whisper model.

Files
- [transcribe.py](transcribe.py) - CLI script containing [`transcribe_file`](transcribe.py) and [`main`](transcribe.py).
- [transcrpt1.txt](transcrpt1.txt) - Example/output text file included in the workspace.

Requirements
- Python 3.8+
- ffmpeg installed system-wide
- Python packages:
  ```sh
  pip install -U openai-whisper torch
  ```

## Usage

1. Prepare environment
   - Create and activate a virtualenv (Linux):
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install Python deps inside the venv:
     ```sh
     pip install -U openai-whisper torch
     ```
   - Install ffmpeg system-wide (Debian/Ubuntu example):
     ```sh
     sudo apt update && sudo apt install ffmpeg
     ```

2. Basic transcription
   ```sh
   python transcribe.py path/to/audio.m4a
   ```
   - By default output is written to the same folder with a `.txt` extension and the output path is printed.

3. Options
   - Select model: `-m` / `--model` (tiny, base, small, medium, large). Example:
     ```sh
     python transcribe.py input.mp3 -m medium
     ```
   - Specify language to improve accuracy: `-l` / `--language` (e.g. `en`, `es`):
     ```sh
     python transcribe.py input.mp3 -l es
     ```
   - Specify output file: `-o` / `--output`:
     ```sh
     python transcribe.py input.mp3 -o transcript.txt
     ```

4. Example
   ```sh
   python transcribe.py interview.m4a -m small -l en -o interview.txt
   cat interview.txt
   ```
