# ----------------------------------
# Jackman, Chase; Samson, Enrico
# Programming Project - Milestone #2
# ----------------------------------

from graphics import *
from CMPT103_MS2_Classes_JCES import *
import pickle

"""
Note: If you change the number of disks and the target tower in the entries, 
press the "Reset" button to apply those changes. This is to prevent changing the
number of disks and the target tower during the game.
"""

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


