import matplotlib.pyplot as plt
from functions import * 

mySound = generateSyntheticSound(156, 3)

length = len(mySound)

fourier = getFft(mySound)
magnitude = getMagnitude(fourier)
magnitude = magnitude[:length//2]
phase = getPhase(fourier)
F = getDiscreteFrequency(44100, mySound)

plt.plot(F, magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()


