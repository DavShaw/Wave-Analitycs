from IPython.display import Image
import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Steps:
# 1. get the fft
# 2. get the magnitude
# 3. get the phase

def getFft(array: list):
    return fft.fft(array)

def getMagnitude(array: list):
    return np.abs(array)

def getPhase(array: list):
    return np.angle(array)

def getTimeVector(array: list, fs: int):
    return np.arange(0, len(array)/fs, 1/fs)

def getWaveData(path: str):
    fs, data = wav.read(path)
    return fs, data

def getDiscreteFrequency(fs, wave):
    length = len(wave)
    F = fs*np.arange(0, length//2)/length
    return F
