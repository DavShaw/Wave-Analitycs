import matplotlib.pyplot as plt
from functions import getPhase, getFft, getWaveData, getMagnitude
from functions import getDiscreteFrequency, getMaxMagnitude, getTimeVector

# 1. Get the sound
fs, sound = getWaveData("src/man.wav")

# 2. Get the fft
transform = getFft(sound)

# 3. Get the magnitude
magnitude = getMagnitude(transform)

# 4. Get the phase
phase = getPhase(transform)

# 5. Get the time vector
time = getTimeVector(sound, fs)

# 6. Get the discrete frequency
df = getDiscreteFrequency(fs, transform)

# 7. Get the predominant frequency
frequency = getMaxMagnitude(magnitude, df)
