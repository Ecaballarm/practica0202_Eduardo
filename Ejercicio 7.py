peso = input("Indica tu peso:")
altura = input("Indica tu estatura:")
imc = round(float(peso)/float(estatura)**2.2)
print("Tu IMC es: ") + str(imc)