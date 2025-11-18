from stack import Stack
import pickle

class Tower:
    """a class representing a tower from the game Hanoi. \n
    a tower must only be accessed from the top
    and you cannot have a larger item on top of a smaller one
    """

    def __init__(self, rings, width):
        """ initializes a tower with a given width and any rings you decide to add \n
        parameters:
             -- rings = the number of rings to add to the tower \n
             -- width = the width of the tower \n
        returns:
            a Tower object
        """
        if (not isinstance(rings, int)
            or not isinstance(width, int)):
            return
        
        self._width = width
        self._stack = Stack()
        for i in range(rings):
            self.push(rings - i)

    def push(self, item) -> bool:
        """add a ring to the tower \n
        args:
            -- item = an int representing the ring being added to the tower
        returns:
            -- True if successful
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
        """removes a ring from the tower
        parameters: 
            -- self: a Tower object
        returns: the int that was at the top of the tower
        """
        return self._stack.pop()

    def __str__(self) -> str:
        """returns a string representation of the tower
        parameters: 
            -- self: a Tower object
        returns: a string representation of the Tower
        example:
        .. code-block::
        ***|***
         **|**
          *|*
          
          *|*
           |
           |
        """

        def ring(width: int, size: int) -> str:
            """returns the string representation of a single ring
            (this could be handled if ring was a class and this was __str__ but that is unneeded for the scale of this project)
            parameters: 
                -- width: the maximum size of the ring
                -- size: the size of the ring
            """
            spacing = (width - size) * ' '
            solid = size * '*'
            return f"{spacing}{solid}|{solid}{spacing}"    

        string = ""
        lst: list[int] = self._stack.get_lst()
        width = self.get_width()
        for i in range(width):
            if i < len(lst):
                string += ring(width, lst[i]) + "\n"
            else:
                string += ring(width, 0) + "\n"
        return string
    
    def __len__(self):
        """returns the amount of rings in the tower
        parameters: 
            -- self: a Tower object
        returns: the length of the tower
        """
        return len(self._stack)

    def is_empty(self):
        """returns true if the tower has nothing in it
        parameters: 
            -- self: a Tower object
        returns: true if empty
        """
        return self._stack.is_empty()

    def top(self):
        """returns the top element in the stack (will print if stack is empty)
        parameters: 
            -- self: a Tower object
        returns: the top element of the tower
        """
        return self._stack.top()

    def get_width(self) -> int:
        """returns the width of the tower
        parameters: 
            -- self: a Tower object
        returns: the width of the tower
        """
        return self._width

class Hanoi:
    def __init__(self, towers, disks, target) -> None:
        """defines a Hanoi board\n
         -- towers = the amount of towers in the board  \n
         -- disks = the number of disks in the first tower \n 
         -- target = the tower you are trying to get all the disks to   \n 
        parameters: 
             -- self: a Tower object
        returns: a Hanoi Object
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
        

    def transfer(self, start: int, end: int) -> bool:
        """transfers one disc from a start board to an end
        returns True if it succeeds
        parameters: 
            -- self: a Tower object
        returns: true if successful
        """
        
        if (not 0 < start <= len(self._game)
            or not 0 < end <= len(self._game)):
            return False
            
        end -= 1
        start -= 1
        disc = self._game[start].top()
        
        if  (not self._game[end].is_empty()
            and not disc == None
            and not disc < self._game[end].top()):
            return False
        self._game[end].push(self._game[start].pop())
        return True

    def __str__(self) -> str:
        """string prepresentation of the Hanoi board
        parameters: 
            -- self: a Tower object
        returns: a string representation of the object
        """

        def board_as_array(board, number) -> list[str]:
            """converts a board to string array and adds a titlebar
            parameters: 
                -- board: a Tower object
                -- number: the number of the titlebar
            returns: a list of strings representing each line of the board
            """
            title_bar = board.get_width() * "="
            title = title_bar + str(number) + title_bar
            return [title] + str(board).split("\n")

        def add_board_arrays(array, other):
            """adds two board arrays together in a zip
            parameters:
                array: the left hand array
                other: the other array
            returns: both of the arrays connected line by line
            """
            # i can safely assume they are the same length
            for i in range(len(array)):
                array[i] += (" " * gaps) + other[i]

        gaps = 1
        buff = []
        for i in range(len(self._game)):
            if len(buff) == 0:
                buff += board_as_array(self._game[i], i+1)
            else:
                add_board_arrays(buff, board_as_array(self._game[i], i+1))

        string: str = ""
        for line in buff:
            string += line + "\n"
        return string
    
    def __len__(self) -> int:
        """returns the amount of towers in the game board
        parameters: 
            -- self: a Tower object
        returns: the length of the tower
        """
        return len(self._game)

    def is_complete(self) -> bool:
        """returns true if the entire stack in the target tower is full
        parameters: 
            -- self: a Tower object
        returns: true if complete
        """
        return len(self._game[self._target]) == self._disks


def main():
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
        

def get_ranged_input(prompt, min, max):
    """prompts the user for an input then checks if its within a target range
    """
    input_str = ""
    while verify_input(input_str, min, max) == False:
        input_str = input(prompt)
    return int(input_str)

def verify_input(value:str, minimum: int, maximum: int):
    """inclusively verifies your input is a digit within a given range
    """
    return value.isdigit() and minimum <= int(value) <= maximum

def new_game():
    """starts a new Hanoi game and prompts the user for the details of the game
    """
    towers = get_ranged_input("Number of towers [min=3,..,max=9]? ", 3, 10)
    disks = get_ranged_input("Number of disks [min=3,..,max=9]? ", 3, 10)
    target = get_ranged_input(f"Target Tower [min=2,..,max={towers}]? ", 2, towers+1)
    
    game = Hanoi(towers, disks, target)
    game_loop(game)
            
    
def existing_game(filename):
    """loads a pickled game from the filesystem, if the game does not exist it creates a new one
    """
    game = None
    try:
        with open(filename, "rb") as f:
            game = pickle.load(f)
    except OSError:
        print("failed to open file")
    if not isinstance(game, Hanoi):
        print("file does not contain a game object, starting a new one")
        new_game()
    return game
    

def game_loop(game:Hanoi):
    running = True
    
    def move_a_disk() -> bool:
        source_tower = get_ranged_input("Source Tower? ", 1, len(game))
        destination_tower = get_ranged_input("Destination Tower? ", 1, len(game))
        if not game.transfer(source_tower, destination_tower):
            print("transfer failed, please try again")
            return False
        return True
        
    def save():
        filename = input("please enter a name for your savefile: ")
        try:
            with open(filename, "wb") as f:
                pickle.dump(game, f)
        except OSError:
            print("failed to open file for saving")
            return False
        return True
        
    def exit():
        print("Ending Game . . .")
        print("Goodbye!")
        
    steps = 0
    while running:
        print(game)
        print("1 - Move a Disk")
        print("2- Save and End")
        print("3- End without Saving")
        option = get_ranged_input("Enter 1, 2, or 3: ", 1, 4)
        if option == 1:
            success = False
            while not success:
                success = move_a_disk()
            steps += 1
            if game.is_complete():
                print(f"Good job, Transfer achieved in {steps} steps")
                return
                
        elif option == 2:
            save_success = False 
            while not save_success:
                save_success = save()
            exit()
            running = False
            
        elif option == 3:
            exit()
            running = False
main()
