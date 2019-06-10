from plotly.offline import plot
import plotly.graph_objs as go

def MakeAPlotlyScatter(sinal, tempo):
    return go.Scatter(
        y = sinal,
        x = tempo, 
        mode = 'lines+markers',
        line = dict(  color = "rgb(200, 0, 0)",
                  width = 4,
                  dash = 'dot'))

def WaveletPlotly(data, name):
    """Gera um gráfico em pyplot de linha feito para demonstração grafica de sinais
     Argumentos: 
        data: Uma list de scatter do Plot.ly
        name: Nome do Arquivo HTML.
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

    plot.plot(fig, filename= name + ".html")
