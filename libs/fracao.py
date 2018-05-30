# -*- coding: utf-8 -*-
'''
Created on 8 de ago de 2017

@author: Eduardo Galvani Massino
'''
class Fracao:
    '''
    Classe para armazenar/manipular frações
    '''
    def __init__(self, n=0, d=1):
        '''(Fracao, int, int) -> None
        Construtor
        '''
        self.num = n
        self.den = d
        self.simplifique()

    def __str__(self):
        '''(Fracao) -> str
        Usada pelo print, representação do objeto
        na forma de string
        '''
        if self.den == 1:
            return "%d" %(self.num)
        return "%d / %d" %(self.num, self.den)

    def __len__(self):
        '''(Fracao) -> int'''
        return len(str(self))

    def __add__(self, other):
        '''(Fracao, Fracao) -> Fracao
        substitui operador + '''
        novo_num = self.num * other.den + other.num * self.den
        novo_den = self.den * other.den
        return Fracao(novo_num, novo_den)

    def __sub__(self, other):
        '''(Fracao, Fracao) -> Fracao
        substitui operador - '''
        novo_num = self.num * other.den - other.num * self.den
        novo_den = self.den * other.den
        return Fracao(novo_num, novo_den)

    def __mul__(self, other):
        '''(Fracao, Fracao) -> Fracao
        substitui operador * '''
        novo_num = self.num * other.num
        novo_den = self.den * other.den
        return Fracao(novo_num, novo_den)

    def pot(self, n):
        '''(Fracao, int) -> Fracao
        exponenciando as fracoes **'''
        res = Fracao(1)
        for i in range(n):
            res *= self
        return res

    def __truediv__(self, other):
        '''(Fracao, Fracao) -> Fracao
        substitui operador / '''
        novo_num = self.num * other.den
        novo_den = self.den * other.num
        return Fracao(novo_num, novo_den)

    def __eq__(self, other):
        '''(Fracao, Fracao) -> bool'''
        aux = self - other
        return aux.num == 0

    def __ne__(self, other):
        '''(Fracao, Fracao) -> bool'''
        return not self == other

    def __lt__(self, other):
        '''(Fracao, Fracao) -> bool'''
        aux = self - other
        return aux.num < 0

    def __le__(self, other):
        '''(Fracao, Fracao) -> bool'''
        return self < other or self == other

    def __gt__(self, other):
        '''(Fracao, Fracao) -> bool'''
        return not self <= other

    def __ge__(self, other):
        '''(Fracao, Fracao) -> bool'''
        return not self < other

    def simplifique(self):
        '''(Fracao) -> None'''
        if self.den == 0:
            return None
        if self.num == 0:
            self.den = 1
            return None
        c = mdc(self.num, self.den)
        self.num //= c
        self.den //= c

    def dec(self):
        '''(Fracao) -> float
        Representação Decimal '''
        return self.num / self.den

# MDC via método de Euclides
def mdc(m, n):
    '''(int, int) -> int'''
    if m == 0:
        return n
    elif n == 0:
        return m

    resto = m % n
    while resto != 0:
        m, n = n, resto
        resto = m % n
    return n

# MMC que usa o MDC
def mmc(m, n):
    '''(int, int) -> int'''
    if m == 0 or n == 0:
        return 0
    if m < 0:
        m = -m
    if n < 0:
        n = -n

    return (n*m) // mdc(m, n)

# um main para testes
def main():

    a = Fracao(1, 2)
    b = Fracao(2, 3)
    c = Fracao(3, 4)
    d = a+b+c
    pa = a/d
    pb = b/d
    pc = c/d
    print(d, d.dec())
    print(pa, "=", pa.dec())
    print(pb, "=", pb.dec())
    print(pc, "=", pc.dec())
    print(pa+pb+pc)
    print("%f"%(pa.dec()+pb.dec()+pc.dec()))
    

# não modificar
if __name__ == "__main__":
    main()