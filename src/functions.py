import numpy as np
import scipy.fftpack as fft
import scipy.io.wavfile as wav

# Given a wave, get the fourier transform
def getFft(array: list):
    return fft.fft(array)

# Given a fourier transform, get the magnitude
def getMagnitude(array: list):
    return np.abs(array)

# Given a fourier transform, get the phase
def getPhase(array: list):
    return np.angle(array)

# Given a fourier transform and fs, get the time vector
def getTimeVector(array: list, fs: int):
    return np.arange(0, len(array)/fs, 1/fs)

# Given a path, get the wave data
def getWaveData(path: str):
    fs, data = wav.read(path)
    return fs, data

# Given a fs and a wave, get the discrete frequency
def getDiscreteFrequency(fs, wave):
    length = len(wave)
    F = fs*np.arange(0, length//2)/length
    return F

# This functions has been made by ChatGPT (100% IA)
def generateSyntheticSound(frequency, duration, fs=44100):
    time_points = np.linspace(0, duration, int(duration * fs), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * time_points)
    waveform /= np.max(np.abs(waveform))
    return waveform

# Given a magnitude array and F, get the max magnitude
def getMaxMagnitude(array: list, F):
    pos = np.where(array == np.max(array))
    return F[pos]


