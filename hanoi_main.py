from stack import Stack
from hanoi_tower import Tower
from hanoi_game import Hanoi

def verify_option(value: int, minimum: int, maximum: int):
    '''
    Purpose: To check if the option's value is an integer within the assigned minimum and maximum values
    Parameters: Variables value, minimum, and maximum as integers
    Return: Boolean of True or False
    '''
    if value.isdigit() == False:
        return False
    elif minimum > int(value) or maximum < int(value):
        return False
    return True


def new_game():
    '''
    Purpose: 
    Parameters:
    Return:
    '''      
    disks, target, towers = '', '', ''
    while verify_option(towers, 3, 9) == False:
        towers = input("Number of towers [min=3,..,max=9]? ")
    while verify_option(disks, 3, 9) == False:
        disks = input("Number of disks [min=3,..,max=9]? ")
    while verify_option(target, 2, 4) == False:
        target = input("Target Tower [min=2,..,max=4]? ")
    game_loop(disks, target, towers)


def save_load(mode:str):
    if mode not in ("s", "l"):
        pass
    pass


def main():
    '''
    Purpose: 
    Parameters:
    Return:
    '''    
    option = ""
    print("WELCOME TO HANOI TOWERS GAME!")
    # If the user did not input a valid option of 1 or 2, keep asking them until they do
    while verify_option(option, 1, 2) == False:
        option = input("\nEnter 1 to Start a new game and 2 to Resume a saved game: ")
    # Start a new game if the option is 1
    if option == "1":
        print("Starting a new game ............")
        new_game()
    # Continue an existing game from a save file if the option is 2
    else:
        print("Enter file name (e.g.: game.p): ")
        save_load()


def move_disk():
    source = input("Source Tower? ")
    target = input("Destination Tower? ")
    pass


def game_loop(disks, target, towers):
    option = ""
    while option != "3":
        print("\n" + str(Hanoi(disks, towers, target)))
        while verify_option(option, 1, 3) == False:
            print("1 - Move a Disk\n2- Save and End\n3- End without Saving\n")
            option = input("Enter 1 or 2 or 3: ")
            print()
        if option == "1":
            move_disk()
        elif option == "2":
            save_load("s")
        else:
            break

main()