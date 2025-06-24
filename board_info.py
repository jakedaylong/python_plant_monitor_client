'''This script imports the 'board' module and prints the available 
pins for the board it's run on. This is a useful step in checking 
available Pin names for the partiular board you are working with.'''
import board

print(dir(board))