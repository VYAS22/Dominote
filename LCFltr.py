import librosa
import numpy as np
from scipy import signal

def high_pass_filter(audio_file, cutoff_freq, sample_rate, order=4):
  """
  Applies a high-pass filter to an audio file.

  Args:
    audio_file: Path to the audio file (wav or mp3).
    cutoff_freq: Cutoff frequency of the filter in Hz.
    sample_rate: Sampling rate of the audio file.
    order: Order of the Butterworth filter.

  Returns:
    Filtered audio signal.
  """

  # Load the audio file
  y, sr = librosa.load(audio_file, sr=sample_rate)

  # Design the high-pass filter
  nyquist_freq = 0.5 * sr
  normalized_cutoff = cutoff_freq / nyquist_freq
  b, a = signal.butter(order, normalized_cutoff, btype='highpass')

  # Apply the filter
  filtered_audio = signal.filtfilt(b, a, y)

  return filtered_audio

# Example usage
audio_file = 'path/to/your/audio.wav'  # Replace with the actual path
cutoff_freq = 1000  # Cutoff frequency in Hz
sample_rate = 44100  # Sampling rate

filtered_audio = high_pass_filter(audio_file, cutoff_freq, sample_rate)

# Save the filtered audio (optional)
librosa.output.write_wav('filtered_audio.wav', filtered_audio, sr)