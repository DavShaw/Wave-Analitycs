import numpy as np
import scipy.fftpack as fourier
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from functions import determinar_sexo

# Leemos el archivo de audio del directorio
Fs, data = waves.read("src/woman.wav")
# Si es estéreo, convertimos a mono seleccionando solo un canal
if len(data.shape) > 1:
    Audio_m = data[:, 0]  # Tomamos solo el primer canal
else:
    Audio_m = data  # El archivo ya es mono

# Tomamos la longitud de la señal
L = len(Audio_m)

# Definimos un vector de tiempo de la misma longitud de la señal
n = np.arange(0, L)/Fs

# Calculamos la FFt de la señal de audio
gk = fourier.fft(Audio_m)
# Tomamos la Magnitud de la FFT
M_gk = abs(gk)
# Tomamos la mitad de los datos (recordar la simetría de la transformada)
M_gk = M_gk[0:L//2]

Ph_gk = np.angle(gk)
F = Fs*np.arange(0, L//2)/L

# Encontramos la posición para la cual la Magnitud de FFT es máxima
Posm = np.where(M_gk == np.max(M_gk))
F_fund = F[Posm]

print(f"Max hz ({F_fund})")
sexo = determinar_sexo(F_fund)
print(f"Sexo: {sexo}")

plt.plot(F, M_gk)
plt.xlabel('Frecuencia (Hz)', fontsize='14')
plt.ylabel('Amplitud FFT', fontsize='14')
plt.show()
