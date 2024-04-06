from functions import getPhase, getFft, getWaveData, getMagnitude, getGenr
from functions import getDiscreteFrequency, getMaxMagnitude, getTimeVector
from functions import getRms

# 1. Get the sound
path = "sounds/cristian.wav"
fs, sound = getWaveData(path)

# 2. Get the fft
transform = getFft(sound)

# 3. Get the magnitude
magnitude = getMagnitude(transform)
rms = getRms(magnitude)
print(f"El rms es: {rms}")

# 4. Get the phase
phase = getPhase(transform)

# 5. Get the time vector
time = getTimeVector(sound, fs)

# 6. Get the discrete frequency
df = getDiscreteFrequency(fs, transform)

# 7. Get the predominant frequency
frequency = getMaxMagnitude(magnitude, df)

# 8. Get the gender
gender_dic = {1: "woman", 0: "man", -1: "unknown"}
gender = getGenr(frequency)
gender = gender_dic[gender]

# 9. Print the gender and frequency
print(f"Voice / Sound used: {path}")
print(f"Voice gender detected: {gender} ({frequency}hz)")
