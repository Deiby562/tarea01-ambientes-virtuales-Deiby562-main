#Importar las librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Crear un cartón de bingo con números aleatorios del 1 al 100
carton = pd.DataFrame(np.random.choice(range(1, 101), (5, 5), replace=False))

#Sorteo de un número aleatorio del 1 al 100
numero = np.random.randint(1, 101)

print("Número sorteado:", numero)

#Marcar el cartón con una "X" si el número sorteado coincide con algún número del cartón
marcado = carton == numero 

#Visualizar el cartón con los números marcados
plt.imshow(marcado.values.astype(int), cmap="Greens")

for i in range(5):
    for j in range(5):
        texto = "X" if marcado.iloc[i, j] else str(carton.iloc[i, j])
        plt.text(j, i, texto, ha='center', va='center')

plt.xticks([])
plt.yticks([])
plt.title("Bingo simple")
plt.show()