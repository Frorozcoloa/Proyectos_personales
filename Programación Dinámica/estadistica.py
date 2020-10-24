import random
import math
import numpy as np

def media(X):
    return sum(X) / len(X)

def varaniza(X):
    mu=media(X)

    acumulador = 0
    for x in X:
        acumulador += (x-mu)**2

    return acumulador/len(X)

def deviacion_estandar(X):
    return (varaniza(X))**0.5

if __name__=='__main__':
    X=[random.randint(1,21) for i in range(20)]
    mu=media(X)
    var=varaniza(X)
    sigma=deviacion_estandar(X)
    print(f'Lista de número = {X}')
    print(f'La media= {mu}')
    print(f'La varaniza= {var} ')
    print(f'La deviación estandar= {sigma}')
