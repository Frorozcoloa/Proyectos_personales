class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f'{self.nombre} esta comiendo')

    def caminar(self):
        print(f'{self.nombre} esta caminado')

    def saltar(self):
        print(f'{self.nombre} esta saltando')

class Elefante(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)

    def saltar(self):
        print(f'{self.nombre} no puede saltar')

    def batido(self):
        print(f'{self.nombre} esta haciendo su batido')

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def ladrar(self):
        print(f'{self.nombre} esta ladrando')


def main():
    perro = Perro('Peluche')
    perro.comer()
    perro.caminar()
    perro.saltar()
    perro.ladrar()

    elefante = Elefante('Mani')
    elefante.comer()
    elefante.caminar()
    elefante.saltar()
    elefante.batido()

if __name__=='__main__':
    main()
