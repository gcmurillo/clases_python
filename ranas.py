
import random as rd

longuitud_total = 20
rana1 = 0
rana2 = 0
cantidad_rana1 = 0
cantidad_rana2 = 0

while rana1 < 20 and rana2 < 20:
    movimiento_rana1 = rd.random()*3 + 0
    rana1 = rana1 + movimiento_rana1

    movimiento_rana2 = rd.random()*3 + 0
    rana2 = rana2 + movimiento_rana2

    cantidad_rana1 = cantidad_rana1 + 1
    cantidad_rana2 = cantidad_rana2 + 1

    if rana1 >= 20:
        print('rana1 ha llegado')

    if rana2 >= 20:
        print('rana2 ha llegado')

print('movimiento r1: ' + str(cantidad_rana1))

print('movimiento r2: ' + str(cantidad_rana2))


