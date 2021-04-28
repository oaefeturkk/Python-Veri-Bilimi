from playsound import playsound
import simpleaudio as sa
import numpy as np
import IPython.display as ipd 
import librosa
import librosa.display
import matplotlib.pyplot as plt

#Playsound Modulu İle Ses Dosyasını Çalıştırmak için; 
playsound('kalem.wav')

# Simpleaudio modulu ile Ses Dosyasını Çalıştırmak için;
filename = 'kalem.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()

# 3 sn lik tek ses için;
freq = 440 
fs = 44100
sec = 3

t = np.linspace(0, sec, sec * fs, False)

note = np.sin(freq * t * 2 * np.pi)

audio = note * (2**15 - 1) / np.max(np.abs(note))

audio = audio.astype(np.int16)

play_obj = sa.play_buffer(audio, 1, 2, fs)

play_obj.wait_done()

# WAV Dosyasını Görüntülemek için;
filename = 'kalem.wav'

plt.figure(figsize=(15,4))
data1,sample_rate1 = librosa.load(filename, sr=22050, mono=True, offset=0.0, duration=50, res_type='kaiser_best')
librosa.display.waveplot(data1,sr=sample_rate1, max_points=50000.0, x_axis='time', offset=0.0, max_sr=1000)

print(data1)
print(len(data1))
print(sample_rate1)

