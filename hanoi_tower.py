from stack import Stack

class Tower:
    num_towers = 0
    
    def __init__(self, max_disks:int, empty_spaces:int):
        '''
        Purpose: To build the Tower
        Parameters: Variables max_disks and empty_spaces as integers
        Return: None
        '''
        Tower.num_towers += 1
        self._tower_num = Tower.num_towers
        self._max_disks = int(max_disks)
        self._empty_spaces = int(empty_spaces)
        if self._empty_spaces > self._max_disks:
            self._empty_spaces = self._max_disks
        self._disks = Stack()
        self.update_disks()
    
    
    def __str__(self):
        '''
        Purpose: To return the string representation of the Tower
        Parameters: None
        Return: The string of Tower
        '''
        # Build the base of the tower
        base = ("=" * self._max_disks) + str(self._tower_num) + ("=" * self._max_disks) + " "
        body, disks = "\n", self._disks.get_lst()
        
        # Build the body of the tower
        for disk in disks:
            body += (" " * disks.index(disk)) + disk + "\n"
        if len(disks) < self._max_disks:
            for empty in range(self._empty_spaces):
                body += (" " * self._max_disks) + "|\n"
        return base + body
    
    
    def remove_disk(self):
        '''
        Purpose: To remove a disk from the Tower
        Parameters: None
        Return: None
        '''            
        # Remove a disk from the stack
        if self._empty_spaces < self._max_disks:
            self._empty_spaces += 1
            self._disks.pop()
    
    
    def update_disks(self):
        '''
        Purpose: To update the stack of the Tower
        Parameters: None
        Return: None
        '''           
        self._disks = Stack()
        for disk in range(self._max_disks, self._empty_spaces, -1):
            self._disks.push(("*" * disk) + "|" + ("*" * disk))
    
    
    def add_disk(self):
        '''
        Purpose: To add a disk from the Tower
        Parameters: None
        Return: None
        '''            
        # If there is an empty space in the tower, add one disk and update the stack
        if self._empty_spaces > 0:
            self._empty_spaces -= 1
            self.update_disks()
            
            
'''
# Test Cases
t1 = Tower(5, 5)
t2 = Tower(5, 0)
print(t1)
t1.add_disk()
print(t2)
print(t1)
t1.remove_disk()
print(t1)
t1.remove_disk()
print(t1)
'''