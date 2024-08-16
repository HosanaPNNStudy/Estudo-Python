funcionarios = []

for i in range(0,2):
    nome = input('Digite seu nome: ')
    salario = input('Digite seu salario: ')
    professor = input('Você professor? s ou n: ')
    

    if professor == 's':
        disciplina = input('Escreva a disciplina que leciona: ')
        funcionarios.append('Nome: ', nome , ' Salario: ', salario , ' Disciplina: ' , disciplina + '.\n' )
    else:
        funcionarios.append('Nome: ', nome ,' Salario: ',salario + '.\n' )

print(funcionarios)