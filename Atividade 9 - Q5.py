import numpy as np

# Definindo a matriz B
B = np.array([[5, 1, 0],
              [1, 4, 1],
              [0, 1, 3]])

# Calculando os autovalores e autovetores
autovalores, autovetores = np.linalg.eig(B)

# Imprimindo os resultados
print("Autovalores:")
print(autovalores)
print("\nAutovetores:")
print(autovetores)

