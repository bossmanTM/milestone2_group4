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


class Hanoi:
    def transfer(self, from_: int, to: int) -> None:
        pass

    def __str__(self) -> str:
        return f""

    def is_complete(self) -> bool:
        return False

    def towers(self) -> None:
        """prints the towers in the game window"""
        pass
