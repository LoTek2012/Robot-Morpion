# client/src/grid.py

import random
from config import *

class Grid :
    """Représente une grille carrée de morpion"""

    def __init__(self, size=3):
        """Initialise une grille vide.

        Args:
            size (int, obtional): Taille de la grille (size × size).
                Par défaut à 3.
        """
        self.size = size

        self.grid = []
        for weight in range(self.size):
            line = []
            for height in range(self.size):
                line.append(SYMBOL['empty'])
            self.grid.append(line)
    
    def get(self, x: int, y: int):
        """Récupère le contenu d'une case.

        Args:
            x (int): Index de la colonne (0 à size-1).
            y (int): Index de la ligne (0 à size-1).

        Returns:
            str: Symboles possibles : " " (vide), "O", "X" ou "?".
        """
        return self.grid[y][x]

    def set(self, x: int, y: int, value: str):
        """Modifie le contenu d'une case.

        Args:
            (int): Index de la colonne (0 à size-1) -> x.
            (int): Index de la ligne (0 à size-1) -> y.
            (str): Valeur a écrire dans la grille (valeurs possibles : Voire SYMBOL dans config.py).
        """
        self.grid[y][x] = value

    def reset(self):
        """Réinitialise la grille en la vidant entièrement."""
        self.grid = []
        for weight in range(self.size):
            line = []
            for height in range(self.size):
                line.append(SYMBOL['empty'])
            self.grid.append(line)

    def get_empty(self):
        """Récupère toutes les cases encore libres.

        Returns:
            list[tuple[int, int]]: Liste des coordonnées (x, y) des cases vides.
        """
        empty = []

        for y, line in enumerate(self.grid) :
            for x, case in enumerate(line) :
                if case == SYMBOL["empty"] :
                    empty.append((x,y))

        return empty

    def display(self):
        """Affiche la grille dans la console avec des separateurs verticaux est horizontaux."""

        separator = []
        formated_lines = []

        for i in range(self.size):
            separator.append("---")

        separator = "+".join(separator) # fusionner les éléments d'une liste en un seul str avec un separateur

        for line in self.grid :
            formated_lines.append(" | ".join(line))

        for line_index, line in enumerate(formated_lines) :
            formated_lines[line_index] = f'{line_index}' + ' ' + line + ' '

        heading = []
        for column_index, case in enumerate(self.grid[0]):
            heading.append(f'{column_index}')

        formated_heading = '  ' + ("   ".join(heading)) + '\n'
        
        formated_grid = formated_heading + (f"\n {separator}\n".join(formated_lines))
         
        print('\nGrille Actuelle :')
        print(f'\n{formated_grid}\n')
            
    def set_random(self, set_empty: bool=False):
        """Remplit aléatoirement chaque case de la grille avec des symboles (Voire SYMBOL dans config.py).
        
        Args:
            - set_empty (bool, obtional) : Defini si la grille peut être remplie avec des cases vides.
        """ 

        self.reset()

        for y, line in enumerate(self.grid) :
            for x, case in enumerate(line) :

                if set_empty == True :
                    rand = random.randint(0, 2)
                elif set_empty == False :
                    rand = random.randint(1, 2)
                else :
                    raise ValueError 

                if rand == 0 :
                    value = ' '
                elif rand == 1 :
                    value = 'O'
                elif rand == 2 :
                    value = 'X'
        
                self.set(x,y,value)

    def get_winner(self):
        """Détermine l'alignement gagnant son symbole.

        Returns:
            - (list[str,tuple[int, int]] | None) : Une list contenant des tuples qui contiennent le symbol des gagnant et les coordonnées (x, y) de leurs lignes, colonnes ou diagonales, ou None si il n'y a pas de gagant.
        """
        tmp_alignments_list = []

        for y, line in enumerate(self.grid) :
            for x, case in enumerate(line) :
                    
                if x == 0 and y == 0:
                    # Diagonal 0
                    tmp_alignments_list.append(self.get_alignment(x,y,1,1))
                    # Ligne 0
                    tmp_alignments_list.append(self.get_alignment(x,y,1, 0))

                elif x == self.size-1 and y == 0 :
                    # Diagonal 1
                    tmp_alignments_list.append(self.get_alignment(x,y,-1,1))
                    # Dernière colonne
                    tmp_alignments_list.append(self.get_alignment(x,y,0,1))

                elif x == 0 :
                    # Autres lignes
                    tmp_alignments_list.append(self.get_alignment(x,y,1,0))

                elif y == 0 :
                    # Autres colonnes
                    tmp_alignments_list.append(self.get_alignment(x,y,0,1))

        winner = []

        for tmp_alignment in tmp_alignments_list :
            symbols = []
            for case in tmp_alignment :
                
                x,y = case
                symbols.append(self.get(x,y))

            is_winning_line = all(symbol == symbols[0] for symbol in symbols) and not any(symbol == SYMBOL['empty'] for symbol in symbols) # all() Verifi si tout les symbol de symbols sont égales a symbols[0] la commande any elle a besoin de que un True pour return True 
            if is_winning_line : 
                winner.append((symbols[0], tmp_alignment))

        if winner == []:
            return None
        else:
            return winner

    def get_alignment(self, x: int, y: int, x_add: int, y_add: int):
        """Trouve un alignement possible a partir de coordonnée de depart (x,y) et d'un décalage (x_add, y_add) positif ou négatif.

        Args:
            - x (int) : Coordonnées x de la case de depart
            - y (int) : Coordonnées y de la case de depart
            - x_add (int) : Decalage sur l'axe x par rapport a la case de depart pout trouver a chaque fois la prochaine case de l'alignement
            - y_add (int) : Decalage sur l'axe y par rapport a la case de depart pout trouver a chaque fois la prochaine case de l'alignement

        Returns:
            - (list[tuple[int,int]]) : List des coordonnéés (x,y) de chaques cases de l'alignement
        """
        alignment = []
        x_tmp = x
        y_tmp = y
        for i in range(self.size):
            alignment.append((x_tmp, y_tmp))
            x_tmp = x_tmp + x_add
            y_tmp = y_tmp + y_add

        return alignment

    def is_full(self): # Ne marche pas !!!
        """Detecte si la grille est pleine.

        Returns:
            - (bool): True si la grille est pleine, sinon False
        """
        if any((case == SYMBOL["empty"] for case in line) for line in self.grid) :
            return False
        else:
            return True

    def get_list_case(self):
        """Retourne la liste de toutes les cases de la grille avec leurs coordonnées.

        Returns :
            - cases (list[tuple[int,int]]) : Liste de tuples contenant les coordonnées (x,y) de chaques cases de la grille
        """
        cases = []

        for y, line in enumerate(self.grid):
            for x, case in enumerate(line):
                cases.append((x,y))

        return cases

def debug():
    """Teste la classe Grid"""
    test_grid = Grid(3)
    print(f'Grille pleine : {test_grid.is_full()}')
    test_grid.set_random(set_empty=False)
    test_grid.display()
    print(f'Grille pleine : {test_grid.is_full()}')
    winner_list = test_grid.get_winner()

    if winner_list == None:
        print('Pas de gagnant')
    else:
        for winner in winner_list:
            symbol, alignment = winner
            print(f'Gagant : {symbol}, -> Alignement : {alignment}')
