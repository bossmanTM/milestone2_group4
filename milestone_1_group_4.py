# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #1
# ----------------------------------

from stack import Stack
import pickle

class Tower:
    """a class representing a tower from the game Hanoi. \n
    a tower must only be accessed from the top
    and you cannot have a larger item on top of a smaller one
    """

    def __init__(self, rings, width):
        """
        purpose: initialize a Tower
        parameters: 
            rings: the number of rings in each tower
            width: the total width of the tower
        return: a Tower object
        """
        if (not isinstance(rings, int)
            or not isinstance(width, int)):
            return
        
        self._width = width
        self._stack = Stack()
        self._steps = 0
        for i in range(rings):
            self.push(rings - i)

    def push(self, item) -> bool:
        """
        purpose: push a ring to the tower
        parameters: item: the ring you wish to push
        return: true if successful
        """
        if (not isinstance(item, int) 
            or not self.get_width() >= item > 0):
            return False
        
        # needed because stack.top will print if its empty            
        if not self._stack.is_empty():
            top = self._stack.top()
            if top is not None and top < item:
                return False
        self._stack.push(item)
        return True

    def pop(self):
        """
        purpose: pops a ring from the tower removing that ring
        parameters: 
        return: an int representing the size of the ring
        """
        return self._stack.pop()

    def ring(self, size: int) -> str: # i would really like this to be declared in __str__
        """
        purpose: get a string representation of a ring in the tower
        parameters: size: the size of the ring
        return: a string representing the ring
        """
        spacing = (self._width - size) * ' '
        solid = size * '*'
        return f"{spacing}{solid}|{solid}{spacing}"

    def __str__(self) -> str:
        """
        purpose: get a string representation of the tower
        parameters:
        return: a string representing the tower
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
        purpose: get the length of the tower
        parameters:
        return: an int representing the amount of rings in the tower
        """
        return len(self._stack)

    def is_empty(self):
        """
        purpose: check if the tower is empty
        parameters:
        return: true if empty
        """
        return self._stack.is_empty()

    def top(self):
        """
        purpose: get the ring on top of the tower
        parameters:
        return: an int representing the ring at the top of the tower
        """
        return self._stack.top()

    def get_width(self) -> int:
        """
        purpose: get the width of the tower
        parameters:
        return: an int representing the width of the tower
        """
        return self._width

class Hanoi:
    def __init__(self, towers, disks, target):
        """
        purpose: initialize a Hanoi game object
        parameters:
            towers: the amount of towers in the game
            disks: the amount of disks in the stareting tower
            target: the tower you are trying to transfer to
        return: a Hanoi Object
        """
        if (not isinstance(towers, int)
            or not isinstance(disks, int)
            or not isinstance(target, int)
            or not towers >= target >= 0):
            return
        self._target = target-1
        self._disks = disks
        self._game: list[Tower] = [Tower(disks, disks)]
        for i in range(towers - 1):
            self._game += [Tower(0, disks)]
        

    def transfer(self, start: int, end: int) -> tuple:
        """
        purpose: transfer a ring from one tower to another
        parameters:
            start: an int pointing to the tower to transfer from 
            end: an int poinint to the tower to transfer to 
        return:
            (True if successful,
            an error message if it failed)
        """
        print(len(self._game))
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


    def add_board_arrays(self, gaps, array, other):
        """
        purpose: zip two arrays together
        parameters: 
            gaps: the amount of padding between array entries
            array: the array going on the left side
            other: the array going on the right side
        return:
        """
            # i can safely assume they are the same length
        for i in range(len(array)):
            array[i] += (" " * gaps) + other[i]
            
    def board_as_array(self, board, number) -> list[str]:
        """
        purpose: convert a board to array separating at new lines and adds a title
        parameters: 
            board: the board to split
            number: the title number of the board
        return: the array representation of the board
        """
        title_bar = board.get_width() * "="
        title = title_bar + str(number) + title_bar
        return [title] + str(board).split("\n")
        
    def __str__(self) -> str:
        """
        purpose: get a string representation of the board
        parameters:
        return: a string representing the Hanoi board
        """

        gaps = 1
        buff = []
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
        purpose: get the length of the game board
        parameters:
        return: an int representing the amount of games in the board
        """
        return len(self._game)

    def is_complete(self) -> bool:
        """
        purpose: determine if the game is complete (all disks are in the target tower)
        parameters:
        return: True if complete
        """
        return len(self._game[self._target]) == self._disks
        
    def get_steps(self):
        """
        purpose: get the amount of steps taken so far
        parameters: 
        return: an int representing the number of steps taken
        """
        return self._steps

def main():
    """
    purpose: enter the program 
    parameters:
    return: None
    """
    option = ""
    print("WELCOME TO HANOI TOWERS GAME!")
    option = get_ranged_input("\nEnter 1 to Start a new game and 2 to Resume a saved game: ", 1, 2)
    if option == 1:
        print("Starting a new game ............")
        new_game()
    else:
        game = None
        while game is None:
            filename = input("Enter file name (e.g.: game.p): ")
            game = existing_game(filename)
        game_loop(game)
        

def get_ranged_input(prompt, input_min, input_max):
    """
    purpose: prompt the user for an input until it is inclusively within a target range
    parameters:
        prompt: the promt to give the user
        input_min: the minimum option the user can enter(inclusive)
        input_max: the maximum option the user can enter(inclusive)
    return: an int representing the users option within the range
    """
    input_str = ""
    while verify_input(input_str, input_min, input_max) == False:
        input_str = input(prompt)
    return int(input_str)

def verify_input(value:str, minimum: int, maximum: int):
    """
    purpose: inclusively verify that your input is an int within the range
    parameters: 
        value: the input to be tested
        minimum: the minimum allowable integer (inclusive)
        maximum: the maximum allowable integer (inclusive)
    return: True if within the range and an int
    """
    if value.isdigit():
        return minimum <= int(value) <= maximum
    return False

def new_game():
    """
    purpose: start a new Hanoi game
    parameters: steps: t
    return:
    """
    towers = get_ranged_input("Number of towers [min=3,..,max=9]? ", 3, 9)
    disks = get_ranged_input("Number of disks [min=3,..,max=9]? ", 3, 9)
    target = get_ranged_input(f"Target Tower [min=2,..,max={towers}]? ", 2, towers+1)
    
    game = Hanoi(towers, disks, target)
    game_loop(game)
            
    
def existing_game(filename):
    """
    purpose: load an existing game if it exists
    parameters: filename: the name of the savefile
    return: a Hanoi game
    """
    game = None
    try:
        with open(filename, "rb") as f:
            game = pickle.load(f)
    except:
        print(f"file: {filename} not found: Starting a new game................")
        new_game()
    return game
    
def move_a_disk(game) -> bool:
    """
    purpose: prompt the user then move a disk from a start tower to an end tower
    parameters: game: the Hanoi game object
    return: True if successful
    """
    source_tower = get_ranged_input("Source Tower? ", 1, len(game))
    destination_tower = get_ranged_input("Destination Tower? ", 1, len(game))
    transfer_result = game.transfer(source_tower, destination_tower)
    if transfer_result[0]:
        return True
    print(transfer_result[1])
    return False

def save(game):
    """
    purpose: prompt the user and save the game
    parameters: game: a Hanoi game to save
    return: True if successful
    """
    filename = input("Enter file name (e.g.: game.p): ")
    try:
        with open(filename, "wb") as f:
            pickle.dump(game, f)
    except OSError:
        print("Failed to open file for saving")
        return False
    print("Game Saved ......")
    return True    

def game_loop(game: Hanoi):
    """
    purpose: handle each game operation
    parameters: game: a Hanoi game to operate on
    return: None
    """
    running = True
        
    while running:
        print(f"\n{game}", end = "")
        print("1 - Move a Disk")
        print("2 - Save and End")
        print("3 - End without Saving\n")
        option = get_ranged_input("Enter 1, 2, or 3: ", 1, 4)
        if option == 1:
            success = move_a_disk(game)
            if success:
                if game.is_complete():
                    print(f"\n{game}Good job! Transfer achieved in {game.get_steps()} steps")
                    return
                
        elif option == 2:
            save_success = False 
            while not save_success:
                save_success = save(game)
            print("See you later ......!")
            running = False
            
        elif option == 3:
            print("Ending Game ......")
            print("Goodbye!")
            running = False
main()
