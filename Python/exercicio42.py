controle =0
for i in range(0,10):
    # entrada = int(input('Digite um número))
    entrada = input('Digite um número: ')
    numero = int(entrada)

    if numero > 10:
        controle+=1

print('Exitem', controle, 'número(s) maiores que 10')