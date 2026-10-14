def capitalize(names: list[str]) -> list[str]:
    new_name = []
    for name in names:
        p1 = name.split(" ")
        for i in range(len(p1)):
            p1[i] = p1[i][0].upper() + p1[i][1:].lower()

        new_name.append(" ".join(p1))

    return new_name


print(capitalize(["ali", "REYHANEH", "aMIR", "AMIR abbas", "Fatemeh Zahra"]))
