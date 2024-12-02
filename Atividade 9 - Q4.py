import numpy as np

# Definindo a matriz
A = np.array([[4, 2],
              [1, 3]])

# Calculando os autovalores
autovalores = np.linalg.eigvals(A)

# Calculando o produto dos autovalores
produto_autovalores = np.prod(autovalores)

# Calculando o determinante
determinante = np.linalg.det(A)

# Comparando os resultados
if produto_autovalores == determinante:
    print("O produto dos autovalores é igual ao determinante da matriz.")
else:
    print("O produto dos autovalores não é igual ao determinante da matriz.")