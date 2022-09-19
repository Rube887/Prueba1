import copy
#El copy module funciona para poder otorgar a otra variable la lista y volverla independiente a cambios en la lista
ex_12 = [1, 2, 3, 4, 5]
ex_13 = copy.deepcopy(ex_12)
ex_12[1] = 5
print(ex_12)
print(ex_13)