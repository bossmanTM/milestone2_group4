from stack import Stack


def main():
    option = ""
    print("WELCOME TO HANOI TOWERS GAME!")
    while verify_option(option, 1, 2) == False:
        option = input("\nEnter 1 to Start a new game and 2 to Resume a saved game: ")
    if option == "1":
        print("Starting a new game ............")
        new_game()
    else:
        print("Enter file name (e.g.: game.p): ")
        existing_game()


def verify_option(value: int, minimum: int, maximum: int):
    if value.isdigit() == False:
        return False
    elif minimum > int(value) or maximum < int(value):
        return False
    return True


def new_game():
    disks, target, towers = '', '', ''
    while verify_option(towers, 3, 9) == False:
        towers = input("Number of towers [min=3,..,max=9]?")
    while verify_option(disks, 3, 9) == False:
        disks = input("Number of disks [min=3,..,max=9]?")
    while verify_option(target, 2, 4) == False:
        target = input("Target Tower [min=2,..,max=4]?")
    game_loop(disks, target, towers)
            
    
def existing_game():
    pass


def existing_game():
    pass


def game_loop():
    pass


class Tower:
    """## a class representing a tower from the game Hanoi.
    a tower must only be accessed from the top, \\
    and you cannot have a larger item on top of a smaller one
    """

    def __init__(self, rings, width):
        """ initializes a tower with a given width and any rings you decide to add \\
        args:
             -- rings = the number of rings to add to the tower \\
             -- width = the width of the tower
        """
        if (not isinstance(rings, int)
            or not isinstance(width, int)):
            return
        
        self._width = width
        self._stack = Stack()
        for i in range(rings + 1):
            self.push(rings - i)

    def push(self, item) -> bool:
        """add a ring to the tower\\
        args:
            -- item = an int representing the ring being added to the tower\\
        returns:
            -- True if successful\\
        """
        if (not isinstance(item, int) 
            or not self.get_width() >= item > 0):
            return False
            
        if not self._stack.is_empty():
            # needed because stack.top will print if its empty
            top = self._stack.top()
            if top != None and top < item:
                return False

        self._stack.push(item)
        return True

    def pop(self):
        """removes a ring from the tower"""
        return self._stack.pop()

    def __str__(self) -> str:
        """returns a string representation of the tower\\
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
            return (
                (width - size) * " "
                + size * "*"
                + "|"
                + size * "*"
                + (width - size) * " "
            )

        string = ""
        lst: list[int] = self._stack.get_lst()
        width = self.get_width()
        for i in range(width):
            if i < len(lst):
                string += ring(width, lst[i]) + "\n"
            else:
                string += ring(width, 0) + "\n"
        return string

    def is_empty(self):
        return self._stack.is_empty()

    def top(self):
        return self._stack.top()

    def get_width(self) -> int:
        return self._width


class Hanoi:
    def __init__(self, towers, disks, target) -> None:
        """defines a Hanoi board
        towers = the amount of towers in the board
        disks = the number of disks in the first tower
        target = the tower you are trying to get all the disks to
        """
        if (not isinstance(towers, int)
            or not isinstance(disks, int)
            or not isinstance(target, int)
            or not towers >= target >= 0):
            return

        self._target = target
        self._disks = disks
        self._game: list[Tower] = [Tower(disks, disks)]
        for i in range(towers - 1):
            self._game += [Tower(0, disks)]

    def transfer(self, start: int, end: int) -> bool:
        """transfers one disc from a start board to an end
        returns True if it succeeds
        """
        
        if (not 0 < start < len(self._game)
            or not 0 < end < len(self._game)):
            return False
            
        end -= 1
        start -= 1
        disc = self._game[start].top()
        
        if  (not self._game[end].is_empty()
            and not disc == None
            and disc < self._game[end].top()):
            return False
        self._game[end].push(self._game[start].pop())
        return True

    def __str__(self) -> str:
        """string prepresentation of the Hanoi board"""

        def board_as_array(board, number) -> list[str]:
            return [
                board.get_width() * "="
                + str(number)
                + board.get_width() * "="  # ===== | =====
            ] + str(board).split("\n")

        def add_board_arrays(array, other):
            # i can safely assume they are the same length
            for i in range(len(array)):
                array[i] += (" " * gaps) + other[i]

        gaps = 5
        buff = []
        for i in range(len(self._game)):
            if len(buff) == 0:
                buff += board_as_array(self._game[i], i)
            else:
                add_board_arrays(buff, board_as_array(self._game[i], i))

        string: str = ""
        for line in buff:
            string += line + "\n"
        return string

    def is_complete(self) -> bool:
        """returns true if the entire stack in the target tower is full"""
        return self._game[self._target] == self._disks
        return False
