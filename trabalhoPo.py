from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Dados do problema
oferta = [100, 150, 200]  # Oferta de fornecedores
demanda = [120, 80, 170]  # Demanda de destinos

# Matriz de custo
custo = [[4, 6, 8],
         [3, 5, 7],
         [2, 4, 6]]

# Número de fornecedores e destinos
num_fornecedores = len(oferta)
num_destinos = len(demanda)

# Criando o problema de programação linear
problema = LpProblem(name="Problema_Transporte", sense=LpMaximize)

# Criando as variáveis de decisão
x = [[LpVariable(name=f"x_{i}_{j}", lowBound=0) for j in range(num_destinos)] for i in range(num_fornecedores)]

# Adicionando a função objetivo
problema += lpSum(custo[i][j] * x[i][j] for i in range(num_fornecedores) for j in range(num_destinos)), "Custo_Total"

# Adicionando as restrições de oferta
for i in range(num_fornecedores):
    problema += lpSum(x[i][j] for j in range(num_destinos)) <= oferta[i], f"Restricao_Oferta_{i}"

# Adicionando as restrições de demanda
for j in range(num_destinos):
    problema += lpSum(x[i][j] for i in range(num_fornecedores)) == demanda[j], f"Restricao_Demanda_{j}"

# Resolvendo o problema
problema.solve()

# Verificando se a otimização foi bem-sucedida
if problema.status == 1:
    # Extraindo e exibindo os resultados
    solucao = [[x[i][j].varValue for j in range(num_destinos)] for i in range(num_fornecedores)]

    print("Matriz de transporte:")
    for linha in solucao:
        print(linha)

    print("\nCusto máximo:", problema.objective.value())
else:
    print("A otimização não foi bem-sucedida. Status do problema:", problema.status)
