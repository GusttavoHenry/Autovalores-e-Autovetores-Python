import numpy as np

# Definindo a matriz A
A = np.array([[4, 2], [1, 3]])

# Calculando os autovalores
autovalores = np.linalg.eigvals(A)

# Calculando o traço da matriz
traco = np.trace(A)

# Somando os autovalores
soma_autovalores = np.sum(autovalores)

# Comparando a soma dos autovalores com o traço
if soma_autovalores == traco:
    print("A soma dos autovalores é igual ao traço da matriz.")
else:
    print("A soma dos autovalores não é igual ao traço da matriz.")