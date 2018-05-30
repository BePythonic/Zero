# -*- coding: utf-8 -*-
from libs.file_aux import FileAux
from libs.grafico import Grafico
from collections import Counter

alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_ext = alfabeto+"-çàâãáêéíóôõú"

def clean(palavra):
    '''(str -> str, str)
    Limpa a palavra obtida, retornando também o lixo
    '''
    nova, resto = "", ""
    for letra in palavra.lower():
        if letra in alfabeto_ext:
            nova += letra
        else:
            resto += letra
    return nova, resto

def graf_letras(letras, qtde_letras, t):
    '''(list, int) -> None'''
    # gerando lista de frequencias de letras
    x, y = zip(*letras)
    def rel(y): return y /qtde_letras
    y = list(map(rel, y)) # matplot aceita lista e não iterable
    n = range(len(x))
    
    # gráfico da frequência de letras
    plot = Grafico(False)
    plot.titulo = "Frequência de letras em %s"%t
    plot.p.xticks(n, x)
    plot.p.axis(ymax=max(y)*1.2)
    plot.p.bar(n, y, width=0.5, color='red')
    plot.p.text.unicode = True    
    for i, v in enumerate(y):
        plot.p.text(x=i-0.1, y=v+0.018, s=str("%.3f%%"%(v*100)), 
                 color='red', rotation=75)
    plot.show()
    
def graf_palavras(palavras, qtde_palavras, t):
    '''(list, int) -> None'''
    # gerando lista de frequencias de palavras
    x, y = zip(*palavras[10:50])
    def rel(y): return y / qtde_palavras
    y = list(map(rel, y)) # matplot aceita lista e não iterable
    m = range(len(x))
    
    # gráfico da frequência de palavras
    plot = Grafico(False)
    plot.titulo = "As 40 palavras mais frequentes de %s"%t
    plot.p.xticks(m, x, rotation=60)
    plot.p.axis(ymax=max(y)*1.2)
    plot.p.bar(m, y, width=0.8, color='green')
    for i, v in enumerate(y):
        plot.p.text(x=i-0.3, y=v+0.002, s=str("%.3f%%"%(v*100)), 
                 color='green', rotation=75)
    plot.show()

def main():
    t = "Senhor dos Anéis"
    arquivo = "lotr.txt"
    arq = FileAux(arquivo)
    arq2 = open(arquivo, encoding="utf8")
    
    # percorrendo o arquivo e contando palavras
    palavras = {}
    palavra = arq.getPalavra()
    while palavra is not None:
        palavra, _ = clean(palavra)
        if palavra != "":
            qtde = palavras.get(palavra, 0)
            palavras[palavra] = qtde + 1        
        palavra = arq.getPalavra()
    
    # Usando classe Counter para contar letras
    letras = Counter()
    for linha in arq2:
        letras += Counter(linha.lower())
    arq2.close()
    
    # convertendo para lista de tuplas (key, value)
    palavras_t = palavras.items()
    letras_t = letras.items()
    
    # removendo letras indesejadas
    for letra, _ in list(letras_t):
        if letra not in alfabeto:
            del letras[letra]
    qtde_letras = sum(letras.values())
    
    # ordenando as listas
    letras = sorted(letras_t, key=lambda x: x[0], reverse=False)
    palavras = sorted(palavras_t, key=lambda x: x[1], reverse=True)
        
    # gerando os gráficos
    graf_letras(letras, qtde_letras, t)        
    graf_palavras(palavras, arq.qtde_palavras, t)
    

if __name__ == "__main__": main()