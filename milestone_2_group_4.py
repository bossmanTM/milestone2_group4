# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #2
# ----------------------------------

from graphics import *
# File to be imported from Downloads must be named "milestone_1_group_4" for the program to function
from milestone_1_group_4 import Tower, Hanoi 
import pickle

def game_loop(game:Hanoi):
    """
    Purpose: Handle each iteration of the game
    Parameters: game: The Hanoi board to be played
    Return: None
    """
    pass

def save_game(filename:str, game:Hanoi):
    """
    Purpose: To save the game
    Parameters: 
        filename: The name to save the game as
        game: The game to save
    Return: None
    """
    try:
        with open(filename, "wb") as f:
            pickle.dump(game, f)
    except OSError:
        return False
    return True 

def load_game(filename:str):
    """
    Purpose: To load the game using a given filename
    Parameters: filename: The name of the savefile to load
    Return: A Hanoi object representing either the game with the filename or a new one if it doesnt exist
    """
    game = None
    try:
        with open(filename, "rb") as f:
            game = pickle.load(f)
    except:
        return 
    return game

def draw_background(window: GraphWin):
    """
    Purpose: To draw the background elements
    Parameters: The GraphWin object called "window"
    Return: The tuples called "buttons" and "entries"
    """
    draw_static(window)
    reset = draw_button(window, 55, 70, 110, 30, "Reset")
    quit = draw_button(window, 780, 70, 40, 30, "Quit")
    save = draw_button(window, 780, 70, 80, 30, "Save")
    load = draw_button(window, 780, 70, 120, 30, "Load")
    move = draw_button(window, 300, 100, 525, 30, "Move Disk") 
    buttons = (load, move, quit, reset, save)
    
    disk_num = draw_entry(window, 430, 40, 2)
    target = draw_entry(window, 430, 75, 2)
    source = draw_entry(window, 157, 540, 2)
    destination = draw_entry(window, 255, 540, 2)
    entries = {"disk_num": disk_num, "destination": destination, "source": source, "target":target}
    return buttons, entries
    
def draw_button(window:GraphWin, start_x:int, w:int, start_y:int, h:int, display:str):
    rect = Rectangle(Point(start_x, start_y), Point((start_x + w), (start_y + h)))
    rect.draw(window)
    x_mid = (((start_x * 2) + w)) // 2
    y_mid = (((start_y * 2) + h)) // 2
    text = Text(Point(x_mid, y_mid), display)
    text.draw(window)
    return rect    

def draw_entry(window:GraphWin, start_x:int, start_y:int, w:int):
    entry = Entry(Point(start_x, start_y), w)
    entry.draw(window)
    return entry

def draw_static(window:GraphWin):
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

def draw_towers(window:GraphWin, game:Hanoi):
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
        tower = make_tower(game.get_tower(tower_num), tower_x, tower_bottom, tower_width, shaft_width, tower_height)
        tower[0].setFill("red")
        tower[0].setOutline("black")
        for ring in tower[1]:
            ring.setFill("blue")
            ring.setOutline("black")
            ring.draw(window)
            
        towers.append(tower)
        tower[0].draw(window)    
    return towers    

def is_clicked(pt, rect):
    """
    Purpose: To return True or False based on whether the user clicked the button
    Parameters: 
        pt: The Point object called "pt"
        rect: The Rectangle object called "rect"
    Return: The boolean True or False
    """      
    x, y = pt.getX(), pt.getY()
    p1, p2 = rect.getP1(), rect.getP2()
    x1, x2 = p1.getX(), p2.getX()
    y1, y2 = p1.getY(), p2.getY()
    if (x1 <= x <= x2) and (y1 <= y <= y2):
        return True
    return False

def make_tower(tower:Tower, x:int, y:int, tower_width:int, pole_width:int, height:int):
    """
    Purpose: To return the shape representation of the tower
    Parameters: 
        window: The GraphWin object
        (x, y): The position of the top left corner of the tower
        width: The width of the tower
        height: The height of the tower
    Return: A tuple storing the tower and a list of its rings
    """   
    rings = []
    center = x + tower_width/2
    pole = Rectangle(Point((center - pole_width/2), y), Point((center + pole_width/2), y + height))
    unit_height = height/tower.get_width()
    unit_width = tower_width/tower.get_width()
    for i in range(len(tower)):
        start_point = Point((center - (unit_width/2) * tower.get_disk(i)), y+height - i*unit_height)
        end_point = Point(center + (unit_width/2) * tower.get_disk(i), y+height - (i+1)*unit_height)
        rings.append(Rectangle(start_point, end_point))
    return (pole, rings)

def getIntOrDefault(string:str, default:int):
    """
    Purpose: get either an int from the string or a default int if not available
    Parameters:
        string: the string to search
        default: the default int to return
    retunes: either the int in the string or a default
    """
    if string.isnumeric():
        print("test")
        return int(string)
    else:
        return default

def main(): # Testing window output
    window = GraphWin("Hanoi Towers Game", 900, 600)
    buttons, entries = draw_background(window)
    disks = 3
    game = Hanoi(3, disks, 3)
    towers = draw_towers(window, game)
    while True:
        try:
            cursor = window.getMouse()
        except:
            window.close()
        try: # Currently, clicking any button other than quit then clicking the "x" will cause an infinite loop
            if is_clicked(cursor, buttons[3]):
                print("Resetting...")
                game = Hanoi(3, getIntOrDefault(entries["disk_num"].getText(), 3), getIntOrDefault(entries["target"].getText(), 3))
            elif is_clicked(cursor, buttons[2]):
                print("Quitting...")
                window.close()
                break
            elif is_clicked(cursor, buttons[4]):
                print("Saving...")
                save_game("savefile",game)
            elif is_clicked(cursor, buttons[0]):
                print("Loading...")
                loaded_game = load_game("savefile")
                if loaded_game is None:
                    game = Hanoi(3, disks, 2)
                else:
                    game = loaded_game
            elif is_clicked(cursor, buttons[1]):
                print(f"Moving Disk from {entries["source"].getText()} to {entries["destination"].getText()}...")  
                start = entries["source"].getText()
                end = entries["destination"].getText()
                if start.isnumeric() and end.isnumeric():
                    start = int(start)
                    end = int(end)
                    game.transfer(start, end)
                    print(game)
                else:
                    print("failed to move disk")
            for tower in towers: # prolly not ideal method
                for ring in tower[1]:
                    ring.undraw()
                window.delItem(tower[0])
            towers = draw_towers(window, game)
        except UnboundLocalError:
            window.close()
main()
