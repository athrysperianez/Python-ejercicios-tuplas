import sys


def loopMenu(data:dict):
    name = input("Introduce un nombre para buscar/introducir, introduce * para salir ")
    if name == "*":
        sys.exit()
    else:
       tlf = data.get(name, None)

    if tlf is not None:
        print(name, "-", str(tlf))
    else:
        check = False
        while not check:
            try:
                command = int(input("Introduce un tlf para incluirlo junto a el nombre o introduce * para salir "))
                check = True
            except ValueError:
                print("Numero incorrecto, vuelve a intentarlo")
                check = False
        data[name] = command
    return data


data = {"Alberto": 42104921}

while True:
    loopMenu(data)
