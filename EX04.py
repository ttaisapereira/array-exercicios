# Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor,
# Calcular a média da  turma e contar quantos alunos obtiveram  nota acima desta média calculada
# Escrever a média da turma e o resultado  da contagem

notas = [0]*5
cont = 0
soma = 0

for x in range(5):
    notas[x]= float(input("Digite a nota dos alunos: "))
for y in range(5):
    soma+=notas[y]

media = soma/5
for z in range(5):
    if notas[z] > media:
        cont+=1
print(f'A média da sala é {media} e {cont} obtiveram notas acima da média')