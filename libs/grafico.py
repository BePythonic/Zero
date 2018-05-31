# -*- coding: utf-8 -*-
# @author Eduardo
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot

class Grafico:
    def __init__(self, grid=True):
        '''(Grafico, bool) -> None
        Cria o gráfico com ou sem grid
        '''
        self.p = matplotlib.pyplot
        self.grid = grid
        self.titulo = ""
        self.eixo_x = ""
        self.eixo_y = ""
        self.font = FontProperties()
        self.setTamanho()

    def setOpcoes(self):
        '''(Grafico, dict) -> None
        Configura título e textos dos eixos
        '''
        self.p.title(self.titulo)
        self.p.grid(self.grid)
        self.p.xlabel(self.eixo_x)
        self.p.ylabel(self.eixo_y)
    
    def setTamanho(self, tamanho=(25,20)):
        '''(Grafico, tuple) -> None
        Configura o tamanho do gráfico em centímetros
        '''
        def to_cm(x): return x / 2.54
        self.p.rcParams["figure.figsize"] = tuple(map(to_cm, tamanho))

    def XY(self, X, *Y):
        '''(Grafico, list, list of lists) -> None
        Gráfico XY de vários conjuntos imagem em Y
        onde tem que pertencer ao mesmo domínio X
        '''
        for y, estilo, lbl in Y:
            self.p.plot(X, y, estilo, label=lbl)
            
    def show(self):
        '''(Grafico) -> None
        Mostra o gráfico
        '''
        self.setOpcoes()
        self.p.show()
