alunos = []

for i in range(3):
    nome = input('Digite o nome do aluno(a): ')
    media = float(input('Digite a média do aluno(a): '))

    if media >= 0 and media <=10:
        alunos.append((nome, media))
    else:
        print('ERRO! A média tem que está entre 0 e 10')
        

for aluno in alunos:
    print('Nome do Aluno(a):',aluno[0],'Média:',aluno[1])

    