def checkSubString(target, subString):
    if subString in target:
        return True
    else:
        return False


def order(string1, string2):
    target = list([string1, string2])
    target.sort()
    return target[0]

goOn = True
while goOn:
    check = False
    while not check:
        try:
            choose = int(input("1.Comprobar si hay una cadena en otra\n2.Ordenar dos cadenas alfabeticamente\n3.Salir\n"))
            check = True
        except ValueError:
            print("Numero incorrecto vuelve a intentarlo")
            check = False

    if choose == 1:
        if checkSubString(input("Introduce el string en el que comprobar "), input("Introduce el string a buscar ")):
            print("Se encontro el string")
        else:
            print("No se encontro el String")
    if choose == 2:
        print(order(input("Introduce el primer string "), input("Introduce el segundo string ")))
    if choose == 3:
        goOn = False

