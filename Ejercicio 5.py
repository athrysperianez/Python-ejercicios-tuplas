def buscar(targetTuple, stringToLook):
    result = list()
    i = 0
    for x in targetTuple:
        if stringToLook in x[0] or stringToLook in x[1]:
            result.append(x)
            i += 1
    return result


print(buscar([("Prueba", "123456789")], "i"))