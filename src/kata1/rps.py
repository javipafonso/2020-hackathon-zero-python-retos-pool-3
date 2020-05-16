from random

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    resultado=""
    if player == 'Piedra' and ai == 'Papel' or player == 'Papel' and ai == 'Piedra':
        resultado = "Perdiste!"
    elif player == ia:
        resultado = "Empate!"        
    elif player == 'Papel' and ai == 'Tijeras' or player == 'Tijeras' and ai == 'Papel':
        resultado = "Perdiste!"
    elif player == 'Piedra'and ai == 'Tijeras':
        resultado = "Ganaste!"
    elif player == 'Papel' and ai == 'Piedra':
        resultado = "Ganaste!"
    elif player == 'Tijeras' and ai == 'Papel':
        resultado = "Ganaste!"
    return resultado
    
# Entry Point
def Game():
    #
    #
    player=input("Eliga una opcion: ")
    indice=random.randint(0, len(options))
    ai=options[indice]
    #
    
    winner = quienGana(player, ai)

    print(winner)
    
Game()

