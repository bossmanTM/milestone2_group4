# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #2
# ----------------------------------

from graphics import *
from CMPT103_MS2_Classes_JCES import *
import pickle

def announce(string:str, text:Text, window:GraphWin):
    """
    Purpose: To draw the red text on the screen for errors or saving/loading
    Parameters: 
        string: The string called "string" to be written
        text: The Text object called "text"
        window: The GraphWin object called "window"
    Return: The boolean True or False
    """      
    if text != None:
        text.undraw()
    text = Text(Point(450, 495), string)
    text.setSize(10)
    text.setTextColor("red")
    text.draw(window)  
    return text

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
    Purpose: To draw the buttons
    Parameters: The GraphWin object called "window"
    Return: The tuple called "buttons"
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
    Purpose: To draw an entry
    Parameters: 
        window: The GraphWin object called "window"
        coords: The tuple called "coords"
        width: The integer called "width"
    Return: The Entry object called "entry"
    """      
    x_start = coords[0]
    y_start = coords[1]
    entry = Entry(Point(x_start, y_start), width)
    entry.draw(window)
    return entry

def draw_entries(window:GraphWin):
    """
    Purpose: To draw the entries onto the screen
    Parameters: The GraphWin object called "window"
    Return: The tuple called "entries"
    """      
    disk_num = draw_entry(window, (430, 40), 2)
    target = draw_entry(window, (430, 75), 2)
    source = draw_entry(window, (157, 540), 2)
    destination = draw_entry(window, (255, 540), 2)
    entries = (destination, disk_num, source, target)
    return entries

def draw_header(game:Hanoi, window:GraphWin):
    """
    Purpose: To draw the green header onto the screen
    Parameters:
        game: The Hanoi object called "game"
        window: The GraphWin object called "window"
    Return: The Text object called "header"
    """        
    disks = game.get_max_disks()
    target = game.get_target()
    header = Text(Point(450, 180), f"Disks = {disks}. Target Tower = {target}")
    header.setSize(18)
    if game.get_win():
        steps = game.get_steps()
        win_message = f"Congratulations! All disks have been moved to tower {target} in {steps} steps."
        header = Text(Point(450, 180), win_message)
        header.setSize(20)
    header.setTextColor("green")
    header.draw(window)
    return header

def draw_static(window:GraphWin):
    """
    Purpose: To draw some of the graphics objects that do not change on the window
    Parameters: The GraphWin object called "window"
    Return: None
    """
    disk = Text(Point(230, 40), "Number of Disks? (Enter a positive int: 3 by default)")
    target = Text(Point(219, 75), "Target Tower? (Enter a positive int: 3 by default)") 
    line = Line(Point(50, 450), Point(850, 450))
    source = Text(Point(97, 540), "From tower?")
    destination = Text(Point(207, 540), "to tower?")   
    static = (destination, disk, line, source, target) 
    for item in static:
        item.draw(window)

def load_game():
    """
    Purpose: To load the game using game.p
    Parameters: None
    Return: The list called "move_history" or None
    """
    move_history = None
    try:
        with open("game.p", "rb") as f:
            move_history = pickle.load(f)
    except:
        return
    return move_history
        
def main():
    """
    Purpose: To start the game by initializing and drawing the necessary elements
    Parameters: None
    Return: None
    """      
    window = GraphWin("Hanoi Towers Game", 900, 600)
    hanoi_game = new_game(window)
    hanoi_game[0][0].draw_towers("d", window)
    window_operations(hanoi_game, window)
    
def make_move(hanoi_game:list, text:Text, window:GraphWin):
    """
    Purpose: To move the disk on the screen to its correct location
    Parameters: 
        hanoi_game: The list called "hanoi_game"
        text: The Text object called "text"
        window: The GraphWin object called "window"
    Return: A Text object if there is an error in moving the disk
    """       
    update_info(hanoi_game, False, window)
    destination, source = hanoi_game[0][1][0], hanoi_game[0][1][2]
    message = hanoi_game[0][0].move_disk(destination, source)
    if hanoi_game[0][0].get_win() == True:
        hanoi_game[1][2].undraw()
        hanoi_game[1][2] = draw_header(hanoi_game[0][0], window)  
    if message != None and len(message) > 0:
        return announce(message, text, window)    
    
def new_game(window:GraphWin):
    """
    Purpose: To start a new game and draw the necessary elements on the screen
    Parameters: The GraphWin object called "window"
    Return: The list called "hanoi_game"
    """      
    reset_screen(window)
    buttons, entries = draw_background(window)
    destination, disk_num, source, target = 3, 3, 1, 3
    info = [destination, disk_num, source, target]
    set_entries(entries, info)
    game = Hanoi(disk_num, target)
    header = draw_header(game, window)   
    content, gui = [game, info], [buttons, entries, header]
    hanoi_game = [content, gui]
    return hanoi_game

def pressed_load(hanoi_game:list, move_history:list, red_text:Text, window:GraphWin):
    """
    Purpose: To load the game when the user presses the load button
    Parameters: 
        hanoi_game: The list called "hanoi_game"
        move_history: The list called "move_history"
        red_text: The Text object called "red_text"
        window: The GraphWin object called "window"
    Return: None
    """         
    if load_game() != None:
        move_history = load_game()
        for move in range(len(move_history)):
            for stat in range(4):
                hanoi_game[1][1][stat].setText(move_history[move][stat])         
            make_move(hanoi_game, red_text, window) 

def reset_screen(window:GraphWin):
    """
    Purpose: To clear all elements on the screen
    Parameters: The GraphWin object called "window" 
    Return: None
    """      
    for graphic in window.items.copy():
        graphic.undraw()
        
def save_game(move_history:list):
    """
    Purpose: To save the game
    Parameters: The list called "move_history" to save
    Return: None
    """
    try:
        with open("game.p", "wb") as f:
            pickle.dump(move_history, f)
    except:
        return False
    return True 
    
def set_entries(entries:list, values:list):
    """
    Purpose: To set the values of every entry
    Parameters: 
        entries: The list called "entries"
        values: The list called "values"
    Return: None
    """        
    for index in range(len(entries)):
        entries[index].setText(str(values[index]))
        
def update_info(hanoi_game:list, is_reset:bool, window:GraphWin):
    """
    Purpose: To update or reset the information on the screen
    Parameters: 
        hanoi_game: The list called "hanoi_game"
        is_reset: The boolean called "is_reset" (determines if information should be reset)
        window: The GraphWin object called "window"
    Return: None
    """
    hanoi_game[1][2].undraw() 
    default = (3, 3, 1, 3)
    orig_disk_num = hanoi_game[0][1][1]
    orig_target = hanoi_game[0][1][3]
    names = ["destination", "disk_num", "source", "target"]
    for entry in range(len(hanoi_game[1][1])):
        test_entry = hanoi_game[1][1][entry]
        is_valid = valid_entry(test_entry, names[entry])
        test_entry.setFill("gray")
        if is_valid and is_reset != True:
            pass
        else:
            if is_valid == False:
                test_entry.setFill("yellow")
            test_entry.setText(default[entry])
        hanoi_game[0][1][entry] = int(test_entry.getText())
    disk_num, target = hanoi_game[0][1][1], hanoi_game[0][1][3]  
    if orig_disk_num != disk_num or orig_target != target or is_reset:
        hanoi_game[0][0].draw_towers("ud", window) 
        hanoi_game[0][0] = Hanoi(disk_num, target)
        hanoi_game[0][0].draw_towers("d", window)
    hanoi_game[1][2] = draw_header(hanoi_game[0][0], window)

def valid_entry(entry:Entry, name:str):
    """
    Purpose: To check if the input in the entry is an integer within a specified range
    Parameters: 
        entry: The Entry object called "entry"
        name: The string called "name" (name of the variable)    
    Return: The boolean True or False
    """     
    if entry.getText().isdigit() == False:
        return False
    value = int(entry.getText())
    if name == "destination":
        return (1 <= value <= 3)
    elif name == "disk_num":
        return (3 <= value <= 5)
    elif name == "source":
        return (1 <= value <= 3)
    elif name == "target":
        return (2 <= value <= 3)
    else:
        return False

def window_operations(hanoi_game:list, window:GraphWin):
    """
    Purpose: To allow the buttons in the window to function
    Parameters: 
        hanoi_game: The list called "hanoi_game"
        window: The GraphWin object called "window"
    Return: None
    """     
    buttons, move_history, red_text = hanoi_game[1][0], [], None 
    while True:
        try:
            cursor = window.getMouse()
            if detect_click(cursor, buttons[3]):
                red_text = announce("", red_text, window)
                update_info(hanoi_game, True, window)
            elif detect_click(cursor, buttons[2]):
                window.close()
                break
            elif detect_click(cursor, buttons[4]):          
                save_game(move_history)
                red_text = announce("Game saved.", red_text, window)
            elif detect_click(cursor, buttons[0]):
                pressed_load(hanoi_game, move_history, red_text, window)
                red_text = announce("Game loaded.", red_text, window)
            elif detect_click(cursor, buttons[1]):
                red_text = announce("", red_text, window)
                if hanoi_game[0][0].get_win() == False:
                    red_text = make_move(hanoi_game, red_text, window)
                    entry_texts = []
                    for entry in range(4):
                        entry_texts.append(hanoi_game[1][1][entry].getText())
                    move_history.append(entry_texts) 
        except:
            window.close()
main()
