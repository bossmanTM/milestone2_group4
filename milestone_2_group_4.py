from stack import Stack


def main():
    option = ""
    print("WELCOME TO HANOI TOWERS GAME!")
    while verify_option(option, 1, 2) == False:
        option = input("\nEnter 1 to Start a new game and 2 to Resume a saved game: ")
    if option == 1:
        new_game()
    else:
        existing_game()


def verify_option(value: int, minimum: int, maximum: int):
    if value.isdigit() != True:
        return False
    elif minimum > int(value) or maximum < int(value):
        return False
    return True


def new_game():
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
        if not isinstance(rings, int):
            return
        if not isinstance(width, int):
            return

        self._stack = Stack()
        for i in range(rings):
            self.push(i + 1)
        self._width = width

    def push(self, item) -> bool:
        """add a ring to the tower\\
        args:
            -- item = an int representing the ring being added to the tower\\
        returns:
            -- True if successful\\
        """
        if not isinstance(item, int):
            return False
        if not self._stack.is_empty():
            # needed because stack.top will print if its empty
            top = self._stack.top()
            if top != None and top < item:
                return False
        if not self.get_width() > item > 0:
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
                string += ring(width, lst[-(i + 1)]) + "\n"
            else:
                string += ring(width, 0) + "\n"
        return string

    def get_width(self) -> int:
        return self._width


class Hanoi:
    def __init__(self, games: int, rings):
        self._game: list[Tower] = [Tower(rings, rings)]
        for i in range(games - 1):
            self._game += [Tower(0, rings)]

    def transfer(self, from_: int, to: int) -> None:
        pass

    def __str__(self) -> str:
        def board_as_array(board: Tower, number: int) -> list[str]:
            return [
                board.get_width() * "="
                + str(number)
                + board.get_width() * "="  # ===== | =====
            ] + str(board).split("\n")

        def add_board_arrays(array: list[str], other: list[str]):
            # i can safely assume they are the same length
            for i in range(len(array)):
                array[i] += other[i]

        buff = []
        for i in range(len(self._game)):
            if len(buff) == 0:
                buff += board_as_array(self._game[i], i)
            add_board_arrays(buff, board_as_array(self._game[i], i))

        string: str = ""
        for line in buff:
            string += line + "\n"
        return string

    def is_complete(self) -> bool:
        return False

    def towers(self) -> None:
        """prints the towers in the game window"""
        pass
