numeros = []
for i in range(0,8):
    entrada = int(input('Digite um número: '))
    numeros.append(entrada)
        
    maior = max (numeros)
    menor = min (numeros)

print('Maior numero é:',maior)
print('Menor numero é:',menor)
