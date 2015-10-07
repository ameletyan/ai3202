_**Artur Meletyan**_ | _**10/7/15**_ | _**CSCI 3202**_ | _**Assignment 5**_
-
Before running the program, make sure that the file to be processed by it is in the same directory as the program itself.

To run the program, enter the following in the terminal at the directory of the file:

_python Meletyan_Assignment5.py_

Upon running the program, a prompt will come up that will ask for the name of the file that contains the world.  Answer the
prompt and make sure to INCLUDE THE EXTENSION OF THE FILE IN USE (only text files (*.txt) have been sure to work with this
program).  Otherwise, the program will not be able to find the file.

Another prompt will come up that will ask for a value of epsilon.  Any value between 0 and 100 would work fine.  If a value that
is higher than 100 is entered, the program could recurse infinitely.  If a value that is below zero is entered, the program would return an error.

After adding all the input, a result should appear that displays the optimal route throught the world (including locations
traversed and their utilities), a map of the world represented by the utility of each location, and another map of the world 
represented by the optimal move from each location.

**Output of the Program Using Default Input (the file used is World1MDP.txt and the epsilon value used is 0.5)**
-
Enter the file you would like to use: World1MDP.txt

Enter the value of epsilon you would like to use: 0.5

OPTIMAL PATH (including locations and utilities):

Location:  (0, 0) Utility:  0.792539414952
Location:  (1, 0) Utility:  0.9831657121
Location:  (2, 0) Utility:  1.51552089558
Location:  (3, 0) Utility:  2.09327040994
Location:  (3, 1) Utility:  2.71787990186
Location:  (4, 1) Utility:  3.5131841393
Location:  (5, 1) Utility:  3.49053513493
Location:  (5, 2) Utility:  4.40881744777
Location:  (5, 3) Utility:  5.57446851431
Location:  (5, 4) Utility:  6.96665623569
Location:  (6, 4) Utility:  8.36350340691
Location:  (7, 4) Utility:  9.74694743733
Location:  (7, 5) Utility:  13.8808779593
Location:  (7, 6) Utility:  18.1856287425
Location:  (7, 7) Utility:  26.6467065868
Location:  (7, 8) Utility:  36.0
Location:  (7, 9) Utility:  50

WORLD (utility of each space):

Note that these values do not change with epsilon.

3.0 	 4.2 	 5.9 	 7.6 	 9.7 	 13.9 	 18.2 	 26.6 	 36.0 	 50.0 	 
0.0 	 0.0 	 4.4 	 6.2 	 8.4 	 8.7 	 0.0 	 19.2 	 0.0 	 36.0 	 
2.5 	 3.5 	 4.4 	 5.6 	 7.0 	 4.9 	 0.0 	 17.4 	 20.0 	 27.7 	 
0.0 	 3.5 	 0.0 	 0.0 	 5.7 	 6.5 	 11.2 	 14.5 	 0.0 	 20.0 	 
2.1 	 2.7 	 0.0 	 3.4 	 4.4 	 0.0 	 8.0 	 10.1 	 10.0 	 15.3 	 
1.5 	 0.1 	 0.0 	 3.0 	 3.4 	 0.0 	 6.9 	 7.9 	 0.0 	 11.0 	 
1.0 	 -1.2 	 0.0 	 2.3 	 1.7 	 0.0 	 5.4 	 5.2 	 0.0 	 0.0 	 
0.8 	 0.9 	 1.5 	 2.0 	 2.5 	 3.3 	 4.6 	 4.4 	 3.2 	 2.3 	 

WORLD (optimal move from each space):

Note that these values change with epsilon.

R 	 R 	 R 	 R 	 R 	 R 	 R 	 R 	 R 	 F 	 
W 	 W 	 R 	 R 	 U 	 U 	 W 	 U 	 W 	 U 	 
R 	 R 	 R 	 R 	 U 	 U 	 W 	 R 	 R 	 U 	 
W 	 U 	 W 	 W 	 R 	 R 	 R 	 U 	 W 	 U 	 
R 	 U 	 W 	 R 	 U 	 W 	 U 	 U 	 R 	 U 	 
U 	 U 	 W 	 R 	 U 	 W 	 R 	 U 	 W 	 U 	 
U 	 L 	 W 	 U 	 U 	 W 	 U 	 U 	 W 	 W 	 
U 	 R 	 R 	 R 	 R 	 R 	 U 	 U 	 L 	 L 	
