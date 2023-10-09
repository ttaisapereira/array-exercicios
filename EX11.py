#Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
# Após exibir essa lista, o programa deve mostrar também os nomes na ordem
# inversa em que o usuário os digitou, um por linha.

nomes = []
for x in range(5):
    nome = input("Digite o nome: ")
    nomes = nomes + [nome]
for i in range(4, -1, -1):
    print(nomes[i])