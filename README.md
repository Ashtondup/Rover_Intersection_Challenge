# Rover_Intersection_Challenge
This readme will help you understand how the program works and how to run the program.

## How to run the program:
I have writen this program using Python. To run the program please make sure that you have a Python compiler installed on your device. If you do not have a Python compiler you can download one here https://www.python.org/downloads/. Once you downloaded Python you should also add the Python add-on to your IDE, if you do not already have it.

To run the code please make sure that the text file, name input.txt is in the same folder as the Rover_Chalenge.py, the program wil not work if the text file and the .py file is not in the same file. All you now have to do is prease run and you will get the results in the termenal of the IDE that you are using.

## How the program works
The program reads the text file that contains the coordinates of the plateau the rover is located in the first line, the second line contains the first rover's initial position, the thered line contains the series of instructions telling the first rover how to explore the plateau, the forth line contains the second rover's initial position, the fith line contains the series of instructions telling the second rover how to explore the plateau.

The file is read in to a map to apply a given function to all the items that are in the iterable. To get the x and y axes of the rover I useed the split function to distinguish between the two, this function only workes in the rows, 1, 2 and 3. I than to deteman the movement of the rovers used a for loop to keep the proces to run until it can no longer run. The movement of the rovers are calculated as follow: if the instructions contains a N the y axes will increase by 1, a S will decrease the y axes by 1, a E will increase the x axes by 1, and a W will decrease the x axes by 1.

The end result that you will se is the intersections of the rovers, a visual representation path of the movement of the rovers, and lastle a legend to be able to read the movement of the rovers.
