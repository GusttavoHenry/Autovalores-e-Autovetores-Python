import numpy as np

# Definindo a matriz A
A = np.array([[4, 2], [1, 3]])

# Calculando os autovalores e autovetores (assumindo que já foram calculados)
autovalores, autovetores = np.linalg.eig(A)

# Verificando a relação Av = λv para cada par de autovalor e autovetor
for i in range(len(autovalores)):
    lambda_i = autovalores[i]
    v_i = autovetores[:, i]  # Acessando o i-ésimo autovetor (coluna)
    
    # Calculando Av e λv
    Av = np.dot(A, v_i)
    lambda_v = lambda_i * v_i
    
    # Comparando os resultados (com uma tolerância para evitar erros numéricos)
    if np.allclose(Av, lambda_v):
        print(f"A relação Av = λv é válida para λ = {lambda_i} e v = {v_i}")
    else:
        print(f"A relação Av = λv NÃO é válida para λ = {lambda_i} e v = {v_i}")
