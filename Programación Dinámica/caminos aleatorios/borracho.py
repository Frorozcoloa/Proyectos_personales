import random
class Borracho:


    def __init__(self, nombre):
        self.nombre = nombre



class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0 , 1), (0 , -1), (1 , 0), (-1 , 0)])


class MiBorracho(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(1,-2), (8,-12), (4,0), (34,8),(0,29),(54,60),(1,1)])
