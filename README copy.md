# 🎙️ Whisper Speech-to-Text Toolkit

Набор скриптов на Python для работы с **OpenAI Whisper** — мощной моделью распознавания речи.  
Позволяет:
- Распознавать речь из аудиофайлов  
- Записывать голос с микрофона  
- Создавать субтитры `.srt`  
- Индексировать тексты для быстрого поиска  

---

## 📁 Структура проекта

```
├── audios/                     # Папка с аудиофайлами (.wav, .mp3, .m4a, ...)
├── transcripts.json            # Автоматически сохраняемые расшифровки
├── subtitles.srt               # Созданные субтитры
├── test_whisper.py             # Минимальный тест Whisper
├── transcribe_and_index.py     # Распознавание и сохранение в JSON
├── record_and_transcribe.py    # Запись с микрофона и расшифровка
├── subtitles.py                # Создание субтитров из аудио
├── README.md                   # Этот файл
└── SETUP_GUIDE.md              # Подробная инструкция по установке
```

---

## 🚀 Быстрый старт

1. **Создай виртуальное окружение**
   ```bash
   python3 -m venv whisper-env
   source whisper-env/bin/activate
   ```

2. **Установи зависимости**
   ```bash
   pip install -U openai-whisper sounddevice scipy
   ```

3. **Проверь работу модели**
   ```bash
   python test_whisper.py
   ```

---

## 🧩 Скрипты

### ▶️ `test_whisper.py`
Простое распознавание одного файла:
```python
import whisper
model = whisper.load_model("small")
result = model.transcribe("audios/audio.m4a")
print(result["text"])
```

---

### 🗂️ `transcribe_and_index.py`
Автоматически проходит по всем файлам в `audios/`, распознаёт и сохраняет тексты в `transcripts.json`.

---

### 🎤 `record_and_transcribe.py`
Записывает голос с микрофона (5 секунд), сохраняет в `audios/record.wav` и выводит расшифровку с таймкодами.

---

### 📝 `subtitles.py`
Создаёт файл субтитров `subtitles.srt` из аудио с точными таймкодами.  
Подходит для использования в видеоредакторах или YouTube.

---

## ⚙️ Требования

- Python 3.9 или новее  
- Микрофон (для записи)  
- Модель Whisper (`tiny`, `base`, `small`, `medium`, `large`)

---

## 📚 Полная инструкция

Смотри файл [`SETUP_GUIDE.md`](./SETUP_GUIDE.md)

---

## 🧠 Автор

Разработано для демонстрации возможностей **OpenAI Whisper**.  
Если проект помог — ⭐ звезда приветствуется!
