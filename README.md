# task scheduling problem 
PROBLEM 1

This Python script calculates the earliest and latest completion times for a set of tasks based on their durations and dependencies. It is useful for project scheduling and determining the critical path in task management.

Overview
The script performs the following functions:

1.Takes a list of tasks and their durations.
2.Receives task dependencies to determine the order in which tasks must be completed.
3.Calculates the Earliest Start Time (EST), Earliest Finish Time (EFT), Latest Start Time (LST), and Latest Finish Time (LFT) for each task.
4.Outputs the earliest and latest possible completion times for the project.


# running the scripts 
1.Open Terminal or Command Prompt
2.Navigate to the Directory Containing the Script
ex:cd path/to/your/directory
3.Run the script
python task-scheduling.py
or
python .\task-scheduling.py (According to file location)

# example user input 
1.List of Tasks: Enter tasks separated by spaces. Example: A B C

2.Task Durations
Enter the duration for task A: 5
Enter the duration for task B: 3
Enter the duration for task C: 2

3.Number of Dependencies
Enter the number of dependencies: 2

4.Task Dependencies: For each dependency, enter the task and its dependency separated by a space. 

Enter a task and its dependency separated by a space: B A
Enter a task and its dependency separated by a space: C B

# The script will calculate:

Earliest Completion Time: The minimum time required to complete all tasks if started as early as possible.
Latest Completion Time: The latest permissible time to complete all tasks without delaying the project.



# friends-network

PROBLEM-2


This Python script manages a network of friends, allowing you to find common friends between two people and determine the degree of separation between two people within the network. It is useful for analyzing social networks or any graph-based relationships.

# Overview
The script provides the following functionalities:

Find Common Friends: Identifies common friends between two given individuals in the network.
Find Nth Connection: Determines the shortest path or degree of separation between two individuals.

# Running the Script
Open Terminal or Command Promp

# Navigate to the Directory Containing the Script
cd path/to/your/directory

# Run the Script:
Execute the script using Python with the following command:
python friends-network.py
OR
python .\friends-network.py (According the file location)

# user input example 
1.Number of Relationships
2.Relationships: For each relationship, enter the two friends separated by a space.
Enter the number of relationships: 3


3.Relationships For each relationship, enter the two friends separated by a space. 
Enter the relationships in the format 'Person Friend':
Alice Bob
Bob Charlie
Charlie David

4.Find Common Friends: Enter two people to find common friends between them.
Enter the first person to find common friends: Alice
Enter the second person to find common friends: Charlie

5.Find Nth Connection: Enter the start and end people to find the degree of separation. 
Enter the starting person to find nth connection: Alice
Enter the ending person to find nth connection: David









