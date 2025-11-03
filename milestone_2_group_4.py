from _typeshed import Self
from stack import Stack


def main():
    new_input = input("do you want to start a new game or load an existing one")


def new_game():
    pass


def existing_game():
    pass


def game_loop():
    pass


class Tower:
    def __init__(self):
        self._stack = Stack()

    def __str__(self) -> str:
        def ring(width: int, size: int) -> str:
            return (
                (width - size) * " "
                + size * " "
                + "|"
                + size * " "
                + (width - size) * " "
            )

        string = ""
        lst: list[int] = self._stack.get_lst()
        for item in lst:
            string += ring(len(lst), item) + "\n"
        return string

    def get_width(self) -> int:
        return 4


class Hanoi:
    def __init__(self, games: int):
        self._game: list[Tower] = []

        for i in range(games):
            self._game += [Tower()]

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
