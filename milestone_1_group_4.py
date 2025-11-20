# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #1
# ----------------------------------

from stack import Stack
import pickle

class Tower:
    """
    A class representing a tower from the game Hanoi.
    A Tower must only be accessed from the top,
    and cannot have a larger disk on top of a smaller one
    """

    def __init__(self, rings: int, width: int):
        """
        Purpose: To initialize a Tower
        Parameters: 
            rings: The number of rings in each tower
            width: The total width of the tower
        Return: A Tower object
        """
        if (not isinstance(rings, int)
            or not isinstance(width, int)):
            return
        
        self._width = width
        self._stack = Stack()
        for ring in range(rings):
            self.push(rings - ring)

    def push(self, item: int) -> bool:
        """
        Purpose: Push a ring to the front of the Tower's stack
        Parameters: item: The int value of the ring
        Return: Boolean True or False
        """
        if (not isinstance(item, int) 
            or not self.get_width() >= item > 0):
            return False
        
        # Needed otherwise stack.top will print if empty            
        if not self._stack.is_empty():
            top = self._stack.top()
            if top is not None and top < item:
                return False
        self._stack.push(item)
        return True

    def pop(self):
        """
        Purpose: Pops a ring from the Tower, removing that ring
        Parameters: None
        Return: An int representing the size of the ring
        """
        return self._stack.pop()

    def ring(self, size: int) -> str:
        """
        Purpose: To get a string representation of a ring in the tower
        Parameters: size: The size of the ring
        Return: A string representing the ring
        """
        spacing = (self._width - size) * ' '
        solid = size * '*'
        return f"{spacing}{solid}|{solid}{spacing}"

    def __str__(self) -> str:
        """
        Purpose: To get a string representation of the Tower
        Parameters: None
        Return: A string representing the Tower
        """   

        string = ""
        lst: list[int] = self._stack.get_lst()
        width = self.get_width()
        for i in range(width):
            if i < len(lst):
                string += self.ring(lst[i]) + "\n"
            else:
                string += self.ring(0) + "\n"
        return string
    
    def __len__(self):
        """
        Purpose: To get the length of the tower
        Parameters: None
        Return: An int representing the amount of rings in the tower
        """
        return len(self._stack)

    def is_empty(self):
        """
        Purpose: To check if the Tower is empty
        Parameters: None
        Return: Boolean True or False
        """
        return self._stack.is_empty()

    def top(self):
        """
        Purpose: To get the ring on top of the tower
        Parameters: None
        Return: An int representing the ring at the top of the tower
        """
        return self._stack.top()

    def get_width(self) -> int:
        """
        Purpose: To get the width of the tower
        Parameters: None
        Return: An int representing the width of the tower
        """
        return self._width

class Hanoi:
    def __init__(self, towers: int, disks: int, target: int):
        """
        Purpose: To initialize a Hanoi game object
        Parameters:
            towers: The amount of Towers in the game
            disks: The amount of disks in the starting Tower
            target: the Tower the user is trying to transfer all disks to
        Return: a Hanoi Object
        """
        if (not isinstance(towers, int)
            or not isinstance(disks, int)
            or not isinstance(target, int)
            or not towers >= target >= 0):
            return
        self._target = target - 1
        self._disks = disks
        self._game: list[Tower] = [Tower(disks, disks)]
        self._steps = 0
        for i in range(towers - 1):
            self._game += [Tower(0, disks)]
        
    def transfer(self, start: int, end: int) -> tuple:
        """
        Purpose: Transfer a ring from one Tower to another
        Parameters:
            start: An int pointing to the Tower to transfer from 
            end: An int pointing to the Tower to transfer to 
        Return:
            (True if successful,
            an error message otherwise)
        """
        if ((not 0 < start <= len(self._game))
            or (not 0 < end <= len(self._game))):
            return (False, "Invalid move. that is not a tower. Please try again!")
        end -= 1
        start -= 1
        if self._game[start].is_empty():
            return (False, "Invalid move. the source tower is empty. Please try again!")
            
        disc = self._game[start].top()
        
        if  (not self._game[end].is_empty()
            and not disc == None
            and not disc < self._game[end].top()):
            return (False, "Invalid move. Can't put bigger disk on a smaller one. Please try again!")
        self._game[end].push(self._game[start].pop())
        self._steps += 1
        return (True, "")

    def add_board_arrays(self, gaps: int, array: list, other: list):
        """
        Purpose: To neatly concatenate two arrays side by side
        Parameters: 
            gaps: The amount of padding between array entries
            array: The array going on the left side
            other: The array going on the right side
        Return: None
        """
            # Can safely assume the arrays are the same length
        for i in range(len(array)):
            array[i] += (" " * gaps) + other[i]
            
    def board_as_array(self, board: str, number: int) -> list[str]:
        """
        Purpose: To convert a board to array separating at new lines and adds a title
        Parameters: 
            board: The board to split
            number: The title number of the board
        Return: The array representation of the board
        """
        title_bar = board.get_width() * "="
        title = title_bar + str(number) + title_bar
        return [title] + str(board).split("\n")[:-1]
        
    def __str__(self) -> str:
        """
        Purpose: To get a string representation of the board
        Parameters: None
        Return: A string representing the Hanoi board
        """
        buff, gaps = [], 1
        for i in range(len(self._game)):
            if len(buff) == 0:
                buff += self.board_as_array(self._game[i], i+1)
            else:
                self.add_board_arrays(gaps, buff, self.board_as_array(self._game[i], i+1))

        string: str = ""
        for line in buff:
            string += line + "\n"
        return string
    
    def __len__(self) -> int:
        """
        Purpose: To get the length of the game board
        Parameters: None
        Return: An int representing the amount of games in the board
        """
        return len(self._game)

    def is_complete(self) -> bool:
        """
        Purpose: To determine if the game is complete (all disks are in the target tower)
        Parameters: None
        Return: Boolean True or False
        """
        return len(self._game[self._target]) == self._disks
        
    def get_steps(self):
        """
        Purpose: To get the amount of steps taken so far
        Parameters: None
        Return: An int representing the number of steps taken
        """
        return self._steps

def main():
    """
    Purpose: To enter the program 
    Parameters: None
    Return: None
    """
    option = ""
    print("\nWELCOME TO HANOI TOWERS GAME!")
    option = get_ranged_input("\nEnter 1 to Start a new game and 2 to Resume a saved game: ", 1, 2)
    if option == 1:
        print("Starting a new game ............")
        new_game()
    else:
        game = None
        while game == None:
            filename = input("Enter file name (e.g.: game.p): ")
            game = existing_game(filename)
        game_loop(game)
        
def get_ranged_input(prompt, input_min: str, input_max: str):
    """
    Purpose: To prompt the user for an input until it is inclusively within a target range
    Parameters:
        prompt: The promt to give the user
        input_min: The minimum option the user can enter(inclusive)
        input_max: The maximum option the user can enter(inclusive)
    Return: An int representing the users option within the range
    """
    input_str = ""
    while verify_input(input_str, input_min, input_max) == False:
        input_str = input(prompt)
    return int(input_str)

def verify_input(value:str, minimum: int, maximum: int):
    """
    Purpose: To inclusively verify that the user input is an int within the range
    Parameters: 
        value: The input to be tested
        minimum: The minimum allowable integer (inclusive)
        maximum: The maximum allowable integer (inclusive)
    Return: Boolean True or False
    """
    if value.isdigit():
        return minimum <= int(value) <= maximum
    return False

def new_game():
    """
    Purpose: To start a new Hanoi game
    Parameters: None
    Return: None
    """
    towers = get_ranged_input("Number of towers [min=3,..,max=9]? ", 3, 9)
    disks = get_ranged_input("Number of disks [min=3,..,max=9]? ", 3, 9)
    target = get_ranged_input(f"Target Tower [min=2,..,max={towers}]? ", 2, towers)
    
    game = Hanoi(towers, disks, target)
    game_loop(game)
            
def existing_game(filename: str):
    """
    Purpose: To load an existing game if it exists
    Parameters: filename: The name of the savefile
    Return: A Hanoi game
    """
    game = None
    try:
        with open(filename, "rb") as f:
            game = pickle.load(f)
    except:
        print(f"file: {filename} not found: Starting a new game................")
        new_game()
    return game
    
def move_a_disk(game: Hanoi) -> bool:
    """
    Purpose: To prompt the user then move a disk from a start tower to an end tower
    Parameters: game: The Hanoi game object
    Return: Boolean True or False
    """
    source_tower = get_ranged_input("Source Tower ? ", 1, len(game))
    destination_tower = get_ranged_input("Destination Tower ? ", 1, len(game))
    transfer_result = game.transfer(source_tower, destination_tower)
    if transfer_result[0]:
        return True
    print(transfer_result[1])
    return False

def save(game: Hanoi):
    """
    Purpose: To prompt the user for a file name and save the game
    Parameters: game: a Hanoi game to save
    Return: Boolean True or False
    """
    filename = input("Enter file name (e.g.: game.p): ")
    try:
        with open(filename, "wb") as f:
            pickle.dump(game, f)
    except OSError:
        return False
    print("Game Saved ......")
    return True    

def game_loop(game: Hanoi):
    """
    Purpose: To handle each game operation
    Parameters: game: a Hanoi game to operate on
    Return: None
    """
    running = True
    while running:
        print(f"\n{game}", end = "")
        options = f"\n{"":>4}1 - Move a Disk\n{"":>4}2 - Save and End\n{"":>4}3 - End without Saving\n\n"        
        option = get_ranged_input(f"{options}Enter 1 or 2 or 3: ", 1, 3)
        if option == 1:
            success = move_a_disk(game)
            if success:
                if game.is_complete():
                    print(f"\n{game}\nGood job! Transfer achieved in {game.get_steps()} steps")
                    return

        elif option == 2:
            save_success = False 
            while not save_success:
                save_success = save(game)
            print("See you later ......!")
            running = False
            
        elif option == 3:
            print("Ending Game ......\nGoodbye!")
            running = False
main()
