def saludate(tuple, origin, ammount):
    i = origin - 1
    while i < len(tuple) and i < ammount:
        x = tuple[i]
        if x[1] == "Male":
            print("Estimado " + x[0] + " vote por mi.")

        if x[1] == "Female":
            print("Estimada " + x[0] + " vote por mi.")

        if x[1] == "Other":
            print("Estimade " + x[0] + " vote por mi.")
        i += 1


tuple = (("Manolo", "Male"), ("Alicia", "Female"), ("Alberto", "Other"))
saludate(tuple, 1, 3)
