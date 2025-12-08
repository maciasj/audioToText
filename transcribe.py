#!/usr/bin/env python3
import argparse
import os
import sys

try:
    import whisper
    import torch
except Exception as e:
    sys.exit(
        "Missing dependency: install with `pip install -U openai-whisper torch` and ensure ffmpeg is installed. Error: "
        + str(e)
    )


def transcribe_file(path: str, model_name: str = "small", language: str | None = None) -> str:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model(model_name, device=device)
    kwargs = {}
    if language:
        kwargs["language"] = language
    result = model.transcribe(path, **kwargs)
    return result.get("text", "").strip()


def main():
    p = argparse.ArgumentParser(description="Transcribe an audio file (.m4a, .mp3, .wav, ...)")
    p.add_argument("input", help="Input audio file path (.m4a)")
    p.add_argument(
        "--model",
        "-m",
        default="small",
        help="Whisper model to use (tiny, base, small, medium, large). Larger = slower but more accurate.",
    )
    p.add_argument(
        "--language",
        "-l",
        default=None,
        help="If known, provide the language code (e.g. en, es). Otherwise Whisper will auto-detect.",
    )
    p.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output text file. Defaults to input filename with .txt extension in same folder.",
    )
    args = p.parse_args()

    if not os.path.isfile(args.input):
        sys.exit("Input file not found: " + args.input)

    out_path = args.output or os.path.splitext(args.input)[0] + ".txt"
    text = transcribe_file(args.input, model_name=args.model, language=args.language)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(out_path)


if __name__ == "__main__":
    main()