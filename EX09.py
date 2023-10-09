#Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois
#vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos
#elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.

n = int(input("Digite o tamanho do vetor: "))
a = [0]*n
b = [0]*n
for x in range(n):
    a[x] = int(input(f'Digite o valor de A: '))
for i in range(n):
    b[i] = int(input(f'Digite o valor de B: '))

soma = [''] * n
for y in range(n):
    soma[y] = a[y] + b[y]

print(f'A soma dos valores de A e B são: {soma}')