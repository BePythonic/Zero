# -*- coding: utf-8 -*-
__author__ = "Eduardo Galvani Massino"
__copyright__ = "Copyright 2017"
__email__ = "eduardo.massino@usp.br"

from fracao import Fracao
from math import ceil

# torna cada elemento da matriz um objeto do tipo Fracao
def rep_fracoes(matriz):
  l = len(matriz)
  for i in range(l):
    c = len(matriz[i])
    for j in range(c):
      if not matriz[i][j] is Fracao: 
        matriz[i][j] = Fracao(matriz[i][j])

# buscar a coluna e linha do pivo mais a esquerda a partir da linha dada
def busca_pos_pivo(matriz, linha):
  '''(list[], int) -> int, int'''
  for c in range(len(matriz[0])):
    l = linha
    while(l < len(matriz)):
      if(matriz[l][c] != Fracao(0)):
        return l, c
      l = l + 1
  return None, None

# buscar coluna do lider para subida Jordan
def busca_lider(matriz, linha):
  '''[list[], int] -> int'''
  col = -1
  for c in range(len(matriz[linha])):
    if(matriz[linha][c] == Fracao(1)):
      col = c
      break
  return col

# operacao elementar: multiplicacao de uma linha por um escalar (Fracao)
def multiplicar(matriz, linha, alfa):
  '''[list[], int, Fracao] -> None'''
  if(len(matriz) > 0):
    for col in range(len(matriz[linha])):
      matriz[linha][col] = matriz[linha][col] * alfa

# operacao elementar: trocar uma linha por outra
def trocar_linhas(matriz, yin, yang):
  matriz[yin], matriz[yang] = matriz[yang], matriz[yin]

# busca linhas totalmente nulas da matriz
def linhaNula(matriz):
  '''[list[]] -> int'''
  lins = len(matriz)
  if(lins == 0): return -1
  cols = len(matriz[0])
  for l in range(lins):
    nula = -1
    for c in range(cols):
      if(matriz[l][c] != Fracao(0)):
        nula = -1
        break
      nula = l
    if(nula != -1): break
  return nula

# metodo de eliminacao de Gauss-Jordan
def gaussJordan(matriz, show=False):
  '''[list[], bool] -> None'''
  lins = len(matriz)
  cols = len(matriz[0])

  if(show): print("\nEscalonamento passo-a-passo")

  # descendo via Gauss
  for lin in range(lins):
    # recupera elemento pivo
    pivo_l, pivo_c = busca_pos_pivo(matriz, lin)
    if(pivo_l is None): continue
    pivo = matriz[pivo_l][pivo_c]

    # troca linhas caso necessario
    if(pivo_l != lin):
      trocar_linhas(matriz, lin, pivo_l)
      if(show):
        showMatriz(matriz, 0)

    # normaliza a linha do pivo
    if(pivo != Fracao(1)):
      multiplicar(matriz, lin, Fracao(1)/pivo)
      if(show):
        showMatriz(matriz, 0)

    # zera elementos abaixo do pivo
    for l in range(lin+1, lins):
      m = matriz[l][pivo_c]
      for c in range(cols):
        matriz[l][c] = matriz[l][c] - m * matriz[lin][c]
      if(show):
        showMatriz(matriz, 0)

  # remove linhas nulas
  n = linhaNula(matriz)
  while(n != -1):
    del(matriz[n])
    lins = len(matriz)
    n = linhaNula(matriz)
    if(show):
        showMatriz(matriz, 0)

  # subindo via Jordan
  for lin in range(lins-1, -1, -1):
    # recupera coluna do elemento lider
    col = busca_lider(matriz, lin)
    if(col == -1):
      continue

    # zera elementos acima do lider
    for l in range(lin):
      m = matriz[l][col]
      for c in range(cols):
        matriz[l][c] = matriz[l][c] - m * matriz[lin][c]
      if(show and l < lin-1):
        showMatriz(matriz, 0)  

  # torna-se a matriz escalonada reduzida

# metodo de eliminacao de Gauss (fatoracao LU)
def gaussLU(matriz, show=False):
  '''[list[], bool] -> None'''
  lins = len(matriz)
  cols = len(matriz[0])

  if(show): print("\nFatoração LU")

  # descendo via Gauss
  for lin in range(lins):
    # recupera elemento pivo
    pivo_l, pivo_c = busca_pos_pivo(matriz, lin)
    if(pivo_l is None): continue
    pivo = matriz[pivo_l][pivo_c]

    # troca linhas caso necessario
    if(pivo_l != lin):
      trocar_linhas(matriz, lin, pivo_l)
      if(show):
        showMatriz(matriz, 0)

    # zera elementos abaixo do pivo
    for l in range(lin+1, lins):
      if(pivo == 0): continue
      m = matriz[l][pivo_c] / pivo
      for c in range(cols):
        matriz[l][c] = matriz[l][c] - m * matriz[lin][c]
      if(show and l < lins-1):
        showMatriz(matriz, 0)
  
  # torna-se a matriz triangular (LU)

# retorna numero de algarismos inteiros de um numero
def nlen(num):
  if(abs(num) < 1): return 1
  return 1 + len(str(int(abs(num))))

# retorna maior elemento de uma matriz
def maxDig(matriz):
  nlin = len(matriz)
  if(nlin < 1): return 0
  ncol = len(matriz[0])
  maior = len(matriz[nlin-1][ncol-1])
  for i in range(nlin):
    for j in range(ncol):
      if(len(matriz[i][j]) > maior):
        maior = len(matriz[i][j])
  return maior

# exibe matrizes visualmente
def showMatriz(matriz, dec=0):
  if(dec < 0): dec = 0
  nlin = len(matriz)
  if(nlin < 1): return
  ncol = len(matriz[0])
  ndig = maxDig(matriz) + dec + 1 # mais ponto e casas decimais
  ldig = nlen(nlin) + dec
  if(dec > 0):
    ldig -= 2
  print("\n%*c" %(ldig + 1, ' '), end="") # espacos
  # indices das colunas
  for j in range(1, ncol+1):
    for i in range(ndig-1):
      print(" ", end="")
    print("%d  " %(j), end="")
  # imprime cada linha da matriz
  for i in range(nlin):
    print("\n%*c" %(ldig + 1, ' '), end="") # espacos
    for j in range(ncol):
      print("+", end="")
      for t in range(ndig + 1):
        print("-", end="")
    print("+\n%*d |" %(ldig, i+1), end="") # indice da linha
    for j in range(ncol):
      #if(matriz[i][j] == 0): matriz[i][j] = 0
      if(dec > 0):
        print("%*.*lf |" %(ndig, ldig, matriz[i][j]), end="")
      else:
        esp = (ndig + 1 - len(matriz[i][j])) / 2
        print("%*c%s%*c|" %(ceil(esp), ' ', matriz[i][j], int(esp), ' '), end="")
  print("\n%*c" % (ldig + 1, ' '), end="") # espacos
  for j in range(ncol):
    print("+", end="")
    for t in range(ndig + 1):
      print("-", end="")
  print("+")
