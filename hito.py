import random #Importamos la librería random

numeros = random.sample(range(1, 11), 10) #Generar de forma aleatoria un vector de 10 elementos enteros
print(f'Los numeros antes de la ordenacion es {numeros}') #Mostrar el vector antes de la ordenación.

numeros.sort() #Aplicar el algoritmo de ordenación
print(f'Los números después de la ordenacion son {numeros}') #Mostrar el vector después de la ordenación.