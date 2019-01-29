from enum import Enum

class Cardinal(Enum):
    NORTH = 0
    EAST = 1
    WEST = 2
    SOUTH = 3


class Personaje:

    def __init__(self, pos: list, velocidad: int, vida: int):
        self.position = pos #[x,y]
        self.velocidad = velocidad
        self.vida = vida

    def recibir_ataque(self, dmg):
        self.vida = self.vida - dmg
        if self.vida <= 0:
            print("El personaje en x", self.position[0], "y en y", self.position[1], "murio")

    def mover(self, dist, cardinal: Cardinal):
        if cardinal == Cardinal.NORTH:
            self.position[1] = self.position[1] + dist

        if cardinal == Cardinal.EAST:
            self.position[0] = self.position[1] + dist

        if cardinal == Cardinal.WEST:
            self.position[0] = self.position[1] - dist

        if cardinal == Cardinal.SOUTH:
            self.position[1] = self.position[1] - dist


class Soldado(Personaje):

    def __init__(self, pos: list, velocidad: int, vida: int, atk: int):
        super(Soldado, self).__init__(pos, velocidad, vida)
        self.atk = atk

    def atacar(self, target: Personaje):
        target.recibir_ataque(self.atk)


class Campesino(Personaje):

    def __init__(self, pos: list, velocidad: int, vida: int, cosecha: int):
        super(Campesino, self).__init__(pos, velocidad, vida)
        self._cosecha = cosecha

    def cosechar(self):
        return self._cosecha


piolet = Soldado([1, 0], 10, 1, 5)
troski = Campesino([1, 1], 1, 1, 1)

print(str(troski.cosechar()))
piolet.atacar(troski)
piolet.mover(1, Cardinal.NORTH)

