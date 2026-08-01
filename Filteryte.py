import numpy as np
import sox
import librosa
from sound_to_midi.monophonic import wave_to_midi

tfm = sox.Transformer()
# apply high-pass filter which called also (low-cut)
tfm.highpass(frequency=150)
# apply compression
tfm.compand()
#create output
tfm.build('in.mp3', 'in2.wav')
#convert to midi
data, samplerate = librosa.load('in2.wav', sr=None)
midi = wave_to_midi(data, srate=samplerate)
with open ('out.midi', 'wb') as f:
    midi.writeFile(f)
#done
print('Done')
