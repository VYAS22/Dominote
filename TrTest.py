import omnizart
import librosa
## import midi

# Load the audio file
audio_file = "audio.wav"
audio, sample_rate = librosa.load(audio_file)

# Extract the features
features = omnizart.extract_features(audio, sample_rate)

# Perform music transcription
transcription = omnizart.transcribe(features)

# Save the transcription
## midi_file = "transcription.mid"
## midi.write_midi_file(midi_file, transcription)
