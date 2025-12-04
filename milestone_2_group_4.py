# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #2
# ----------------------------------

from graphics import *
# File to be imported from Downloads must be named "milestone_1_group_4" for the program to function
from milestone_1_group_4 import Tower, Hanoi 
import pickle

# i really wish we were allowed to just use classes properly and i could treat this one specifically like a struct because thats all i actually need from it
# because this class is literally there just so you can oragnize a functions returns an incredible amount easier and you dont have to use a hash map which is
# a cool solution but seen as how this isnt a website backend it is useless to me
# 
# nvm im using a hashmap cause they are sick as hell
# but for the record a class that literally is just used to store 5 values isnt an antipattern and would be the optimal solution here

#i might actually just make my own version without these restrictions cause i just went to refactor the button code and im gonna crash out
# so anyways im using a hash map because they are the most readable form of code i can use without writing a stupid long class for storing 5 data pieces

class Button:
    def __init__(self, start_x:int, width:int, start_y:int, height:int, display:str):
        self._start_x = start_x
        self._start_y = start_y
        self._width = width
        self._height = height
        self._display = display
    
    
    def make_button(self):
        """
        Purpose: To make the button object that will be written to the screen
        Parameters: self: the button to be made
        return: the objects that were made
        """
        objects = []
        objects.append(Rectangle(Point(self._start_x, self._start_y), Point((self._start_x + self._width), (self._start_y + self._height))))
        x_mid = (((self._start_x * 2) + self._width)) // 2
        y_mid = (((self._start_y * 2) + self._height)) // 2
        objects.append(Text(Point(x_mid, y_mid), self._display))
        return objects    


    def is_clicked(self, pt): # this function alone makes me want to turn our buttons into classes
        # i wrote that comment before making this class
        """
        Purpose: To return True or False based on whether the user clicked the button
        Parameters: 
            pt: The that the mouse clicked called "pt"
            rect: The Rectangle object called "rect"
        Return: The boolean True or False ( True if the button was clicked )
        """      
        x, y = pt.getX(), pt.getY()
        # p1, p2 = rect.getP1(), rect.getP2()
        # x1, x2 = p1.getX(), p2.getX()
        # y1, y2 = p1.getY(), p2.getY() just commenting that out cause thats a pretty pretty way to do this
        
        left_x, top_y = self._start_x, self._start_y
        right_x, bottom_y = left_x + self._width, top_y + self._height
        
        if (left_x <= x <= right_x) and (top_y <= y <= bottom_y):
            return True
        return False


class Hanoi_Window: # using another class because classes are ok when you cant use structs
    def __init__(self, default_disk_count = 3, default_destination = 3):
        self._window = GraphWin("Hanoi Towers Game", 900, 600)
        self._default_disk_count = default_disk_count
        self._default_destination = default_destination
        self._game = Hanoi(3, self._default_disk_count, self._default_destination)
        self._to_draw = self.make_static()  # this isnt labeled as one because i really dont wanna make a whole new class for what is essentially a name but this is a stack
        self._entries = self.make_entries()
        self._buttons = self.make_buttons()
        for button in self._buttons:
            self._to_draw += self._buttons[button].make_button()
        self._rings = []
        self.make_towers(self._game)
        # id usually write this in a functional way because side effects could be bad here but to maintain the pattern i think this is nicer
        # SYKE (i changed my mind after restructuring the writing loop)
        
        # am i about to use a third hashmap for this????
        # am i losing my mind?
        # mayhaps
        # actually nvm, theres no need to remember what specifically will be stored so its just being turned into a list
        self._drawn = []
        self._to_undraw = [] # same as this
        self.refresh_window()
        
        
    def make_buttons(self):
        """
        Purpose: draw the buttons
        Parameters: self: the game being handled
        Return: a Hashmap storing all of the buttons
        """
        buttons = {}
        buttons.update({"Reset" : Button(55, 70, 110, 30, "Reset")})
        buttons.update({"Quit" : Button(780, 70, 40, 30, "Quit")})
        buttons.update({"Save" : Button(780, 70, 80, 30, "Save")})
        buttons.update({"Load" : Button(780, 70, 120, 30, "Load")})
        buttons.update({"Move Disk" : Button(300, 100, 525, 30, "Move Disk")})
        return buttons
        
    
    def make_entries(self):
        """
        Purpose: draw the entries
        Parameters: self: the game being handled
        Return: None
        """
        entries = {}
        entries.update({"disk count" : Entry(Point(430, 40), 2)})
        entries.update({"target" : Entry(Point(430, 75), 2)})
        entries.update({"source" : Entry(Point(157, 540), 2)})
        entries.update({"destination" : Entry(Point(255, 540), 2)})
        return entries
        
    def make_static(self):
        """
        Purpose: To generate some of the graphics objects that do not change on the window (we really dont need to keep these but im going to in order to be safe)
        Parameters: The GraphWin object called "window"
        Return: None
        """
        # Initialize and draw the static graphics objects
        objects = []
        objects.append(Text(Point(230, 40), "Number of Disks? (Enter a positive int: 3 by default)"))
        objects.append(Text(Point(219, 75), "Target Tower? (Enter a positive int: 3 by default)"))
        objects.append(Line(Point(50, 450), Point(850, 450)))
        objects.append(Text(Point(97, 540), "From tower?"))
        objects.append(Text(Point(207, 540), "to tower?"))   
        return objects
        
        
    def refresh_window(self):
        """
        Purpose: to refresh the window with the new items(this will happen every frame)(this library is wierd so idk if theres smth implimented already but im used to openGL)
        Parameters: self: the game being handled
        Return: None
        """
        for _ in range(len(self._to_undraw)):
            object = self._to_undraw.pop()
            object.undraw()
            # praying there isnt something i have to do to make sure this get handled by the garbage collecter
            # (trauma from writing C code)
            
        for entry in self._entries:
            if self._entries[entry].canvas is None:
                self._entries[entry].draw(self._window)
        
        for _ in range(len(self._to_draw)):
            object = self._to_draw.pop()
            object.draw(self._window)
            self._drawn.append(object) # if i ever need to actually find these im gonna crash out and turn to_draw and to_undraw into a hash map
        
        for ring in self._rings:
            ring.undraw()
            ring.draw(self._window)
        

    def save_game(self, filename:str):
        """
        Purpose: To save the game
        Parameters: 
            filename: The name to save the game as
            game: The game to save
        Return: None
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self._game, f)
        except OSError:
            print("failed to save the game")
        return 


    def load_game(self, filename:str):
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
            print("failed to open the game")
        if not isinstance(game, Hanoi):
            game = Hanoi(3, self._default_disk_count, self._default_destination)
        self._game = game


    def make_towers(self, game:Hanoi):
        """
        Purpose: To draw the towers on the window
        Parameters: The GraphWin object called "window"
        Return: The tuple of the list called "towers"
        """    
        margins = 50
        tower_width = int((self._window.getWidth()-margins*2)/3)
        tower_height = 200
        tower_bottom = 250
        shaft_width = 5
        # Initialize and draw the towers with spacing in-between
        for tower_num in range(0, 3):
            tower_x = margins + (tower_num * (tower_width))
            self._to_draw += self.make_tower(game.get_tower(tower_num), tower_x, tower_bottom, tower_width, shaft_width, tower_height)

    def make_tower(self, tower:Tower, x:int, y:int, tower_width:int, pole_width:int, height:int) -> list[Rectangle]:
        # this could be a class but it only has to be one function so its not
        """
        Purpose: To return the shape representation of the tower
        Parameters: 
            window: The GraphWin object
            (x, y): The position of the top left corner of the tower
            width: The width of the tower
            height: The height of the tower
        Return: the elements to draw for the tower
        """   
        to_draw = []
        center = x + tower_width/2
        pole = Rectangle(Point((center - pole_width/2), y), Point((center + pole_width/2), y + height))
        pole.setFill("red")
        pole.setOutline("black")
        to_draw.append(pole)
        
        unit_height = height/tower.get_width()
        unit_width = tower_width/tower.get_width()
        for i in range(len(tower)):
            start_point = Point((center - (unit_width/2) * tower.get_disk(i)), y+height - i*unit_height)
            end_point = Point(center + (unit_width/2) * tower.get_disk(i), y+height - (i+1)*unit_height)
            ring = Rectangle(start_point, end_point)
            ring.setFill("blue")
            ring.setOutline("black")
            self._rings.append(ring)
        return to_draw
    
    def handle_clicks(self, cursor):
        if self._buttons["Reset"].is_clicked(cursor):
            print("Resetting...")
            game = Hanoi(3, getIntOrDefault(self._entries["disk count"].getText(), 3), getIntOrDefault(self._entries["target"].getText(), 3))
        elif self._buttons["Quit"].is_clicked(cursor):
            print("Quitting...")
            self._window.close()
            return False
        elif self._buttons["Save"].is_clicked(cursor):
            print("Saving...")
            self.save_game("savefile")
        elif self._buttons["Load"].is_clicked(cursor):
            print("Loading...")
            self.load_game("savefile")
        elif self._buttons["Move Disk"].is_clicked(cursor):
            start = self._entries["source"].getText()
            end = self._entries["destination"].getText()
            print(f"Moving Disk from {start} to {end}...")  
            if start.isnumeric() and end.isnumeric():
                start = int(start)
                end = int(end)
                self._game.transfer(start, end)
                for _ in range(len(self._rings)):
                    ring = self._rings.pop()
                    self._to_undraw.append(ring)
                self.make_towers(self._game)
                if self._game.is_complete():
                    print("you win or smth")
                    self.close()
                    return False
            else:
                print("failed to move disk")
        return True
        
        
    def close(self):
        self._window.close()

def getIntOrDefault(string:str, default:int):
    """
    Purpose: get either an int from the string or a default int if not available
    Parameters:
        string: the string to search
        default: the default int to return
    retunes: either the int in the string or a default
    """
    if string.isnumeric():
        return int(string)
    else:
        return default


def main(): # Testing window output
    game = Hanoi_Window()
    
    while True:
        try:
            cursor = game._window.getMouse()
        except:
            print("failed to get the cursor")
            game.close()
            return
        try: # Currently, clicking any button other than quit then clicking the "x" will cause an infinite loop
            if not game.handle_clicks(cursor):
                print("closing game")
                game.close()
                break
            game.refresh_window()
        except UnboundLocalError:
            print("some error")
            game.close()
            return
main()
