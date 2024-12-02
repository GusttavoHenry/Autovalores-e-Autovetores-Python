import numpy as np

# Definindo a matriz A
A = np.array([[4, 2],[1, 3]])

# Calculando os autovalores e autovetores
autovalores, autovetores = np.linalg.eig(A)

# Imprimindo os resultados
print("Autovalores:")
print(autovalores)

print("\nAutovetores:")
print(autovetores)
