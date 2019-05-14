from plotly.offline import plot
import plotly.graph_objs as go

#Gráficos

#    MatPlot
def WaveLetMatPlot(tempo, sinal):
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
    plt.plot(tempo, sinal)
    plt.show()

def FourierAnaliseGraph(FourierAnalise):
    """Gera um gráfico em Matplotlib de Barras feito para Analise de Fourier"""
    plt.figure()
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.bar(FourierAnalise[0],FourierAnalise[1], width=FourierAnalise[2])  # 1 / N is a normalization factor
    plt.show()

#    Plot.ly
def MakeAPlotlyScatter(sinal, tempo):
    return go.Scatter(
        y = sinal,
        x = tempo, 
        mode = 'lines+markers',
        line = dict(  color = "rgb(200, 0, 0)",
                  width = 4,
                  dash = 'dot'))

def WaveletPlotly(tempo, data, name):
    """Gera um gráfico em pyplot de linha feito para demonstração grafica de sinais
     Argumentos: 
        Tempo: Um numpy array com os valores do tempo
        Sinal: Um numpy Array com os valores do sinal em relação ao tempo
    Retorno:
        Salva um Grafico em html na pasta do arquivo"""

    layout = {
        "title": "Wavelets", 
        "xaxis": {
        "showgrid": False, 
        "title": "time"
    }, 
    "yaxis": {
        "showline": False, 
    "title": "Frequency"
        }
    }

    fig = go.Figure(data=data, layout=layout)

    plot(fig, filename= name + ".html")
