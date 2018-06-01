
import random as rd

precios = []
contador = 0

while contador < 30:
    precios.append((rd.random()*21) + 130)
    contador = contador + 1

suma = 0
for precio in precios:
    suma = suma + precio

promedio = suma/len(precios)
print('El promedio de precio fue: ' + str(promedio))
print(precios)
minimo = min(precios)
print(minimo)
dia_menor = precios.index(minimo) + 1
print('el dia con medsdsad: ' + str(dia_menor))

dias_mayores = []
for dia in precios:
    if dia > promedio:
        dias_mayores.append(precios.index(dia) + 1)

print(dias_mayores)

