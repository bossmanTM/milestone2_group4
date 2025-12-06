# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #2
# ----------------------------------

from graphics import *
from CMPT103_MS2_Classes_JCES import *
import pickle

'''

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
'''

def detect_click(pt:Point, button:Button):
    """
    Purpose: To return True or False based on whether the user clicked the button
    Parameters: 
        pt: The Point object called "pt"
        rect: The Rectangle object called "rect"
    Return: The boolean True or False
    """      
    rect = button.get_image()[0]
    x, y = pt.getX(), pt.getY()
    p1, p2 = rect.getP1(), rect.getP2()
    x1, x2 = p1.getX(), p2.getX()
    y1, y2 = p1.getY(), p2.getY()
    if (x1 <= x <= x2) and (y1 <= y <= y2):
        return True
    return False

def draw_background(window:GraphWin):
    """
    Purpose: To draw the background elements
    Parameters: The GraphWin object called "window"
    Return: The tuples called "buttons" and "entries"
    """
    buttons = draw_buttons(window)
    entries = draw_entries(window)
    draw_static(window)
    return buttons, entries

def draw_buttons(window:GraphWin):
    """
    Purpose: To draw the background elements
    Parameters: The GraphWin object called "window"
    Return: The tuples called "buttons" and "entries"
    """    
    reset = Button(55, 110, 70, 30, "Reset")
    quit = Button(780, 40, 70, 30, "Quit")
    save = Button(780, 80, 70, 30, "Save")
    load = Button(780, 120, 70, 30, "Load")
    move = Button(300, 525, 100, 30, "Move Disk")
    buttons = (load, move, quit, reset, save)
    for button in buttons:
        button.draw(window)
    return buttons

def draw_entry(window:GraphWin, coords:tuple, width:int):
    """
    Purpose: 
    Parameters: 
    Return: 
    """      
    x_start = coords[0]
    y_start = coords[1]
    entry = Entry(Point(x_start, y_start), width)
    entry.draw(window)
    return entry

def draw_entries(window:GraphWin):
    """
    Purpose: 
    Parameters: 
    Return: 
    """      
    disk_num = draw_entry(window, (430, 40), 2)
    target = draw_entry(window, (430, 75), 2)
    source = draw_entry(window, (157, 540), 2)
    destination = draw_entry(window, (255, 540), 2)
    entries = (disk_num, destination, source, target)
    return entries

def draw_info(game:Hanoi, window:GraphWin):
    """
    Purpose: 
    Parameters: 
    Return: 
    """        
    disks = game.get_max_disks()
    target = game.get_target()
    info = Text(Point(450, 180), f"Disks = {disks}. Target Tower = {target}")    
    info.setSize(18)
    info.setTextColor("green")
    info.draw(window)
    return info

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
        
def main(): # Testing window output
    """
    Purpose: 
    Parameters: 
    Return: 
    """      
    window = GraphWin("Hanoi Towers Game", 900, 600)
    buttons, entries = draw_background(window)
    game = Hanoi(3, 3)
    game.draw_towers("d", window)
    info = draw_info(game, window)
    info = update_info(entries, game, info, window)
    start, end = 1, 3
    next_move = (start, end)
    next_move = update_move(entries, next_move)
    gui = (buttons, entries, info)
    window_operations(game, gui, next_move, window)
    
def redraw_info(game:Hanoi, info:Text, window:GraphWin):
    """
    Purpose: 
    Parameters: 
    Return: 
    """    
    info.undraw()
    return draw_info(game, window)
    
def set_move_info(entries:tuple, original:tuple):
    """
    Purpose: 
    Parameters: 
    Return: 
    """       
    source = entries[2]
    destination = entries[1]
    original = list(original)
    if source.getText() != str(original[0]):
        user_input = source.getText()
        if valid_move_input(user_input):
            original[0] = int(user_input)
        else:
            source.setText(str(original[0]))
    if destination.getText() != str(original[1]):
        user_input = destination.getText()
        if valid_move_input(user_input):
            original[1] = int(user_input)
        else:
            destination.setText(str(original[1]))    
    if original[0] == original[1]:
        return (1, 3)
    return tuple(original)
        
def set_start_info(entry:Entry, name:str, original:int):
    """
    Purpose: 
    Parameters: 
    Return: 
    """             
    if entry.getText() != str(original):
        user_input = entry.getText()
        if valid_start_input(name, user_input):
            original = int(user_input)
        else:
            entry.setText(str(original))
    return original

def update_info(entries:tuple, game:Hanoi, info:Text, window:GraphWin):
    """
    Purpose: 
    Parameters: 
    Return: 
    """            
    disks = set_start_info(entries[0], "disks", game.get_max_disks())
    target = set_start_info(entries[3], "target", game.get_target())
    info = redraw_info(Hanoi(disks, target), info, window)
    game.update_towers(disks, target, window)
    return info

def update_move(entries:tuple, next_move:tuple):
    """
    Purpose: 
    Parameters: 
    Return: 
    """     
    next_move = set_move_info(entries, next_move)   
    return next_move

def valid_move():
    pass

def valid_move_input(user_input:str):
    """
    Purpose: 
    Parameters: 
    Return: 
    """     
    is_digit = user_input.isdigit()
    if is_digit and (1 <= int(user_input) <= 3):
        return True    
    return False

def valid_start_input(to_verify:str, user_input:str):
    """
    Purpose: 
    Parameters: 
    Return: 
    """ 
    is_digit = user_input.isdigit()
    if to_verify == "disks":
        if is_digit and (3 <= int(user_input) <= 5):
            return True
    elif to_verify == "target":
        if is_digit and (2 <= int(user_input) <= 3):
            return True           
    return False

def window_operations(game:Hanoi, gui:tuple, next_move:tuple, window:GraphWin):
    """
    Purpose: 
    Parameters: 
    Return: 
    """     
    buttons, entries, info = gui[0], gui[1], gui[2]
    while True:
        try:
            cursor = window.getMouse()
            if detect_click(cursor, buttons[3]):
                game.update_towers(3, 3, window)
            elif detect_click(cursor, buttons[2]):
                window.close()
                break
            elif detect_click(cursor, buttons[4]):
                print("Saving...")
            elif detect_click(cursor, buttons[0]):
                print("Loading...")
            elif detect_click(cursor, buttons[1]):
                info = update_info(entries, game, info, window)
                next_move = update_move(entries, next_move)
                game.move_disk(next_move[0], next_move[1])             
        except:
            window.close()    
main()