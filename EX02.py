#altere o exercício anterior e mostre na tela, ao final, o nome de cada aluno e sua  respectiva posição no array.

qtd = int(input("Quantos alunos tem na sala? "))
nomes = [0]*qtd
for x in range(qtd):

    nomes[x] = input(f"Digite o nome do aluno: ")
for i in range(qtd):
    print(f'O aluno {nomes[i]} está na posição {i}')