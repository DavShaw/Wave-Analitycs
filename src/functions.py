import numpy as np
import scipy.fftpack as fft
import scipy.io.wavfile as wav

# Given a wave, get the fourier transform (doesnt need to be fixed)


def getFft(array: list):
    return fft.fft(array)

# Given a fourier transform, get the magnitude (fixed)


def getMagnitude(data: list):
    return (np.abs(data))[0:len(data)//2]

# Given a fourier transform, get the phase (doesnt need to be fixed)


def getPhase(transform: list):
    return np.angle(transform)

# Given a fourier transform and fs, get the time vector (fixed)


def getTimeVector(data: list, fs: int):
    return np.arange(0, len(data))/fs

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


def getMaxMagnitude(magnitude, F):
    posm = np.where(magnitude == np.max(magnitude))
    return F[posm]


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
