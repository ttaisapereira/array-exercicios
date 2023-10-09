#altere o exercício anterior para permitir  achar o nome de um aluno na lista

qtd = int(input("Quantos alunos tem na sala? "))
nomes = [0]*qtd
for x in range(qtd):

    nomes[x] = input(f"Digite o nome do aluno: ")
nomeNaLista = input("Qual aluno deseja verificar na lista? ")
for i in range(qtd):
    if nomeNaLista == nomes[i]:
        print(f'O aluno {nomeNaLista} está na posição {i}')