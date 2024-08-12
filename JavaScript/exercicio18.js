    jogador1 = prompt("JOGADOR 1 - Digite pedra, papel, tesoura ou sair\n");
    jogador2 = prompt("JOGADOR 2 - Digite pedra, papel, tesoura ou sair\n");

    if (jogador1 == "pedra" && jogador2 == "papel") {
            alert ("Papel ganha de Pedra");
        } else if (jogador1 ==  "pedra" && jogador2 == "tesoura"){
            alert ("Pedra ganha de Tesoura");
        } else if (jogador1 == "pedra" && jogador2 == "pedra") {
            alert ("Empate...Jogue novamente!");
        }
    
    else if (jogador1 == "papel" && jogador2 == "pedra") {
            alert ("Papel ganha de Pedra");
        } else if (jogador1 == "papel" && jogador2 == "tesoura"){
            alert ("Tesoura ganha de Papel");
        } else if (jogador1 == "papel" && jogador2 == "papel") {
            alert ("Empate...Jogue novamente!");
        }

    else if (jogador1 == "tesoura" && jogador2 == "papel") {
            alert ("Tesoura ganha de papel");
        }else if (jogador1 == "tesoura" && jogador2 == "pedra") {
            alert ("Pedra ganha de tesoura");
        }else if ( Jogador1 == "tesoura" && jogador2 == "tesoura")  {
            alert ("Empate...Jogue novamente!");
        }

    else if( jogador1 == "sair" || jogador2 == "sair"){
        alert("Jogo finalizado!")
        exit();
    }
