from _typeshed import Self
from stack import Stack


def main():
    option = None
    print("WELCOME TO HANOI TOWERS GAME!")
    while option.isdigit() != True and option not in [1, 2]:
        option = input("Enter 1 to Start a new game and 2 to Resume a saved game: ")
    if option == 1:
        new_game()
    else:
        existing_game()

def new_game():
    disks, target, towers = None, None, None
    


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


class Hanoi:
    def __init__(self, games: int):
        self._game:list[Tower] = []

        for i in range(games):
            self._game += [Tower()]

    def transfer(self, from_: int, to: int) -> None:
        pass

    def __str__(self) -> str:
        for tower in self._game:



    def is_complete(self) -> bool:
        return False

    def towers(self) -> None:
        """prints the towers in the game window"""
        pass
