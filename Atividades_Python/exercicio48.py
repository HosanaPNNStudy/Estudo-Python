cadastro = []

for i in range(0,10):
    aux = []
    nome = input('Digite seu nome: ')
    bairro = input('Digite seu bairro: ')

    aux = [nome, bairro]

    cadastro.append(aux)

cadastro.sort()
print(cadastro)