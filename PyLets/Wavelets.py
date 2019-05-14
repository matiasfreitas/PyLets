import math
import numpy as np
import scipy.integrate as integrate

def SinalBasico(Tempo, Frequencia, Amplitude):
    return Amplitude*np.sin(Frequencia*2*np.pi*Tempo)

def EnergiaWale(arrayWavelet):
    return integrate.simps((arrayWavelet)**2)

def WaleNormaliza(funcWavelet,tempo,dilat,posic):
    wavelet = funcWavelet(tempo,dilat,posic)
    Energia = EnergiaWale(wavelet)
    return 1/(Energia**(1/2))*(wavelet)

def WaleNotNormaliza(funcWavelet,tempo,dilat,posic):
    wavelet = funcWavelet(tempo,dilat,posic)
    return wavelet

def HermitianHat (tempo,dilat,posic ):
    """Retornar um array das posições de uma OndaLet(Chápeu de Hermitian) em relação ao tempo
    
    Argumentos:
        tempo: um Numpy Array com os pontos do sinal que serão exibido
        dilat: O valor de dilatação da Wavelet
        posic: O valor da posição em relação ao tempo da Wavelet

    Retorno:
        Retorna um Array 2D com os valores de Amplitude em relação ao tempo."""

    t = ((tempo-posic)/dilat)
    return 2/(5**(1/2))*math.pi**-(1/4)*t*(1+t)*math.e**((-1/2)*t**2)

def MexicanHat (tempo,dilat,posic):
    """Retornar um array das posições de uma OndaLet(Chápeu de mexicano) em relação ao tempo
    
    Argumentos:
        tempo: um Numpy Array com os pontos do sinal que serão exibido
        dilat: O valor de dilatação da Wavelet
        posic: O valor da posição em relação ao tempo da Wavelet

    Retorno:
        Retorna um Array 2D com os valores de Amplitude em relação ao tempo."""
    t = ((tempo-posic)/dilat)
    return (1-t**2)*math.e**((t**2/2)*-1)
    
def MeyerWale (tempo,dilat,posic ):
    """Retornar um array das posições de uma OndaLet(Meyer) em relação ao tempo
    
    Argumentos:
        tempo: um Numpy Array com os pontos do sinal que serão exibido
        dilat: O valor de dilatação da Wavelet
        posic: O valor da posição em relação ao tempo da Wavelet

    Retorno:
        Retorna um Array 2D com os valores de Amplitude em relação ao tempo.
        
        Formando a imagem correta(provavelmente), mas com problemas no deslocamento do eixo do tempo, indo da direita pra esquerda"""

    t = ((tempo-posic)/dilat)
    outputArray = np.array([])
    for x in t:
        if x == 0:
            output = 2/3 + 4/(3*math.pi)
        else: 
            output = ((np.sin((2*math.pi)/(3)*x)+(4/3)*x*np.cos(((4*math.pi)/3)*x))/(math.pi*x-(16*math.pi/9)*(x**3)))
            output = output 
        outputArray = np.append(output, outputArray)
    return outputArray

def HermitianWale1(tempo,dilat,posic):

    t = ((tempo-posic)/dilat)
    return (2**(1/2))*math.pi**(-1/4)*t*math.e**((-t**2)/2)