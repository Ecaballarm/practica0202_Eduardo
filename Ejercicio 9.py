cantidad = float(input("Introduce cantidad:"))
interes = float(input("Introduce interes porcentual:"))
años = int(input("Introduce numero de años:"))
print("Capital final:" + str(round(cantidad * (interes / 100 + 1)** años, 2)))