from functions import getWaveData, getFft, getMagnitude, getPhase, getDiscreteFrequency, getMaxMagnitude, getGenr, captureAudio
# Get realtime sound
path = "src/real.wav"
captureAudio(duration=10, filename=path)
fs, sound = getWaveData(path)

# Get transform
transform = getFft(sound)

# Get magnitude
magnitude = getMagnitude(transform)

# Get phase
phase = getPhase(transform)

# Get df (discrete frequency)
df = getDiscreteFrequency(fs, transform)

# Get frequency
frequency = getMaxMagnitude(magnitude, df)

# Detect gender
genders = {0: "man", 1: "woman", -1: "unknown"}
detected = getGenr(frequency=frequency, activate_error=True, error=(20/100))
print(f"Frequency detected: {frequency} hz")
print(f"Voice gender detected: {genders[detected]}")
