# Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar em
# uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo
# valor X. Logo após, imprimir o vetor M


a = []
m = []
for i in range(10):
    num = int(input("Digite os número que serão multiplicados: "))
    a += [num]

x = int(input("Digite o valor multiplicador: "))

m = [num * x for num in a]

print(f'multiplicador {x}')
print(f'Números que foram multiplicados: {a}')
print(f'Resultados: {m}')