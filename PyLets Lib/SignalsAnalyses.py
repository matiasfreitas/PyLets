import math
import numpy as np
import scipy.integrate as integrate

def TransFourier(tempo, sinal):
    """Analisa as frequencias de um sinal a partir da transformada de fourier
    """
    fft = np.fft.fft(sinal)
    T = tempo[1] - tempo[0]  # sampling interval 
    N = sinal.size

    # 1/T = frequency
    f = np.linspace(0, 1 / T, N)
    return [f[:N // 2],2*np.abs(fft)[:N // 2] * 1 / N, 1.5]

def TransWaleConti(tempo, dilatRange, RealSinal, WaveletFunction, WaveletType):
    matrix = np.matrix([])
    for a in dilatRange:
        linha = np.array([])
        for b in tempo:
            WaveletSinal = WaveletFunction(WaveletType, tempo, a, b)
            WaveletTransform = integrate.simps(WaveletSinal*RealSinal, tempo)
            linha = np.append( (1/(a**1/2))*WaveletTransform, linha)
        print(100/dilatRange[-1]*a)
        matrix = np.append(linha, matrix)
    matrix = matrix.reshape(len(RealSinal), len(dilatRange))
    return matrix
