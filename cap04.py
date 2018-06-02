# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:12:29 2018

@author: Eduardo
"""
from functools import reduce
from math import sqrt, acos, pi
import random as rand

#----------------------------------------------------------------#

def vector_add(v, w):
    '''(list, list) -> list
    soma componente a componente
    '''
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_sub(v, w):
    '''(list, list) -> list
    soma componente a componente
    '''
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    '''(list of lists) -> list
    Soma uma lista de vetores
    '''
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    '''(float, list) -> list
    Multiplica um escalar por um vetor
    '''
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    '''(list of lists) -> list
    Computa o vetor médio entre os vetores
    '''
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))

def dot(v, w):
    '''(list, list) -> float
    Retorna o produto escalar de v por w
    '''
    return sum((vi * wi for vi, wi in zip(v, w)))

def sum_of_squares(v):
    '''(list) -> float
    Soma dos quadrados das componentes
    '''
    return dot(v, v)

def magnitude(v):
    '''(list) -> float
    Retorna a magnitude do vetor v
    '''
    return sqrt(sum_of_squares(v))

def angle(v, w):
    '''(list, list) -> float
    Calcula ângulo entre os vetores em graus
    '''
    cos = dot(v, w) / magnitude(v) / magnitude(w)
    return acos(cos) * 180 / pi

def squared_distance(v, w):
    '''(list, list) -> float
    Distância quadrada entre 2 vetores
    '''
    return sum_of_squares(vector_sub(v, w))

def distancia(v, w):
    '''(list, list) -> float
    Distância euclidiana entre 2 vetores
    '''
    return magnitude(vector_sub(v, w))

def vetores():
    v = [rand.randint(-9,9) for _ in range(3)]
    w = [rand.randint(-9,9) for _ in range(3)]
    V = [[rand.randint(-9,9) for _ in range(4)]
         for _ in range(4)]
    
    print(list(zip(v, w)))
    
    print("vetores aleatórios", V)
    print("soma", vector_sum(V))
    print("media", vector_mean(V))
    
    print("v", v, ", w", w)
    print("v + w =", vector_add(v, w))
    print("v - w =", vector_sub(v, w))
    print("v.w =", dot(v, w))
    print("angle =", angle(v, w))
    print("|v|^2 =", sum_of_squares(v))
    print("|w|^2 =", sum_of_squares(w))
    print("|v| =", magnitude(v))
    print("|w| =", magnitude(w))
    print("|v-w|^2 =", squared_distance(v, w))
    print("|v-w| =", distancia(v, w))
    
#----------------------------------------------------------------#

def shape(A):
    '''(matriz) -> int, int
    Retorna número de linhas e colunas da matriz
    '''
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # num de elementos da primeira linha
    return num_rows, num_cols

def get_row(A, i):
    '''(matriz, int) -> vetor
    Retorna i-ésima linha da matriz como um vetor
    '''
    return A[i]

def get_col(A, j):
    '''(matriz, int) -> vetor
    Retorna j-ésima coluna da matriz como um vetor
    '''
    return [A_i[j] for A_i in A]

def transposta(A):
    '''(matriz) -> matriz
    Retorna a transposta da matriz A
    '''
    num_cols = len(A[0]) # num de colunas -> será o de linhas
    return [get_col(A, j)
            for j in range(num_cols)]

def make_matrix(m, n, f):
    '''(int, int, function) -> matriz
    Cria uma matriz m X n a partir da função geradora f
    '''
    return [[f(i, j)
            for j in range(n)] # colunas
            for i in range(m)] # linhas

def gen_identidade(i, j):
    '''(int, int) -> int
    Função geradora da matriz identidade
    '''
    return 1 if i == j else 0

def matrizes():
    A = [[rand.randint(-9,9) for _ in range(3)]
         for _ in range(2)]  # linhas
    
    print(shape(A))
    print("A >>", A)
    print("A^T >>", transposta(A))
    print(get_row(A, 0))
    print(get_col(A, 0))
    
    B = make_matrix(5, 5, gen_identidade)
    print(B)
    print(transposta(B))
    
#----------------------------------------------------------------#

if __name__ == "__main__": 
    vetores()
    print("\n%s\n"%("#"*75))
    matrizes()