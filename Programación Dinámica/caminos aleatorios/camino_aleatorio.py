from borracho import MiBorracho
from campo import Campo
from coordenadas import Coordenada

import random
from bokeh.plotting import figure, show

def graficar(x,y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    graficar(x,y)

    show(grafica)

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho(nombre='David')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_intentos+1):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simular_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simular_caminata,1))

    return distancias

def main(distancias_de_caminata, numero_intentos, tipo_borracho):
    distancia_por_caminata = []

    for pasos in distancias_de_caminata:
        print(f'El número del paso es {pasos}')
        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
        distancias_media = round(sum(distancias)/len(distancias),4)
        distancias_maxima = max(distancias)
        distancias_minima = min(distancias)
        distancia_por_caminata.append(distancias_media)
        distancia_por_caminata.append(distancias_maxima)
        distancia_por_caminata.append(distancias_media)

        print(f'{tipo_borracho. __name__ } caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancias_media}')
        print(f'Máxima = {distancias_maxima}')
        print(f'Mínima = {distancias_minima}')
        print('*' * 50)
    graficar(distancias_de_caminata, distancia_por_caminata )


if __name__=='__main__':

    distancias_de_caminata = [6,600,6000]
    numero_intentos =  1000

    main(distancias_de_caminata, numero_intentos, MiBorracho)
