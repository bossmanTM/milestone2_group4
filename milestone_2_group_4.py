# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #2
# ----------------------------------

# from milestone_1_group_4 import Hanoi; temporarily commented so the program can be tested
from graphics import *

def game_loop(game: Hanoi):
    """
    purpose: handle each iteration of the game
    parameters: game: The Hanoi board to be played
    return: None
    """
    window = GraphWin("Towers of Hanoi")
    draw_game(window, game)
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

def load_game(filename: str):
    """
    purpose: load the game using a given filename
    parameters: filename: the name of the savefile to load
    return: a Hanoi object representing either the game with the filename or a new one if it doesnt exist
    """
    pass 

def draw_game(window: GraphWin, game: Hanoi):
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
    Purpose: To draw the background elements; more detailed purpose tba
    Parameters: The GraphWin object called "window"
    Return: The tuple of the list called "towers"
    """
    draw_static(window)
    return draw_towers(window)

def draw_static(window: GraphWin):
    """
    Purpose: To draw some of the graphics objects that do not change on the window
    Parameters: The GraphWin object called "window"
    Return: None
    """
    # Initialize and draw the static graphics objects
    disk = Text(Point(230, 40), "Number of Disks? (Enter a positive int: 3 by default)")
    target = Text(Point(220, 75), "Target Tower? (Enter a positive int: 3 by default)") 
    line = Line(Point(50, 450), Point(850, 450))
    source = Text(Point(100, 540), "From tower?")
    destination = Text(Point(210, 540), "to tower?")   
    static = (disk, destination, line, source, target) 
    for item in static:
        item.draw(window)

def draw_towers(window: GraphWin):
    """
    Purpose: To draw the towers on the window
    Parameters: The GraphWin object called "window"
    Return: The tuple of the list called "towers"
    """    
    # Initialize and draw the towers with spacing in-between
    towers = []
    for tower_num in range(1, 4):
        tower_x = tower_num * 220
        tower = Rectangle(Point(tower_x, 250), Point((tower_x + 5), 450))
        tower.setFill("red")
        tower.setOutline("black")
        towers.append(tower)
        tower.draw(window)    
    return tuple(towers)    

def main(): # Testing window output
    window = GraphWin("Hanoi Towers Game", 900, 600)
    towers = draw_background(window)
    try:
        cursor = window.getMouse()
    except:
        window.close()

main()
