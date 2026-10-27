# client/src/game.py

from config import *
from grid import Grid

def display_end_game(winner_list: list | None):
    """Affiche le résultat final de la partie.
        
    Args:
        - winner_list (list | None)
    """
    if not winner_list is None :
        for winner in winner_list:
            symbol, alignment = winner
            print(f'Joueur {symbol} à gagné, -> Alignement : {alignment}')
    else :
        print('Égalité')

def switch_player(current_player: str) -> str :
    """Bascule entre P1 et P2.
        
    Args:
        - current_player (str) : Le symbol du joueur actuelle (voire SYMBOL)

    Returns:
        - (str) : Le symbol du prochain joueur
    """
    if current_player == SYMBOL['P2'] :
        return SYMBOL['P1'] 
    elif current_player == SYMBOL['P1'] :
        return SYMBOL['P2']
    else :
        raise ValueError(f"Symbole de joueur inconnu : {current_player}")

def get_player_move(grid: Grid, player: str) -> tuple[int, int]:
    """Demande au joueur de saisir sa position de jeu et la vérifie.

    Args:

        - grid (Grid) : La grille de jeu
        - player (str) : Le symbole du joueur actuel

    Returns:

        - (tuple[int, int]) : La position (x,y) saisie par le joueur
    """
    while True:
        answer = input(f"Joueur {player}, où veux-tu jouer (x,y) : ")
        formated_answer = answer.split(",")

        # Vérification du format (deux éléments)
        if len(formated_answer) != 2:
            print("Saisie incorrecte : Indiquez deux coordonnées séparées par une virgule (ex: 0,1) !")
            continue

        x_str, y_str = formated_answer[0].strip(), formated_answer[1].strip()

        # Vérification qu'il s'agit de deux nombres entiers
        if not x_str.isdigit() or not y_str.isdigit():
            print("Saisie incorrecte : Il faut deux nombres entiers positifs !")
            continue

        x, y = int(x_str), int(y_str)

        # Vérification de la validité et de la disponibilité de la case
        if x < 0 or x >= grid.size or y < 0 or y >= grid.size:
            print("Saisie incorrecte : Position hors de la grille !")
        elif (x, y) not in grid.get_empty():
            print("Saisie incorrecte : Case déjà occupée !")
        else:
            return (x, y)

def play_turn(grid: Grid, player: str) -> None:
    """Joue un tour pour le joueur actuelle.
    
    Args:
        - grid (Grid) : La grille de jeu
        - player (str) : Le symbol du joueur actuelle
    """
    grid.display()
    x,y = get_player_move(grid, player)
    print(f'Joueur {player} a jouer en {x,y}...')
    grid.set(x,y,player)

def game(grid: Grid) -> None:
    """Lance une partie de morpion.
    
    Args:
        - grid (Grid) : La grille de jeu
    """
    print('..........Morpion..........')

    win = False
    player = SYMBOL['P1']
    running = True

    while running == True :

        play_turn(grid, player)
        winner_list = grid.get_winner()

        if grid.is_full() or not winner_list is None:
            running = False

        player = switch_player(player)

    display_end_game(winner_list)
