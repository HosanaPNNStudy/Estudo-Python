idade = 18
responsavel = True
nome = "Pereira"
cpf = "444.333.222-11"
endereco = "Sao Goncalo"
taxa = False

print("Ola, " + nome)

if endereco == "Rio de Janeiro":
    print("Eu, " + nome + " portador de CPF " + cpf + ", residente no endereco " + endereco + ", declaro que as informacoes sao verdadeiras")
elif taxa == True:
    print("Eu, " + nome + " portador de CPF " + cpf + ", residente no endereco " + endereco + ", declaro que as informacoes sao verdadeiras")
else:
    print("Para receber seu documento precisar pagar uma taxa de R$50,00")

#if idade >= 18:
#    print("Entra na festa")
#else:
#   if responsavel == True:
#        print("Entrou na festa, pois esta acompanhado do responsavel")
#    else:
#        print("Barrado")       

