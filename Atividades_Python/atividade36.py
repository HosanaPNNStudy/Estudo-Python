from random import randint

impar_par = int(input('Digite 0, se você for PAR ou Digite 1, se for IMPAR: '))
usuario= int(input("Digite um número: "))
computador = randint(0, 10)

soma = computador + usuario

if impar_par == 0:
    print('VOCÊ é PAR e jogou:',usuario, 'e o COMPUTADOR é IMPAR e jogou:',computador)
    if soma % 2 ==0 :
        print(soma,'É PAR')
        print('VOCÊ VENCEU!')
    else:
        print(soma,'É IMPAR')
        print('COMPUTADOR VENCEU!')
else:
    print('Você é IMPAR e jogou:',usuario,'e o COMPUTADOR é PAR e jogou:',computador)
    if soma % 2 ==0 :
        print(soma,'É PAR')
        print('O COMPUTADOR VENCEU!')
    else:
        print(soma, 'É IMPAR')
        print('VOCÊ VENCEU!')