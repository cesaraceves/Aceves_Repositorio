correo = input("Introduce tu correo electrónico: ").strip()

nombreUsuario = correo[:correo.index("@")]

dominio = correo[correo.index("@")+1:]

res = "Tu nombre de usuario es: {}\nTu dominio es: {}".format(nombreUsuario, dominio)
print(res)

