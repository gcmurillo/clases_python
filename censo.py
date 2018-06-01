
import numpy as np

n = int(input('Ingrese numero de habitantes: '))
genero = np.zeros(n+1, dtype=int)

'''
quien = 0
while not (quien > n):
    genero[quien] = int(input('Genero[1,2]: '))
    quien = quien + 1
'''

for persona in range(0, len(genero)):
    genero[persona] = int(input('Genero[1,2]: '))

instruccion = np.zeros(n+1, dtype=int)
quien = 0
while not (quien > n):
    instruccion[quien] = int(input('Instruccion[1,2,3]: '))
    quien = quien + 1

quien = 0
print('N - Genero - Instruccion')
while not (quien > n):
    print(str(quien + 1) + '-' + str(genero[quien]) + '-' + str(instruccion[quien]))
    quien = quien + 1