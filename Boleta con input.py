# descuento del 30% en boleta
a= float(input("Ingrese precio del pollo"))
b= float(input("Ingrese precio de la mayonesa"))
c= float(input("Ingrese precio del arroz"))
d = a + b + c
print("Boleta\nPollo     " + str(a) + "\nMayonesa     " + str(b) + "\nArroz     " + str(c) + "\nTotal     " + str(round(d, 2)) + "\nTotal con descuento     "+ str(d-(d/100)*30))

