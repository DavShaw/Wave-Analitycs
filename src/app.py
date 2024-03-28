import matplotlib.pyplot as plt
from functions import getPhase, getFft, getWaveData  # , generateSyntheticSound
from functions import getDiscreteFrequency, getMaxMagnitude, getMagnitude

fs, mySound = getWaveData("src/sound125hz.wav")
# fs, mySound = 44100, generateSyntheticSound(4856, 8)

length = len(mySound)

fourier = getFft(mySound)
magnitude = getMagnitude(fourier)
magnitude = magnitude[:length]
phase = getPhase(fourier)
F = getDiscreteFrequency(fs, mySound)
themax = getMaxMagnitude(magnitude, F)

plt.plot(F, magnitude)
plt.xlabel("Freq (Hz)")
plt.ylabel("Mag")
plt.show()

print(themax)
