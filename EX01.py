# Perguntar ao usuário quantos alunos tem  na sala e criar um array, unidimensional
# (Vetor) com o nome de todos os alunos da  sala


qtd = int(input("Quantos alunos tem na sala? "))
nomes = [0]*qtd
for x in range (qtd):

    nomes[x] = input(f"Digite o nome do aluno: ")
for i in range (qtd):
    print(nomes[i], end =", ")