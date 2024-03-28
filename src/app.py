import matplotlib.pyplot as plt
from functions import * 

fs, mySound = getWaveData("src/sound.wav")

length = len(mySound)

fourier = getFft(mySound)
magnitude = getMagnitude(fourier)
magnitude = magnitude[:length//2]
phase = getPhase(fourier)
F = getDiscreteFrequency(fs, mySound)
themax = getMaxMagnitude(magnitude, F)

plt.plot(F, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Magnitude Spectrum")
plt.show()
print(themax)

