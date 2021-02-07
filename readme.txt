Name: FAHAD UR RAHAMAN
UTA Student-ID: 1001753107
Net-ID: fxr3107
Course: CSE-5360-003-ARTIFICIAL INTELLIGENCE I
------------------------------------------------------------------------------------------------------------------
Assignment 1 - Task 1
------------------------------------------------------------------------------------------------------------------
This is the readme.txt file with instructions for running the Assignment 1 - Task 1 program.

This program has been written in Python 3.8.1 and edited in IDLE Editor

Steps to follow to execute this program:
1) Copy the files "find_route.py", "h_kassel.txt", "input1.txt" in the current working directory.
2) Open the Command Prompt in the Windows Operating System.
3) Now go to the current working directory path on the command prompt where you have placed all the above files using "cd" command.
4) Now run the command as "find_route.py input1.txt Bremen Kassel" or "find_route.py input1.txt London Kassel".
5) You will get the Outputs as shown below.

--------------------------------------------------------------------------------------------------------------------

Below is the Output for the program acheived during testing:-
------------------------------------------------------------
Command: find_route.py input1.txt Bremen Kassel
------------------------------------------------------------


C:\Users\fahad\OneDrive\Desktop\UT ARLINGTON\4th SEM - Fall 2020\CSE-5360-003-ARTIFICIAL INTELLIGENCE I\Assignments\Assignment 1>find_route.py input1.txt Bremen Kassel

The output for Uninformed Search is as shown below:

nodes expanded: 12
nodes generated: 20
distance: 297.0 km
route:
Bremen to Hannover, 132.0 km
Hannover to Kassel, 165.0 km
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


C:\Users\fahad\OneDrive\Desktop\UT ARLINGTON\4th SEM - Fall 2020\CSE-5360-003-ARTIFICIAL INTELLIGENCE I\Assignments\Assignment 1>find_route.py input1.txt London Kassel

The output for Uninformed Search is as shown below:

nodes expanded: 7
nodes generated: 7
distance: infinity
route:
none
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


C:\Users\fahad\OneDrive\Desktop\UT ARLINGTON\4th SEM - Fall 2020\CSE-5360-003-ARTIFICIAL INTELLIGENCE I\Assignments\Assignment 1>find_route.py input1.txt Bremen Kassel h_kassel.txt

The output for Informed Search is as shown below:

nodes expanded: 3
nodes generated: 8
distance: 297.0 km
route:
Bremen to Hannover, 132.0 km
Hannover to Kassel, 165.0 km

############################################################ END OF FILE ########################################################################