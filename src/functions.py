import numpy as np
import scipy.fftpack as fft
import scipy.io.wavfile as wav

# Given a wave, get the fourier transform (doesnt need to be fixed)


def getFft(sound: list):
    return fft.fft(sound)

# Given a fourier transform, get the magnitude (fixed)


def getMagnitude(transform: list):
    return (np.abs(transform))[0:len(transform)//2]

# Given a fourier transform, get the phase (doesnt need to be fixed)


def getPhase(transform: list):
    return np.angle(transform)

# Given a sound and fs, get the time vector (fixed)


def getTimeVector(sound: list, fs: int):
    return np.arange(0, len(sound))/fs

# Given a path, get the wave data (fixed)


def getWaveData(path: str):
    fs, data = wav.read(path)
    if len(data.shape) > 1:
        return fs, data[:, 0]
    return fs, data

# Given a fs and a wave, get the discrete frequency (fixed)


def getDiscreteFrequency(fs, transform):
    return fs * np.arange(0, len(transform)//2)/len(transform)
# This functions has been made by ChatGPT (100% IA)


def generateSyntheticSound(frequency, duration, fs=44100):
    time_points = np.linspace(0, duration, int(duration * fs), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * time_points)
    waveform /= np.max(np.abs(waveform))
    return waveform

# Given a magnitude array and F, get the max magnitude


def getMaxMagnitude(magnitude, df):
    posm = np.where(magnitude == np.max(magnitude))
    return df[posm]


def get_genr(frequency):
    men_range = (85, 155)
    women_range = (165, 255)

    error_thredshold = 15/100

    men_range_a = men_range * (1 - error_thredshold)
    men_range_b = men_range * (1 + error_thredshold)
    women_range_a = women_range * (1 - error_thredshold)
    women_range_b = women_range * (1 + error_thredshold)

    men = range(men_range_a, men_range_b)
    women = range(women_range_a, women_range_b)

    if frequency in men:
        return 0
    elif frequency in women:
        return 1
    else:
        return -1
