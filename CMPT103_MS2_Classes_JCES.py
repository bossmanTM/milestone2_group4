# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #2
# ----------------------------------

from graphics import GraphWin, Rectangle, Text, Point, Entry, Line 
from stack import Stack
import pickle

class Button:
    def __init__(self, x_pos:int, y_pos:int, width:int, height:int, text:str):
        """
        Purpose: To initialize the Button object
        Parameters:
            x_pos: The integer called "x_pos"
            y_pos: The integer called "y_pos"
            width: The integer called "width"
            height: The integer called "height"
            text: The string called "text"
        Return: None
        """        
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        self._text = text
        self._image = self.get_image()
        
    def draw(self, window:GraphWin):
        """
        Purpose: To draw the pressable area and the message of the button
        Parameters: The GraphWin object called "window"
        Return: None 
        """          
        self._image[0].draw(window)
        self._image[1].draw(window)
        
        
    def get_coords(self):
        """
        Purpose: To get the x and y coordinates of the button
        Parameters: None
        Return: Two integers representing the x and y coordinates
        """          
        return self._x_pos, self._y_pos
    
    
    def get_image(self):
        """
        Purpose: To get the visual representation of the button
        Parameters: None
        Return: The Rectangle object called "base" and the Text object called "display"
        """         
        p_start = Point(self._x_pos, self._y_pos)
        p_end = Point((self._x_pos + self._width), (self._y_pos + self._height))
        base = Rectangle(p_start, p_end)
        x_mid = (((self._x_pos * 2) + self._width)) // 2
        y_mid = (((self._y_pos * 2) + self._height)) // 2
        display = Text(Point(x_mid, y_mid), self._text)
        return base, display
        
        
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
        
        left_x, top_y = self._x_pos, self._y_pos
        right_x, bottom_y = left_x + self._width, top_y + self._height
        
        if (left_x <= x <= right_x) and (top_y <= y <= bottom_y):
            return True
        return False
    
    
class Tower:
    def __init__(self, x_pos:int, max_disks:int):
        """
        Purpose: To initialize the Tower object
        Parameters: 
            x_pos: The integer called "x_pos"
            max_disks: The integer called "max_disks"
        Return: None
        """           
        self._x_pos = x_pos
        self._max_disks = max_disks
        self._stack = Stack()
        
        
    def __len__(self):
        """
        Purpose: To return the current number of disks
        Parameters: None
        Return: An integer representing the number of disks in the stack
        """ 
        return len(self._stack)
    
    
    def __str__(self):
        string = ""
        for disk in self.get_disks():
            string += str(disk) + ", "
        return string[:-2]    
    
    
    def add_disk(self, disk:Rectangle):
        """
        Purpose: To add a disk to the stack
        Parameters: The Rectangle object called "disk"
        Return: None
        """           
        self._stack.push(disk)
        
    
    def get_disks(self):
        """
        Purpose: To return a list version of the stack containing the disks
        Parameters: None
        Return: The list of the stack self._stack
        """         
        return self._stack.get_lst()
        
        
    def take_disk(self):
        """
        Purpose: To remove and return the top disk
        Parameters: None
        Return: A Rectangle object
        """        
        if len(self._stack) > 0:
            return self._stack.pop()
            
            
    def build_tower(self, window):
        """
        Purpose: build a tower and draw the pole
        Parameters: window: the window to draw to
        Returns: the objects in the tower
        """
        pole = Rectangle(Point(self._x_pos, 250), Point((self._x_pos + 5), 450))        
        pole.setFill("red")
        pole.setOutline("black")
        pole.draw(window)
        diff_from_max = 5 - len(self)
        objects = []
        rings = self._stack.get_lst()
        for i in range(len(rings)):
            disk = len(self) - rings[i]
            p1 = Point(self._x_pos - 220 + (155 + (disk * 12) + (diff_from_max * 12)), (430 + (i * -20)))
            p2 = Point(self._x_pos - 220 + (290 + (disk * -12) + (diff_from_max * -12)), (450 + (i * -20)))
            rect = Rectangle(p1, p2)
            rect.setFill("blue")
            objects.append(rect)
        return objects


class Hanoi:
    def __init__(self, disks:int, target:int):
        """
        Purpose: To initialize the Hanoi object
        Parameters: 
            disks: The integer called "disks"
            target: The integer called "target"
        Return: None
        """        
        self._disks = disks
        self._target = target
        self._towers = self.make_towers()
        self._game_won = False
        self._steps = 0
        
                    
    def draw(self, window:GraphWin):
        """
        Purpose: To draw all the objects it is given
        Parameters: window: the window to draw to
        Return: None
        """
        objects = []
        for tower in self._towers:
            objects += tower.build_tower(window)
        return objects
                
                                
    def get_max_disks(self):
        """
        Purpose: To get the maximum number of disks each tower can have
        Parameters: None
        Return: An integer
        """           
        return self._disks
    
    
    def get_target(self):
        """
        Purpose: To get the number of the target tower
        Parameters: None
        Return: An integer
        """           
        return self._target
    
    
    def get_steps(self):
        """
        Purpose: To get the number of steps taken
        Parameters: None
        Return: An integer
        """                   
        return self._steps
    
    
    def get_win(self):
        """
        Purpose: To determine if the user won the game
        Parameters: None
        Return: A boolean True or False
        """          
        return len(self._towers[self._target - 1]) == self._disks
    
    
    def move_allowed(self, start:Tower, end:Tower, destination:int, source:int):
        """
        Purpose: To determine if the user's move is illegal
            destination: The integer called "destination"
            source: The integer called "source"
        Return: A boolean True or False and string called "reason"
        """       
        if len(start) == 0:
            reason = "ERROR: the source tower is empty. Please try again!"
            return False, reason
        elif len(end) > 0:
            start_disk = start.get_disks()[0]
            end_disk = end.get_disks()[0]    
            if start_disk > end_disk:
                reason = "ERROR: can't put bigger disk on a smaller one. Please try again!"
                return False, reason
        return True, ""
    
    
    def move_disk(self, source:int, destination:int):
        """
        Purpose: To move a disk with the proper x and y values
        Parameters: 
            destination: The integer called "destination"
            source: The integer called "source"
        Return: The string at allowed_move[1] if allowed_move[0] is False
        """     
        if source == destination or self._game_won:
            return        
        source -= 1
        destination -= 1
        start_tower = self._towers[source]
        end_tower = self._towers[destination]
        allowed_move = self.move_allowed(start_tower, end_tower, destination, source)
        if not allowed_move[0]:
            return allowed_move[1]
        end_tower.add_disk(start_tower.take_disk())
        self._steps += 1
        
        
    def make_towers(self):
        """
        Purpose: To create the three tower objects with the proper number of disks and spacing
        Parameters: None
        Return: a list containing the towers
        """       
        self._steps = 0
        towers = []
        for tower_num in range(3):
            x_pos = ((tower_num + 1) * 220)
            towers.append(Tower(x_pos, 3))
        for disk in range(self._disks):
            towers[0].add_disk(self._disks - disk)
        return towers

        
def undraw_lst(objects):
    """
    Purpose: To undraw all the objects it is given
    Parameters: objects: the objects to undraw
    Return: None
    """
    for i in range(len(objects)):
        g_object = objects.pop()
        g_object.undraw()


def draw_lst(objects, window):
    """
    Purpose: To draw all the objects it is given
    Parameters: 
        objects: the objects to draw
        window: the window to draw to
    Return: The list of the objects
    """
    lst = []
    for i in range(len(objects)):
        g_object = objects.pop()
        g_object.draw(window)
        lst.append(g_object)
    return lst       
            

class Hanoi_Entry: #this should extend entry if we were allowed to use inheritence
    def __init__(self, point:Point, width:int, minimum:int, maximum:int, default:int):
        """
        purpose: initialize an entry for Hanoi within a range
        Parameters: 
            point: the point we are putting the entry
            width: the width of the entry
            min: the minimum value of the entry
            max: the maximum value of the entry
            default: the value to use if none is given
        Returns: None
        """
        self._min = minimum
        self._max = maximum
        self._default = default
        self._entry = Entry(point, width)
        self._objects = []
        self._entry.setText(default)
        
    def get_entry(self) -> Entry:
        """
        Purpose: Get the entry
        Parameters: self: None
        Returns: The entry itself
        """        
        return self._entry
        
    def get_value(self) -> int:
        """
        Purpose: get the value of the entry as an int
        Parameters: self: the entry
        Returns: the value of the entry as an int or the nearest value within the range
        """
        val = self._entry.getText()
        if val.isnumeric():
            val = int(val)
            if val <= self._min:
                return self._min
            elif val >= self._max:
                return self._max
            else:
                return val
        else:
            self._entry.setText(self._default)
            self._entry.setFill("yellow")
            return self._default
            
    def draw(self, window:GraphWin):
        """
        Purpose: draw the entry object
        Parameters: window: the window to draw to
        Returns: None
        """
        self._entry.draw(window)
            

class Hanoi_Graphics:
    def __init__(self):
        """
        Purpose: initialize a Hanoi_Graphics object
        Parameters: None
        Returns: None
        """
        self._window = GraphWin("Hanoi Towers Game", 900, 600)
        self._game = Hanoi(3,3)    
        self._objects = self._game.draw(self._window)
        self._entries = {}
        self.make_entries()
        self._buttons = {}
        self._rings = []
        
        self._announcement = Text(Point(450, 495), "")
        self._announcement.setSize(10)
        self._announcement.setTextColor("red")
        self._announcement.draw(self._window)
        
        self._header = Text(Point(450, 180), "Disks = 3. Target Tower = 3")    
        self._header.setTextColor("green")
        self._header.setSize(18)
        self._header.draw(self._window)
        a = []
        test = Rectangle(Point(0, 0), Point(400, 400))
        test.draw(self._window)
        a.append(test)
        a[0].undraw()
        
        
        self.draw_static()
        self._objects = draw_lst(self._objects, self._window)
    
    
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
            self.announce("Failed to save the game.")
        self.announce("Game saved.")
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
        except OSError:
            game = None
        if game is None:
            self.announce("Can't load a saved game or no game has been saved.")
        else:
            self.announce("Game loaded.")
            self._game = game


    def announce(self, string:str):
        """
        Purpose: To draw the red text on the screen for errors or saving/loading
        Parameters: 
            string: the string to be announced
        Return: None
        """      
        self._announcement.setText(string)


    def make_entries(self):
        """
        Purpose: assemble the entries
        Parameters: self: the game being handled
        Return: None
        """
        self._entries.update({"disk count" : Hanoi_Entry(Point(430, 40), 2, 1, 10, 3)})
        self._entries.update({"target" : Hanoi_Entry(Point(430, 75), 2, 1, 3, 3)})
        self._entries.update({"source" : Hanoi_Entry(Point(157, 540), 2, 1, 3, 1)})
        self._entries.update({"destination" : Hanoi_Entry(Point(255, 540), 2, 1, 3, 3)})
    
            
    def draw_entries(self):
        """
        Purpose: Draw the entries
        Parameters: None
        Return None
        """
        for entry in self._entries:
            self._entries[entry].draw(self._window) 
        
        
    def draw_entry_labels(self):
        """
        Purpose: To draw the labels for our entries
        Parameters: None
        Return: None
        """
        # Initialize and draw the static graphics objects
        objects = []
        objects.append(Text(Point(230, 40), "Number of Disks? (Enter a positive int: 3 by default)"))
        objects.append(Text(Point(219, 75), "Target Tower? (Enter a positive int: 3 by default)"))
        objects.append(Line(Point(50, 450), Point(850, 450)))
        objects.append(Text(Point(97, 540), "From tower?"))
        objects.append(Text(Point(207, 540), "to tower?"))   
        for g_object in objects:
            g_object.draw(self._window)
    
    
    def draw_buttons(self):
        """
        Purpose: draw the buttons
        Parameters: None
        Return: None
        """
        self._buttons.update({"Reset" :     Button(55, 110, 70, 30, "Reset")})
        self._buttons.update({"Quit" :      Button(780, 40, 70, 30, "Quit")})
        self._buttons.update({"Save" :      Button(780, 80, 70, 30, "Save")})
        self._buttons.update({"Load" :      Button(780, 120, 70, 30, "Load")})
        self._buttons.update({"Move Disk" : Button(300, 525, 100, 30, "Move Disk")})
        for button in self._buttons:
            self._buttons[button].draw(self._window)
    
    
    def draw_static(self):
        """
        Purpose: draw all the stuff that doesnt move in the game
        Parameters: None
        Return None
        """
        self.draw_entries()
        self.draw_entry_labels()
        self.draw_buttons()

    
    def update_window(self):
        """
        Purpose: update potentially active objects on the screen
        Parameters: None 
        Return: None
        """              
        self._header.setText(self.get_header_text())
        undraw_lst(self._objects)
        self._objects = self._game.draw(self._window)
        self._objects = draw_lst(self._objects, self._window)
        
        
    def get_header_text(self):
        """
        Purpose: get the text that the header should have
        Parameters: None
        Return: the header text
        """
        if not self._game.get_win():
            return f"Disks = {self._game.get_max_disks()}. Target Tower = {self._game.get_target()}"
        else:
            return f"Congratulations! All disks have been moved to tower {self._game.get_target()} in {self._game.get_steps()} steps."
            
    
    def handle_clicks(self):
        """
        Purpose: handle the clicks made by the person
        Parameters: None
        Return: True if the game should continue
        """
        try:
            cursor = self._window.getMouse()
            
            self.announce("")
            for entry in self._entries:
                # Set entries fill to gray to ensure they do not stay yellow when input is invalid        
                self._entries[entry].get_entry().setFill("gray")
        except:
            self._window.close()
            return False 
            
        if self._buttons["Reset"].is_clicked(cursor):
            print("Resetting...")
            self._game = Hanoi(self._entries["disk count"].get_value(), self._entries["target"].get_value())
            
        elif self._buttons["Quit"].is_clicked(cursor):
            print("Quitting...")
            self._window.close()
            return False
            
        elif self._buttons["Save"].is_clicked(cursor):
            print("Saving...")
            self.save_game("game.p")
            
        elif self._buttons["Load"].is_clicked(cursor):
            print("Loading...")
            self.load_game("game.p")
            
        elif self._buttons["Move Disk"].is_clicked(cursor):
            start = self._entries["source"].get_value()
            end = self._entries["destination"].get_value()
            print(f"Moving Disk from {start} to {end}...") 
            status = self._game.move_disk(start, end)
            if status is not None:
                self.announce(status)
                print(status)
        return True

    def frame_update(self):
        """
        Purpose: handle each frame
        Parameters: None
        Return: True if the game should continue
        """
        self.update_window()
        return self.handle_clicks()



