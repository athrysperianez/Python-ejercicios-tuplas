def iniciales(tuple):
    result = list()
    for x in tuple:
        result.append(x[2] + " " + x[1] + ". " + x[0])
    return result


tuple = (["De la fuente", "M", "Manolo"], ["Perez", "L", "Lucas"])
print(iniciales(tuple))