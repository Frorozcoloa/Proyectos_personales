import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = list(range(1,14))
print(VALORES)
def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)


    corrida = 0
    for mano in manos:
        valores = []
        palos = []
        for carta in mano:
            valores.append(carta[1])

        counter_valores = dict(collections.Counter(valores))
        buscar_escalera = sorted(list(counter_valores.keys()))
        

        if len(buscar_escalera) == tamano_mano :
            if (buscar_escalera[0]-buscar_escalera[tamano_mano-1])== tamano_mano-1 or buscar_escalera[0]-buscar_escalera[tamano_mano-1] == 12:
                corrida += 1
                print(corrida)


    probabilidad_escalera = round(corrida / intentos,100)
    print()

    print(f'La probabilidad de obtener una corrida en una mano de {tamano_mano} barajas es {probabilidad_escalera} ')


if __name__=='__main__':

    while True:
        tamano_mano = int(input('Tamaño de la mano: '))
        if tamano_mano <= 52 and tamano_mano > 0:
            intentos = int(input('Cuantos intentos para calcular la probabilidad: '))
            main(tamano_mano, intentos)
            opcion = input('Quieres volverlo a correr? ')
            print('**'*50)
            if not opcion == 'si':
                break
        else:
            print('Debe ser un numero del 1 al 52')
            print('**'*50)
