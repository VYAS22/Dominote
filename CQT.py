
import librosa
import numpy as np

#Load audio file
y, sr = librosa.load("audio.wav")

#Compute CQT
C = librosa.cqt(y, sr=sr)

#Visualize the CQT
import matplotlib.pyplot as plt
import librosa.display

librosa.display.specshow(librosa.amplitude_to_db(np.abs(C), ref=np.max),
sr=sr, x_axis='time', y_axis='cqt_note')
plt.colorbar(format='%+2.0f dB')
plt.title('Constant-Q power spectrum')
plt.tight_layout()
plt.show()
