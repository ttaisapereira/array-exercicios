#Faça um código para ler 5 números e  armazenar em um vetor. Após a leitura
# total dos 5 números, o código deve  escrever esses 5 números lidos na ordem inversa


num = []
for x in range(5):
    numero = int(input("Digite um número: "))
    num = num + [numero]
for i in range(4, -1, -1):
    print(num[i])