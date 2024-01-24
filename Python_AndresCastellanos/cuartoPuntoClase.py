password = input("Define la contrasena: \n")
condicion = True

while condicion:
    comprobante  = input("Escribe la contrasena para ingresar")
    if comprobante != password:
        print("Sigue intentando")
    elif comprobante == password:
        print("Estamos dentro!\n")
        condicion = False
    