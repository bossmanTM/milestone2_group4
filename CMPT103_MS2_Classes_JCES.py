from graphics import *
from stack import Stack
import pickle

class Button:
    def __init__(self, x_pos:int, y_pos:int, width:int, height:int, text:str):
        """
        Purpose: 
        Parameters: 
        Return: 
        """        
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        self._text = text
        self._image = self.get_image()
        
    def draw(self, window:GraphWin):
        """
        Purpose: 
        Parameters: 
        Return: 
        """          
        self._image[0].draw(window)
        self._image[1].draw(window)
        
    def get_coords(self):
        """
        Purpose: 
        Parameters: 
        Return: 
        """          
        return self._x_pos, self._y_pos
    
    def get_image(self):
        """
        Purpose: 
        Parameters: 
        Return: 
        """         
        p_start = Point(self._x_pos, self._y_pos)
        p_end = Point((self._x_pos + self._width), (self._y_pos + self._height))
        base = Rectangle(p_start, p_end)
        x_mid = (((self._x_pos * 2) + self._width)) // 2
        y_mid = (((self._y_pos * 2) + self._height)) // 2
        display = Text(Point(x_mid, y_mid), self._text)
        return base, display
    
class Hanoi:
    def __init__(self, disks:int, target:int):
        """
        Purpose: 
        Parameters: 
        Return: 
        """        
        self._disks = disks
        self._target = target
        self._towers = self.set_towers()
        
    def draw_towers(self, mode:str, window:GraphWin):
        """
        Purpose: 
        Parameters: 
        Return: 
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
        Purpose: 
        Parameters: 
        Return: 
        """           
        return self._disks
    
    def get_target(self):
        """
        Purpose: 
        Parameters: 
        Return: 
        """           
        return self._target
    
    def move_disk(self, source:int, destination:int):
        source -= 1
        destination -= 1
        disk_to_move = self._towers[source].take_disk()
        self._towers[destination].add_disk(disk_to_move)
        disk_to_move.move(220 * (destination - source), 40)
        
    def set_towers(self):
        """
        Purpose: 
        Parameters: 
        Return: 
        """       
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
        Purpose: 
        Parameters: 
        Return: 
        """          
        self._disks = disks
        self._target = target
        self.draw_towers("ud", window)
        self._towers = self.set_towers()
        self.draw_towers("d", window)
                    
class Tower:
    def __init__(self, x_pos:int, max_disks:int):
        """
        Purpose: 
        Parameters: 
        Return: 
        """           
        self._body = Rectangle(Point(x_pos, 250), Point((x_pos + 5), 450))
        self._max_disks = max_disks
        self._stack = Stack()
        
    def __len__(self):
        """
        Purpose: 
        Parameters: 
        Return: 
        """ 
        return len(self._stack)
    
    def add_disk(self, disk:Rectangle):
        """
        Purpose: 
        Parameters: 
        Return: 
        """           
        self._stack.push(disk)
        
    def get_body(self):
        """
        Purpose: 
        Parameters: 
        Return: 
        """         
        return self._body
    
    def get_disks(self):
        """
        Purpose: 
        Parameters: 
        Return: 
        """         
        return self._stack.get_lst()
        
    def take_disk(self):
        """
        Purpose: 
        Parameters: 
        Return: 
        """        
        if len(self._stack) > 0:
            return self._stack.pop()