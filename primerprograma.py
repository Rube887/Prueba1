variable1 = int(input("Ingresa un numero positivo."))
variable2 = variable1
suma = 0
while variable1 > 0:
    suma += variable1
    variable1 -=1
print("La variable ingresada es " + str(variable2) + ".")
print("La suma es " + str(suma) + ".")