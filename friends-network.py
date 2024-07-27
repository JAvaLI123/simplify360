from collections import defaultdict, deque

def find_common_friends(friends_graph, person1, person2):
    # Error handling: Check if both persons exist in the graph
    if person1 not in friends_graph or person2 not in friends_graph:
        print(f"One or both persons {person1} and {person2} do not exist in the graph.")
        return set()
    
    # Find common friends between person1 and person2
    return set(friends_graph[person1]).intersection(set(friends_graph[person2]))

def nth_connection(friends_graph, start, end):
    # Error handling: Check if both persons exist in the graph
    if start not in friends_graph or end not in friends_graph:
        print(f"One or both persons {start} and {end} do not exist in the graph.")
        return -1

    # If the start and end persons are the same, return 0 (same person has a connection level of 0)
    if start == end:
        return 0
    
    # Initialize a queue for BFS and a set to track visited nodes
    queue = deque([(start, 0)])  # Queue holds tuples of (current_person, depth)
    visited = set()  # Set to track visited persons
    
    # Perform Breadth-First Search (BFS)
    while queue:
        current, depth = queue.popleft()  # Get the current person and their depth level
        if current in visited:
            continue  # Skip if this person has already been visited
        visited.add(current)  # Mark this person as visited
        
        # Explore all friends of the current person
        for friend in friends_graph[current]:
            if friend == end:
                return depth + 1  # Return the depth level (degree of connection) if the end person is found
            if friend not in visited:
                queue.append((friend, depth + 1))  # Add unvisited friends to the queue with incremented depth
    
    return -1  # Return -1 if no connection is found

def main():
    # Input the number of relationships
    num_relations = int(input("Enter the number of relationships: "))
    friends_graph = defaultdict(list)  # Initialize a dictionary to store the friends graph
    
    # Input the relationships
    print("Enter the relationships in the format 'Person Friend':")
    for _ in range(num_relations):
        person, friend = input().split()  # Get a relationship input
        friends_graph[person].append(friend)  # Add the friend to the person's list
        friends_graph[friend].append(person)  # Add the person to the friend's list (bidirectional friendship)
    
    # Input for finding common friends
    person1 = input("Enter the first person to find common friends: ")
    person2 = input("Enter the second person to find common friends: ")
    common_friends = find_common_friends(friends_graph, person1, person2)
    if common_friends:
        print(f"Common friends between {person1} and {person2}: {common_friends}")
    else:
        print(f"No common friends or one/both persons do not exist.")
    
    # Input for finding nth connection
    start = input("Enter the starting person to find nth connection: ")
    end = input("Enter the ending person to find nth connection: ")
    nth_degree = nth_connection(friends_graph, start, end)
    if nth_degree != -1:
        print(f"The connection level between {start} and {end} is: {nth_degree}")
    else:
        print(f"No connection found between {start} and {end}.")

if __name__ == "__main__":
    main()
