import whisper

# Загружаем модель (варианты: tiny, base, small, medium, large)
model = whisper.load_model("small")

# Распознаём речь из аудиофайла
result = model.transcribe("audios/audio.m4a")

print(result["text"])
