lista=[7,3,1,2,4,6]

for i in range(1, len(lista)):
    valor_actual = lista[i]
    posicion_actual = i
    while posicion_actual > 0 and lista[posicion_actual-1]>valor_actual:
        lista[posicion_actual]=lista[posicion_actual-1]
        print(f'lista = {lista} valor actual {valor_actual}')
        posicion_actual-=1


    lista[posicion_actual] = valor_actual
print(f'lista ordenada{lista}')
