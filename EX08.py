# Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e
# mostrando seu nome e a mensagem, login efetuado com sucesso


for x in range(1):
    nome = input("Digite o nome do usuários: ")
    senha = input("Digite a senha do usuários: ")

loginNome=input('Digite seu usuário: ')
loginSenha=input('Digite sua senha: ')

if loginNome != nome:
    print("Erro no seu login!")
elif loginSenha != senha:
    print("Erro no seu login!")
else:
    print(f'{nome}, login efetuado com sucesso!')