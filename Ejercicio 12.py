barras = int(input("Numero de barras que no son del dia:"))
precio = 3.49
descuento = 0.6
coste = barras * precio * (1-descuento)
print("El coste de una barra del dia es " + str(precio) + "€")
print("El descuento de una barra de pan no del dia es " + str(descuento * 100) + "%")
print("El coste a pagar es " + str(round(coste, 2)) + "€")