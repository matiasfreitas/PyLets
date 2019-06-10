from matplotlib import pyplot as plt

#    MatPlot
def WaleMatPlot(tempo, sinal, salve = 1, name = "Sinal.png"):
    """Gera um gráfico em Matplotlib de linha feito para demonstração grafica de sinais
    Argumentos: 
        Tempo: Um numpy array com os valores do tempo
        Sinal: Uma lista de numpy Array com os valores do sinal em relação ao tempo
        Salve: 1 para gravar em PNG, 0 para exibir em Pop Up
        Name: Nome do arquivo em caso de salvar png
    Retorno:
        Exibe um Grafico
    
    """

    plt.figure(2)
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    for x in sinal:
        plt.plot(tempo, x)
    if salve:
        plt.savefig(name)
        plt.clf()
    else:
        plt.show()
        plt.clf()

def TransFourierGraph(FourierAnalise, salve = 1, name = "Transformada Fourier.png"):
    """Gera um gráfico em Matplotlib de linha feito para demonstração grafica da transformada de de Fourier
    Argumentos: 
        FourierAnalise: Array da Transformada de de Fourier
        Salve: 1 para gravar em PNG, 0 para exibir em Pop Up
        Name: Nome do arquivo em caso de salvar png
    Retorno:
        Exibe um Grafico
    """
    plt.figure()
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.bar(FourierAnalise[0],FourierAnalise[1], width=FourierAnalise[2]) 
    if salve:
        plt.savefig(name)
        plt.clf()
    else:
        plt.show()
        plt.clf()

def TransWaleContGraph(Matrix, salve = 1, name = "Transformada Wavelet.png"):
    """Gera um gráfico em Matplotlib de linha feito para demonstração grafica da transformada de Wavelet
    Argumentos: 
        Matrix: Uma Numpy Matrix da Transformada de Wavelet
        Salve: 1 para gravar em PNG, 0 para exibir em Pop Up
        Name: Nome do arquivo em caso de salvar png
    Retorno:
        Exibe um Grafico
    
    """
    plt.imshow(Matrix, cmap='PRGn', aspect='auto')
    
    if salve:
        plt.savefig(name)
        plt.clf()
    else:
        plt.show()
        plt.clf()