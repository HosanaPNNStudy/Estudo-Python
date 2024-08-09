jogador1 = input("JOGADOR 1 - Digite pedra, papel, tesoura ou sair\n")
jogador2 = input("JOGADOR 2 - Digite pedra, papel, tesoura ou sair \n")

if (jogador1 == "pedra" and jogador2 == "papel"):
    print ("Papel ganha de Pedra")
elif (jogador1 == "pedra" and jogador2 == "tesoura"):
    print ("Pedra ganha de Tesoura")
elif (jogador1 == "pedra" and jogador2 == "pedra"):
    print ("Empate...Jogue novamente!")

        
if (jogador1 == "papel" and jogador2 == "pedra"):
    print ("Papel ganha de Pedra")
elif (jogador1 == "papel" and jogador2 == "tesoura"):
    print ("Tesoura ganha de Papel")
elif (jogador1 == "papel" and jogador2 == "papel"):
    print ("Empate...Jogue novamente!!")

       
if (jogador1 == "tesoura" and jogador2 == "papel"):
    print ("Tesoura ganha de papel")
elif (jogador1 == "tesoura" and jogador2 == "pedra"):
    print ("Pedra ganha de tesoura")
elif (jogador1 == "tesoura" and jogador2 == "tesoura"):
    print ("Empate...Jogue novamente!!")
elif (jogador1 == "sair" or jogador2 == "sair"):
    print("Jogo Finalizado!")
    exit()
        

