# -*- coding: utf-8 -*-
from libs.grafico import Grafico
from collections import Counter
import random as rand

def barras():
    movies = ["Annie Hall", "Return of the King", "Casablanca", 
              "Gandhi", "West Side Story"]
    oscars = [5, 11, 3, 8, 10]
    
    xs = [i for i, _ in enumerate(movies)]
    
    plot = Grafico(False)
    plot.font.set_weight('bold')
    plot.p.bar(xs, oscars, color='g')
    
    for i, v in enumerate(oscars):
        plot.p.text(x=i-0.07, y=v+0.2, s=str("%d"%(v)), 
                 color='g', rotation=0, fontproperties=plot.font)
    
    # posições e nomes em posições marcadas
    plot.p.xticks(xs, movies)
    
    plot.titulo = "Filmes Favoritos"
    plot.eixo_y = "# de premiações"
    
    plot.show()

def histogram():
    grades = [83,95,91,87,70,30,85,82,100,67,73,77,0]
    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)    
    print(histogram)
    
    plt = Grafico(False)
    plt.p.bar([x for x in histogram.keys()],
               histogram.values(), 
               8)
    plt.p.axis([-6, 106, 0, 5])
    
    plt.p.xticks(range(0, 101, 10))
    plt.eixo_x = "Decil"
    plt.eixo_y = "# de Alunos"
    plt.titulo = "Distribuição das Notas do Teste 1"
    
    plt.show()

def linhas():
    # usando a cabeça pythonica
    variance = [2**i for i in range(9)]
    bias_square = sorted(variance, reverse=True)
    print(variance, bias_square)
    total_error = [x+y for x, y in zip(variance, bias_square)]
    xs = [i for i, _ in enumerate(variance)] # pra não usar valor fixo    
    print(total_error, xs)
    
    # múltiplas chamadas ao plot
    plot = Grafico()
    plot.XY(xs, 
            [variance, 'g:', 'variância'],
            [bias_square, 'r-.', 'polarização^2'],
            [total_error, 'b-', 'erro total'] )
    
    # significa posicionar a legenda em "top center"
    plot.p.legend(loc=9)
    plot.eixo_x = "complexidade do modelo"
    plot.titulo = "Relação entre Polarização e Variância"
    plot.show()

def dispersao():
    fmax = 100
    friends = [rand.randint(1,fmax) for _ in range(10)]
    minutes = [rand.randint(1,fmax) for _ in range(10)]
    labels = "abcdefghij"
    
    # cria o gráfico
    plot = Grafico(False)
    plot.titulo = "Minutos diários vs. Número de amigos"
    plot.eixo_x = "# de amigos"
    plot.eixo_y = "minutos diários passados no site"
    plot.font.set_weight("bold")
    plot.font.set_size("large")
    plot.p.axis([0, fmax, 0, fmax]) # eixos iguais
    
    # grafico de dispersão
    plot.p.scatter(friends, minutes, color='black')
    
    # nomeia cada posição (alternativa ao p.text)
    for label, friend, minute in zip(labels, friends, minutes):
        plot.p.annotate(label,
                        xy = (friend, minute),
                        xytext=(7, -4), # personaliza posição
                        textcoords='offset points',
                        fontproperties=plot.font)
    
    # exibe
    plot.show()
    
if __name__ == "__main__": dispersao()














