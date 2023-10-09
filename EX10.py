# Faça um código para ler um vetor de 30 números. Após isto, ler mais um número
# qualquer, calcular e escrever quantas vezes esse número aparece no vetor.


vetor = []
for x in range(30):
    numero = int(input("Digite um número: "))
    vetor += [numero]

numPesquisa = int(input("Digite o número a ser pesquisado: "))

cont = 0
for i in vetor:
    if i == numPesquisa:
        cont += 1
print(f"O número {numPesquisa} aparece {cont} vezes no vetor.")