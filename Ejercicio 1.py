def separar(target, character):
    targetAr = list(target)
    result = ""
    for x in targetAr:
        result += x + character
    return result


def deleteWhiteSpaces(target, character):
    targetAr = list(target)
    result = ""
    for x in targetAr:
        if x.isspace():
            result += character
        else:
            result += x
    return result


def replaceNum(target, character):
    targetAr = list(target)
    result = ""
    for x in targetAr:
        if x.isnumeric():
            result += character
        else:
            result += x


def insertarCada(target, character, numIndex):
    result = ""
    tmpIndex = 1
    targetAr = list(target)
    for x in targetAr:
        if tmpIndex == numIndex:
            tmpIndex = 0
            result += x + character
        else:
            result += x
        tmpIndex += 1
    return result

    print(result)
    seguir = True
    while seguir:
        numCheck = False
        while not numCheck:
            print(
                "1.Separar caracteres\n2.Remplazar espacios\n3.Transformar numeros\n4.Insertar caracter cada X "
                "digitos\n5.Salir")
            try:
                choose = int(input("Introduce una opcion: "))
                if choose is None:
                    raise ValueError
                numCheck = True
            except ValueError:
                print("Numero no valido, prueba de nuevo")
                numCheck = False
        if choose == 1:
            print(separar(input("Introduce la cadena a separar "), input("Introduce el caracter para separar ")))
        if choose == 2:
            print(deleteWhiteSpaces(input("Introduce la cadena en la que eliminar los espacios "),
                                    input("Introduce el caracter a usuar ")))
        if choose == 3:
            print(replaceNum(input("Introduce la cadena en la que eliminar los numeros "),
                             input("Introduce el caracter ")))

        if choose == 4:
            numCheck = False
            while not numCheck:
                try:
                    target = input("Introduce la cadena en la que introducir el caracter ")
                    numIndex = int(input("Indica cada cuantos caracteres se introducira el caracter "))
                    character = input("Introduce el caracter ")
                    numCheck = True
                except ValueError:
                    print("Numero no valido, prueba de nuevo")
                    numCheck = False
            print(insertarCada(target, character, numIndex))
        if choose == 5:
            seguir = False

        print()
