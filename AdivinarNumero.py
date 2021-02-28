import random

numero = random.randrange(1,10)
anum = int (input("Adivina el número entre el 1 al 10: "))
var = 0

while anum != numero:
    if anum < numero:
        print("Este no es el número, intentalo de nuevo")
        anum = int (input("\nAdivina el número entre el 1 al 10: "))
        var = var + 1
    else:
        print("Necesitas poner un número dentro del limite, intentalo de nuevo")
        anum = int (input("\nAdivina el número entre el 1 al 10: "))
        var = var + 1

print("Felicidades, adivinaste el numero")
print("Total de intentos " + str(var))
