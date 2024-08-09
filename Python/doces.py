doces = []

doces.append('Pudim')
doces.append('Brigadeiro')
doces.append('Pave')
doces.append('Quindim')
doces.append('Torta de Limao')

print('Imprimindo a Lista')
print(doces)
# for doce in doces:
#     print(doce)
doces.insert(3, 'Cajuzinho')

for doce in doces:
    print(doce)