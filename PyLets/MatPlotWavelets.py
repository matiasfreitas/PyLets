from matplotlib import pyplot as plt

#    MatPlot
def WaleMatPlot(tempo, sinal):
    """Gera um gráfico em Matplotlib de linha feito para demonstração grafica de sinais
    Argumentos: 
        Tempo: Um numpy array com os valores do tempo
        Sinal: Um numpy Array com os valores do sinal em relação ao tempo
    Retorno:
        Exibe um Grafico
    
    """
    

    plt.figure()
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    for x in sinal:
        plt.plot(tempo, x)
    plt.show()

def TransFourierGraph(FourierAnalise):
    """Gera um gráfico em Matplotlib de Barras feito para Analise de Fourier"""
    plt.figure()
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.bar(FourierAnalise[0],FourierAnalise[1], width=FourierAnalise[2])  # 1 / N is a normalization factor
    plt.show()

def TransWaleContGraph(Matrix):
    plt.imshow(Matrix, cmap='PRGn', aspect='auto')
    plt.show()