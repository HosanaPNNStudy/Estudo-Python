    jogador1 = prompt("JOGADOR 1 - Digite pedra, papel, tesoura ou aperte 1 p/ sair");
    jogador2 = prompt("JOGADOR 2 - Digite pedra, papel, tesoura ou aperte 1 p/ sair");

    if (jogador1 == "pedra") {
        if (jogador2 == "papel") {
            alert ("Papel ganha de Pedra");
        } else if (jogador2 == "tesoura"){
            alert ("Pedra ganha de Tesoura");
        } else if (jogador2 == "pedra") {
            alert ("Empate");
            alert ("Jogue novamente");
        }
    }

    else if (jogador1 == "papel") {
        if (jogador2 == "pedra") {
            alert ("Papel ganha de Pedra");
        } else if (jogador2 == "tesoura"){
            alert ("Tesoura ganha de Papel");
        } else if (jogadoe2 == "papel") {
            alert ("Empate");
            alert ("Jogue novamente");
        }
    }

    else if (jogador1 == "tesoura"){
        if (jogador2 == "papel") {
            alert ("Tesoura ganha de papel");
        }else if (jogador2 == "pedra") {
            alert ("Pedra ganha de tesoura");
        }else if (jogador2 == "tesoura")  {
            alert ("Empate");
            alert ("Jogue novamente");
        }

    }
    else if( sair = 1){
        alert("Obrigada por jogar")
        exit();
    }
