# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #2
# ----------------------------------

from graphics import *
from CMPT103_MS2_Classes_JCES import *
import pickle
 
def main():
    """
    Purpose: To start the game by initializing and drawing the necessary elements
    Parameters: None
    Return: None
    """      
    game = Hanoi_Graphics()
    running = True
    while running:
        running = game.frame_update()
        


main()
