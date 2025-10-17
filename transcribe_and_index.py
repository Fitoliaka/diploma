import os
import json
import whisper

model = whisper.load_model("base")
transcripts = {}

for filename in os.listdir("audios"):
    if filename.lower().endswith((".wav", ".mp3", ".m4a", ".flac", ".ogg")):
        result = model.transcribe(os.path.join("audios", filename))
        transcripts[filename] = result["text"].lower()

# сохраняем для дальнейшего поиска
with open("transcripts.json", "w", encoding="utf-8") as f:
    json.dump(transcripts, f, ensure_ascii=False, indent=2)
