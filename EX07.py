# Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array
# diferente, após completar a digitação, imprimir, nome, senha e posição dos dados no array

nomes = []
senhas = []
for x in range(5):
    nome = input("Digite o nome dos usuários: ")
    senha = input("Digite a senha dos usuários: ")
    nomes = nomes + [nome]
    senhas = senhas + [senha]
for i in range(5):
    print(f'Nome {nomes[i]}, senha {senhas[i]}, posição {i}')