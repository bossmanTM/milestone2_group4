from stack import Stack
import pickle

class Tower:
    """a class representing a tower from the game Hanoi. \n
    a tower must only be accessed from the top
    and you cannot have a larger item on top of a smaller one
    """

    def __init__(self, rings, width):
        """ initializes a tower with a given width and any rings you decide to add \n
        args:
             -- rings = the number of rings to add to the tower \n
             -- width = the width of the tower \n
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
        top = self._stack.top()
        if (not self._stack.is_empty()
            and top is not None 
            and top < item):
            return False

        self._stack.push(item)
        return True

    def pop(self):
        """removes a ring from the tower"""
        return self._stack.pop()

    def __str__(self) -> str:
        """returns a string representation of the tower\n
        example:
        .. code-block::
        ***|***
         **|**
          *|*
        .. code-block::
          *|*
           |
           |
        """

        def ring(width: int, size: int) -> str:
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
        return len(self._stack)

    def is_empty(self):
        return self._stack.is_empty()

    def top(self):
        return self._stack.top()

    def get_width(self) -> int:
        return self._width

class Hanoi:
    def __init__(self, towers, disks, target) -> None:
        """defines a Hanoi board\n
         -- towers = the amount of towers in the board  \n
         -- disks = the number of disks in the first tower \n 
         -- target = the tower you are trying to get all the disks to   \n 
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
        """string prepresentation of the Hanoi board"""

        def board_as_array(board, number) -> list[str]:
            title_bar = board.get_width() * "="
            title = title_bar + str(number) + title_bar
            return [title] + str(board).split("\n")

        def add_board_arrays(array, other):
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
        return len(self._game)

    def is_complete(self) -> bool:
        """returns true if the entire stack in the target tower is full"""
        return len(self._game[self._target]) == self._disks


def main():
    option = ""
    print("WELCOME TO HANOI TOWERS GAME!")
    while not verify_option(option, 1, 2):
        option = input("\nEnter 1 to Start a new game and 2 to Resume a saved game: ")
    if option == "1":
        print("Starting a new game ............")
        new_game()
    else:
        filename = input("Enter file name (e.g.: game.p): ")
        existing_game(filename)

def get_ranged_input(str, min, max):
    input_str = ""
    while verify_option(input_str, min, max) == False:
        input_str = input(str)
    return int(input_str)

def verify_option(value, minimum: int, maximum: int):
    if value.is_integer() == False:
        return False
    elif minimum > int(value) or maximum < int(value):
        return False
    return True


def new_game():
    towers = get_ranged_input("Number of towers [min=3,..,max=9]?", 3, 9)
    disks = get_ranged_input("Number of disks [min=3,..,max=9]?", 3, 9)
    target = get_ranged_input("Target Tower [min=2,..,max=4]?", 2, 4)
    
    game = Hanoi(towers, disks, target)
    game_loop(game)
            
    
def existing_game(filename):
    pass

def game_loop(game:Hanoi):
    running = True
    def move_a_disk() -> bool:
        source_tower = get_ranged_input("Source Tower? ", 1, len(game)-1)
        destination_tower = get_ranged_input("Source Tower? ", 1, len(game)-1)
        if not game.transfer(source_tower, destination_tower):
            print("transfer failed, please try again")
            return False
        return True
    def save():
        filename = input("please enter a name for your savefile")
        try:
            with open(filename, "wb") as f:
                pickle.dump(game, f)
        except:
            print("failed to open file for saving")
            return False
        return True
    def exit():
        print("Ending Game . . .")
        print("Goodbye!")
    option = ""
    while running:
        print("\n", game, end = "")
        option = get_ranged_input(" 1 - Move a Disk\n\
                                    2- Save and End\n\
                                    3- End without Saving", 1, 3)
        if option == 1:
            success = False
            while not success:
                success = move_a_disk()
        elif option == 2:
            save_success = False 
            while not save_success:
                save_success = save()
            exit()
            running = False
        elif option == 3:
            exit()
            running = False
