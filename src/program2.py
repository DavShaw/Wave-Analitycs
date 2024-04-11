from functions import getWaveData, getFft, getMagnitude, getPhase, getDiscreteFrequency, getMaxMagnitude, getGenr, captureAudio
from functions import getRms, getFormant
from modelo import predict_With_list

# Get realtime sound
path = "src/real.wav"
captureAudio(duration=10, filename=path)
fs, sound = getWaveData(path)

# Get transform
transform = getFft(sound)

# Get magnitude
magnitude = getMagnitude(transform)

# Get rms
rms = getRms(magnitude)

# Get phase
phase = getPhase(transform)

# Get df (discrete frequency)
df = getDiscreteFrequency(fs, transform)

# Get frequency
frequency = getMaxMagnitude(magnitude, df)

# Get formant
format = getFormant(transform, magnitude, df)

# Get who is talking
name = predict_With_list(frequency, rms, format)

print(f"{name} is talking!!!")
