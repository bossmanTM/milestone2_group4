from graphics import *
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
    
class Tower:
    def __init__(self, x_pos:int, max_disks:int):
        """
        Purpose: To initialize the Tower object
        Parameters: 
            x_pos: The integer called "x_pos"
            max_disks: The integer called "max_disks"
        Return: None
        """           
        self._body = Rectangle(Point(x_pos, 250), Point((x_pos + 5), 450))
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
        
    def get_body(self):
        """
        Purpose: To return the red rectangle holding the disks (visually)
        Parameters: None
        Return: A rectangle object
        """         
        return self._body
    
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
        self._towers = self.set_towers()
        self._game_won = False
        self._steps = 0
        
    def draw_towers(self, mode:str, window:GraphWin):
        """
        Purpose: 
        Parameters: 
            mode: The string called "mode" (value of "ud" undraws all the towers)
            window: The GraphWin object called "window"
        Return: None
        """        
        for tower in self._towers:
            base = tower.get_body()
            base.setFill("red")
            base.setOutline("black")
            if mode == "ud":
                base.undraw()
            else:
                base.draw(window)
        for tower in range(len(self._towers)):
            for disk in self._towers[tower].get_disks():
                disk.setFill("blue")
                disk.setOutline("red") 
                if mode == "ud":
                    disk.undraw()   
                else:
                    disk.draw(window)
                
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
            start_size = start_disk.getP2().getX() - start_disk.getP1().getX()
            end_size = end_disk.getP2().getX() - end_disk.getP1().getX()
            if start_size > end_size:
                reason = "ERROR: can't put bigger disk on a smaller one. Please try again!"
                return False, reason
        return True, ""
    
    def move_disk(self, destination:int, source:int):
        """
        Purpose: To move a disk with the proper x and y values
        Parameters: 
            destination: The integer called "destination"
            source: The integer called "source"
        Return: The string at allowed_move[1] if allowed_move[0] is False
        """      
        if source == destination or self._game_won == True:
            return        
        source -= 1
        destination -= 1
        start_tower = self._towers[source]
        end_tower = self._towers[destination]
        allowed_move = self.move_allowed(start_tower, end_tower, destination, source)
        if allowed_move[0] == False:
            return allowed_move[1]
        point_distance = 220 * (destination - source)
        disk_to_move = start_tower.take_disk()
        disk_to_move.move(point_distance, 0)
        end_tower.add_disk(disk_to_move)
        bottom = disk_to_move.getP2().getY()
        disk_to_move.move(0, 40)
        while bottom != 410:
            if bottom > 410:
                disk_to_move.move(0, -1)
                bottom -= 1
            elif bottom < 410:
                disk_to_move.move(0, 1)
                bottom += 1
        disk_to_move.move(0, (-20 * (len(end_tower) - 1)))
        self._steps += 1
        self._game_won = self.get_win()
        
    def set_towers(self):
        """
        Purpose: To create the three tower objects with the proper number of disks and spacing
        Parameters: None
        Return: The list called "towers"
        """       
        self._steps = 0
        diff_from_max = 5 - self._disks
        towers = []
        for tower_num in range(3):
            x_pos = ((tower_num + 1) * 220)
            towers.append(Tower(x_pos, 3))
        for disk in range(self._disks):
            p1 = Point((155 + (disk * 12) + (diff_from_max * 12)), (430 + (disk * -20)))
            p2 = Point((290 + (disk * -12) + (diff_from_max * -12)), (450 + (disk * -20)))
            towers[0].add_disk(Rectangle(p1, p2))
        return towers
    
    def update_towers(self, disks:int, target:int, window:GraphWin):
        """
        Purpose: To redraw all towers to fit any changes made
        Parameters: 
            disks: The integer called "disks"
            target: The integer called "target"
            window: The GraphWin object called "window"
        Return: None
        """          
        self._disks = disks
        self._target = target
        self.draw_towers("ud", window)
        self._towers = self.set_towers()
        self.draw_towers("d", window)
