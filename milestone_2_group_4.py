from milestone_1_group_4 import Hanoi 
from graphics import GraphWin

def game_loop(game:Hanoi):
    """
    purpose: handle each iteration of the game
    parameters: game: The Hanoi board to be played
    return: None
    """
    window = GraphWin("Towers of Hanoi")
    draw_Game(window, game)
    draw_background(window)
    pass

def save_game(filename: str, game: Hanoi):
    """
    purpose: save the game
    parameters: 
        filename: the name to save the game as
        game: the game to save
    return: None
    """
    pass

def load_game(filename:str):
    """
    purpose: load the game using a given filename
    parameters: filename: the name of the savefile to load
    return: a Hanoi object representing either the game with the filename or a new one if it doesnt exist
    """
    pass 

def draw_Game(window:GraphWin, game: Hanoi):
    """
    purpose: draw the game onto screen
    parameters: 
        window: the window to be edited
        game: The Hanoi board to be drawn
    return: None
    """
    
    return

def draw_background(window: GraphWin):
    """
    purpose: draw the background of the game
    parameters: window: the window to be edited
    return: None
    """
    
    return 

def main():
    pass
