print("#----------------------------#")
print("#--| calculadora de areas |--#")
print("#----------------------------#")
print("#--| 1) cuadrado          |--#")
print("#--| 2) rectángulo        |--#")
print("#--| 3) círculo           |--#")
print("#----------------------------#")
opcion = input("seleccione una opcion: ")
if opcion == "1":
    lado = float(input("ingrese el lado del cuadrado: "))
    area = lado * lado
    print("area del cuadrado:", int(area) if area.is_integer() else area)
elif opcion == "2":
    base = float(input("ingrese la base del rectangulo: "))
    altura = float(input("ingrese la altura del rectangulo: "))
    area = base * altura
    print("area del rectangulo:", int(area) if area.is_integer() else area)
elif opcion == "3":
    radio = float(input("ingrese el radio del circulo: "))
    area = 3.1416 * radio * radio
    print("area del circulo:", round(area, 2))
else:
    print("opcion no valida")