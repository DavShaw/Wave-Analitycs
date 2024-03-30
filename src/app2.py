import matplotlib.pyplot as plt
from functions import getPhase, getFft, getMagnitude, getGenr, captureAudio
from functions import getDiscreteFrequency, getMaxMagnitude, getTimeVector

# 1. Get real-time audio data from microphone
fs = 44100
duration = 10
sound = captureAudio(fs, duration)

# 2. Get the FFT
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

# 8. Get the gender
gender_dic = {1: "woman", 0: "man", -1: "unknown"}
gender = getGenr(frequency)
gender = gender_dic[gender]

# 9. Print the gender and frequency
print(f"Voice gender detected: {gender} ({frequency} Hz)")

# If you want to visualize audio data, you can do it here
# For example, you can plot the waveform or frequency spectrum

plt.plot(time, transform)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio waveform')
plt.show()
