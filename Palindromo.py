var = 1

while var < 5:
    palabraNormal = input("Introduce la palabra " + str(var)+": ")
    palabraInvertida = palabraNormal[::-1]

    if(palabraNormal == palabraInvertida):
        print("Muy bien, estas palabras son iguales del derecho al revez.")
        var = var + 1
    else:
        print("Esto no es un palindromo.")
        var = var + 1
