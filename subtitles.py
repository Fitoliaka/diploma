import whisper

def write_srt(segments, filename="subtitles.srt"):
    with open(filename, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, start=1):
            start = seg["start"]
            end = seg["end"]
            text = seg["text"].strip()
            f.write(f"{i}\n")
            f.write(f"{format_srt_time(start)} --> {format_srt_time(end)}\n")
            f.write(f"{text}\n\n")

def format_srt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds * 1000) % 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

model = whisper.load_model("small")
result = model.transcribe("audios/Новая запись 3.m4a")
write_srt(result["segments"])

print("✅ Субтитры сохранены в subtitles.srt")
