# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #2
# ----------------------------------

# from milestone_1_group_4 import Hanoi; temporarily commented so the program can be tested
from graphics import *
from milestone_1_group_4 import Tower, Hanoi

def game_loop(game): # Removed Hanoi type hint temporarily
    """
    Purpose: Handle each iteration of the game
    Parameters: game: The Hanoi board to be played
    Return: None
    """
    window = GraphWin("Towers of Hanoi")
    draw_game(window, game)
    draw_background(window)
    pass

def save_game(filename: str, game): # Removed Hanoi type hint temporarily
    """
    Purpose: To save the game
    Parameters: 
        filename: The name to save the game as
        game: The game to save
    Return: None
    """
    pass

def load_game(filename: str):
    """
    Purpose: To load the game using a given filename
    Parameters: filename: The name of the savefile to load
    Return: A Hanoi object representing either the game with the filename or a new one if it doesnt exist
    """
    pass 

def draw_game(window: GraphWin, game): # Removed Hanoi type hint temporarily
    """
    Purpose: To draw the game onto screen
    Parameters: 
        window: The window to be edited
        game: The Hanoi board to be drawn
    Return: None
    """
    return

def draw_background(window: GraphWin):
    """
    Purpose: To draw the background elements; more detailed purpose tba
    Parameters: The GraphWin object called "window"
    Return: The tuple of the list called "towers"
    """
    draw_static(window)
    return

def draw_static(window: GraphWin):
    """
    Purpose: To draw some of the graphics objects that do not change on the window
    Parameters: The GraphWin object called "window"
    Return: None
    """
    # Initialize and draw the static graphics objects
    disk = Text(Point(230, 40), "Number of Disks? (Enter a positive int: 3 by default)")
    target = Text(Point(219, 75), "Target Tower? (Enter a positive int: 3 by default)") 
    line = Line(Point(50, 450), Point(850, 450))
    source = Text(Point(97, 540), "From tower?")
    destination = Text(Point(207, 540), "to tower?")   
    static = (disk, destination, line, source, target) 
    for item in static:
        item.draw(window)

def draw_towers(window: GraphWin, game: Hanoi):
    """
    Purpose: To draw the towers on the window
    Parameters: The GraphWin object called "window"
    Return: The tuple of the list called "towers"
    """    
    margins = 50
    tower_width = ((window.getWidth()-margins*2)/3)
    tower_height = 200
    tower_bottom = 250
    shaft_width = 5
    # Initialize and draw the towers with spacing in-between
    towers = []
    for tower_num in range(0, 3):
        tower_x = margins + (tower_num * (tower_width))
        tower = make_tower(window, game.get_tower(tower_num), tower_x, tower_bottom, tower_width, shaft_width, tower_height)
        tower[0].setFill("red")
        tower[0].setOutline("black")
        for ring in tower[1]:
            ring.setFill("blue")
            ring.setOutline("black")
            ring.draw(window)
        towers.append(tower)
        tower[0].draw(window)    
    return tuple(towers)    

def make_tower(window:GraphWin, tower:Tower, x, y, tower_width, pole_width, height):
    """
    Purpose: return the shape representation of the tower
    Parameters: 
        window: The GraphWin object
        (x, y): the position of the top left corner of the tower
        width: the width of the tower
        height: the height of the tower
    Return: a tuple storing the tower and a list of its rings
    """   
    center = x + tower_width/2
    pole = Rectangle(Point((center - pole_width/2), y), Point((center + pole_width/2), y + height))
    rings = []
    unit_height = height/tower.get_width()
    unit_width = tower_width/tower.get_width()
    for i in range(len(tower)):
        rings.append(Rectangle(Point((center - (unit_width/2) * tower.get_disk(i)), y+height - i*unit_height), Point(center + (unit_width/2) * tower.get_disk(i), y+height - (i+1)*unit_height)))
    return (pole, rings)

def main(): # Testing window output
    window = GraphWin("Hanoi Towers Game", 900, 600)
    draw_background(window)
    towers = draw_towers(window, Hanoi(3, 10, 2))
    try:
        cursor = window.getMouse()
    except:
        window.close()

main()
