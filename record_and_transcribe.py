import sounddevice as sd
from scipy.io.wavfile import write
import whisper

fs = 16000
seconds = 5
print("🎤 Говори...")

audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write("audios/record.wav", fs, audio)

model = whisper.load_model("small")
result = model.transcribe("audios/record.wav")

print("\n📝 Распознанный текст:")
for segment in result["segments"]:
    print(f"[{segment['start']:.2f}s -> {segment['end']:.2f}s]: {segment['text']}")
