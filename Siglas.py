cadena = input("Introduzca varias palabras: ")
palabras = cadena.split()
print (palabras)
newString = " "
for p in palabras :
    newString = newString + p[0]
print( newString )
