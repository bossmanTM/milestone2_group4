from _typeshed import Self
from stack import Stack


def main():
    option = ''
    print("WELCOME TO HANOI TOWERS GAME!")
    while verify_option(option, 1, 2) == False:
        option = input("\nEnter 1 to Start a new game and 2 to Resume a saved game: ")
    if option == 1:
        new_game()
    else:
        existing_game()

def verify_option(value:int, minimum:int, maximum:int):
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
    def __init__(self, rings, width):
        if not isinstance(rings, int):
            return
        if not isinstance(width, int):
            return

        self._stack = Stack()
        self._width = width
        for i in range(rings):
            self._stack.push(rings - i)

    def push(self, item) -> None:
        if not isinstance(item, int):
            return
        if item > self._width:
            self._stack.push(item)
        elif item > 0:
            self._stack.push(item)

    def pop(self):
        return self._stack.pop()

    def __str__(self) -> str:
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
        for item in lst:
            string += ring(len(lst), item) + "\n"
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
