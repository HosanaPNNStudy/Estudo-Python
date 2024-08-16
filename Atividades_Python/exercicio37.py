nome = input('Digite seu nome: ')
cidade = input('Digite sua cidade: ')

def informacao(nome, cidade):
    if cidade == 'Rio de Janeiro':
        print(nome,', Seja Bem-Vindo à Cidade Maravilhosa!')
    else:
        print(nome,', da Cidade de',cidade)

informacao(nome, cidade)