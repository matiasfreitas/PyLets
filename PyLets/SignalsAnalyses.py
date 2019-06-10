import math
import numpy as np
from numba import njit, jit
from scipy import integrate

def TransFourier(tempo, sinal):
    """Analisa as frequencias de um sinal a partir da transformada de fourier
    """
    fft = np.fft.fft(sinal)
    T = tempo[1] - tempo[0]  # sampling interval 
    N = sinal.size

    # 1/T = frequency
    f = np.linspace(0, 1 / T, N)
    return [f[:N // 2],2*np.abs(fft)[:N // 2] * 1 / N, 1.5]
@jit
def TransWaleConti(tempo, dilatRange, RealSinal, WaveletFunction, WaveletType):
    matrix = np.zeros((len(dilatRange),len(tempo)))
    for a in range(0,len(dilatRange)):
        for b in range(0,len(tempo)):
            WaveletSinal = WaveletFunction(WaveletType, tempo, dilatRange[a], tempo[b])
            WaveletTransform = np.trapz(WaveletSinal*RealSinal, tempo)
            matrix[a][b] = (1/(dilatRange[a]**1/2))*WaveletTransform
        print(100/len(dilatRange)*a)
    return matrix





