class Corcho:
    bodega: str

class Botella:
    corcho: Corcho

class Sacacorchos:
    ultimoCorcho: Corcho = None

    def sacarCorcho(self, bottle: Botella):
        if self.ultimoCorcho is None:
            self.ultimoCorcho = bottle.corcho
            bottle.corcho = None
        else:
            print("Necesitas sacar el corcho primero")

    def limpiar(self):
        self.ultimoCorcho = None


corcho1 = Corcho()
corcho1.bodega = "Corcho 1"

corcho2 = Corcho()
corcho2.bodega = "Corcho 2"

btl1 = Botella()
btl1.corcho = corcho1

btl2 = Botella()
btl2.corcho = corcho2

sch = Sacacorchos()
sch.sacarCorcho(btl1)
print(sch.ultimoCorcho.bodega)
sch.sacarCorcho(btl2)
sch.limpiar()
sch.sacarCorcho(btl2)
print(sch.ultimoCorcho.bodega)
