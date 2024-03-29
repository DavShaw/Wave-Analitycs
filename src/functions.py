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

# Given a path, get the wave data (fixed)


def getWaveData(path: str):
    fs, data = wav.read(path)
    if len(data.shape) > 1:
        return fs, data[:, 0]
    return fs, data

# Given a fs and a wave, get the discrete frequency


def getDiscreteFrequency(fs, wave):
    length = len(wave)
    F = fs * np.arange(length) / length  # Full frequency range
    return F
# This functions has been made by ChatGPT (100% IA)


def generateSyntheticSound(frequency, duration, fs=44100):
    time_points = np.linspace(0, duration, int(duration * fs), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * time_points)
    waveform /= np.max(np.abs(waveform))
    return waveform

# Given a magnitude array and F, get the max magnitude


def getMaxMagnitude(array, F):
    coords = np.where(array == np.max(F))
    print(f"Algo: {coords[0]}")
    return F[coords[0]]


def determinar_sexo(frecuencia):
    # Rango de frecuencia típico para hombres y mujeres
    hombres_rango = (85, 155)
    mujeres_rango = (165, 255)

    # Umbral para la probabilidad
    umbral_probabilidad = 0.7

    # Probabilidad de que la frecuencia pertenezca a un hombre
    probabilidad_hombre = 1 / \
        (1 + np.exp(-(frecuencia -
         hombres_rango[0]) / (hombres_rango[1] - hombres_rango[0])))

    # Si la probabilidad es mayor que el umbral, predecir hombre, si no, mujer
    if probabilidad_hombre > umbral_probabilidad:
        return "Hombre"
    elif probabilidad_hombre > (1 - umbral_probabilidad):
        return "Indeterminado"
    else:
        return "Mujer"
