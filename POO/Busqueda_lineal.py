import random
def busqueda_lineal(lista, objetivo):
    return objetivo in lista # O(n)
    # match = False
    # for elemento in lista: #o(n)
    #     if elemento == objetivo:
    #         match= True
    #         break


    # return match

if __name__=='__main__':
    tamano_de_lista = int(input('De que tamaño será la lista? '))
    objetivo = int(input('El número a buscar? '))

    lista=[random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    encontrar = busqueda_lineal(lista,objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrar else "no esta"} en la lista')
