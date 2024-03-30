import pyaudio
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

# This functions has been made by ChatGPT


def generateSyntheticSound(frequency, duration, fs=44100):
    time_points = np.linspace(0, duration, int(duration * fs), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * time_points)
    waveform /= np.max(np.abs(waveform))
    return waveform

# Given a magnitude array and F, get the max magnitude


def getMaxMagnitude(magnitude, df):
    posm = np.where(magnitude == np.max(magnitude))
    return df[posm]


def getGenr(frequency, activate_error=False, error=(15/100)):
    men_range = (85, 155)
    women_range = (165, 255)

    if activate_error:
        error_threshold = error

        men_range_a = men_range[0] * (1 - error_threshold)
        men_range_b = men_range[1] * (1 + error_threshold)
        women_range_a = women_range[0] * (1 - error_threshold)
        women_range_b = women_range[1] * (1 + error_threshold)
        men = range(int(men_range_a), int(men_range_b) + 1)
        women = range(int(women_range_a), int(women_range_b) + 1)
    else:
        men = range(men_range[0], men_range[1])
        women = range(women_range[0], women_range[1])

    if withinInterval(frequency, men):
        return 0
    elif withinInterval(frequency, women):
        return 1
    else:
        return -1


def withinInterval(number, interval):
    return (number >= interval[0]) and (number <= interval[-1])

# Function made by ChatGTP


def captureAudio(fs, duration):
    CHUNK = 1024
    audio_data = []

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1,
                    rate=fs, input=True, frames_per_buffer=CHUNK)

    for i in range(0, int(fs / CHUNK * duration)):
        data = stream.read(CHUNK)
        audio_data.append(np.frombuffer(data, dtype=np.int16))
    stream.stop_stream()
    stream.close()
    p.terminate()

    return np.concatenate(audio_data)
