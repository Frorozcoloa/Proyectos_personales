import random
from estadistica import media
from bokeh.plotting import figure,show
from bokeh.layouts import row

def tirar_dado(numero_tiros):
    secuencia_de_tiros = [ ]

    for _ in range(numero_tiros):
        tiro_1 = random.choice([1,2,3,4,5,6])
        tiro_2 = random.choice([1,2,3,4,5,6])
        tiro = tiro_1 + tiro_2
        secuencia_de_tiros.append(tiro)
    media_de_tiro = media(secuencia_de_tiros)
    return media_de_tiro


def estimacion_media(numero_de_tiros):

    medias=[]
    for _ in range(numero_de_tiros):
        media = tirar_dado(numero_de_tiros)
        medias.append(media)

    return medias

def graficar(medias):
    numero_de_dado = list(range(1,7))
    p = figure(title='Distribución de medias de los dados', x_axis_label='Numero del dado', y_axis_labe='Cantidad')
    p.vbar(x=numero_de_dado,y=medias)
    show(p)



# def main(numero_de_tiros,numero_de_intentos):
#     tiros = []
#     for _ in range(numero_de_intentos):
#         secuencia_de_tiros = tirar_dado(numero_de_tiros)
#         tiros.append(secuencia_de_tiros)
#
#     tiros_con_1=0
#     for tiro in tiros:
#         if 12 in tiro:
#             tiros_con_1 += 1
#
#
#     probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
#     print(f'Probabilidad de  obtener por lo menos un 1 en {numero_de_tiros} tiros={probabilidad_tiros_con_1}')
#
#

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tidros del dado: '))
    # numero_de_intentos = int(input('Cuantas veces correrá la simulación: '))
    # main(numero_de_tiros, numero_de_intentos)
    medias=estimacion_media(numero_de_tiros)
    graficar(medias)
