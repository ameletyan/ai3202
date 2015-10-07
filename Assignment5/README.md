_**Artur Meletyan**_ | _**10/7/15**_ | _**CSCI 3202**_ | _**Assignment 5**_
-
Before running the program, make sure that the file to be processed by it is in the same directory as the program itself.

To run the program, enter the following in the terminal at the directory of the file:

_python Meletyan_Assignment5.py_

Upon running the program, a prompt will come up that will ask for the name of the file that contains the world.  Answer the
prompt and make sure to INCLUDE THE EXTENSION OF THE FILE IN USE (only text files (*.txt) have been sure to work with this
program).  Otherwise, the program will not be able to find the file.

Another prompt will come up that will ask for a value of epsilon.  Any value between 0 and 100 would work fine.  If a value that
is higher than 100 is entered, the program could recurse infinitely.  If a value that is below zero is entered, the program would
return an error.

After adding all the input, a result should appear that displays the optimal route throught the world (including locations
traversed and their utilities), a map of the world represented by the utility of each location, and another map of the world
represented by the optimal move from each location.
