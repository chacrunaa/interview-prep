#!/usr/bin/env bash
# Расшифровка видео курса: mp4 -> wav 16k mono -> mlx-whisper (ru) -> .srt/.txt/.json
# usage: transcribe.sh <mp4> <out_dir> <name>
set -euo pipefail
mp4="$1"; out="$2"; name="$3"
WH="${WHISPER_BIN:-$HOME/.venvs/whisper/bin/mlx_whisper}"
mkdir -p "$out"
wav="$out/$name.wav"
[ -f "$wav" ] || ffmpeg -nostdin -loglevel error -i "$mp4" -vn -ac 1 -ar 16000 "$wav"
"$WH" "$wav" --model mlx-community/whisper-large-v3-turbo \
  --language ru --output-dir "$out" --output-name "$name" --output-format all \
  --condition-on-previous-text False --verbose False
rm -f "$wav"
