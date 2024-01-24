print("Que tipo de comida quieres hoy? ")
comida = input("1.)Italiana \n2.)Mexicana \n3.)China\n")
comida = int(comida)
if comida == 1:
    print("Te recomiendo ir a Mia Pizza, es la mejor comida italiana de la ciudad!")
elif comida == 2:
    print("Taquitos al pastor no falla en estas situaciones!")
elif comida == 3:
    print("Pollito agridulce en Soy Wok es muy rico y economico!")
else:
    print("Escoge una opcion correcta")