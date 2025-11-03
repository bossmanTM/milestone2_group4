from stack import Stack


def main():
    option = 0
    print("WELCOME TO HANOI TOWERS GAME!")
    while option.isdigit() != True and option not in [1, 2]:
        option = input("Enter 1 to Start a new game and 2 to Resume a saved game: ")
    if option == 1:
        new_game()
    else:
        existing_game()

def new_game():
    pass


def existing_game():
    pass


def game_loop():
    pass


class Tower(Stack):
    pass


class Hanoi(Tower):
    def transfer(self, from_: int, to: int) -> None:
        pass

    def __str__(self) -> str:
        return f""

    def is_complete(self) -> bool:
        return False

    def towers(self) -> None:
        """prints the towers in the game window"""
        pass
