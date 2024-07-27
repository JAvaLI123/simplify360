from collections import defaultdict, deque

def find_schedule():
    # Prompt user to enter the list of tasks
    tasks = input("Enter the list of tasks separated by spaces: ").split()
    
    # Prompt user to enter the duration for each task and store in a dictionary
    durations = {task: int(input(f"Enter the duration for task {task}: ")) for task in tasks}
    
    # Initialize a defaultdict to hold task dependencies
    dependencies = defaultdict(list)
    
    # Prompt user to enter the number of dependencies
    num_dependencies = int(input("Enter the number of dependencies: "))
    
    # Input dependencies for each task
    for _ in range(num_dependencies):
        task, dependency = input("Enter a task and its dependency separated by a space: ").split()
        dependencies[task].append(dependency)
    
    # Initialize dictionaries to store Early Start Time (EST), Early Finish Time (EFT),
    # Late Start Time (LST), and Late Finish Time (LFT) for each task
    EST = {task: 0 for task in tasks}
    EFT = {task: 0 for task in tasks}
    LST = {task: float('inf') for task in tasks}
    LFT = {task: float('inf') for task in tasks}
    
    # Build the graph for task dependencies and initialize in-degree counts
    graph = defaultdict(list)
    in_degree = {task: 0 for task in tasks}
    
    # Populate the graph and update in-degree counts
    for task, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(task)  # Dependent task added to the graph
            in_degree[task] += 1  # Increment in-degree count for the task
    
    # Perform Topological Sorting using Kahn's algorithm
    queue = deque([t for t in tasks if in_degree[t] == 0])  # Initialize queue with tasks having 0 in-degree
    order = []  # List to store the topologically sorted order of tasks
    
    while queue:
        t = queue.popleft()  # Get a task from the queue
        order.append(t)  # Add it to the topological order
        # Update in-degree counts and add new tasks with 0 in-degree to the queue
        for neighbor in graph[t]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Calculate Early Start Time (EST) and Early Finish Time (EFT) for each task
    for t in order:
        EFT[t] = EST[t] + durations[t]  # Calculate the finish time for the task
        for neighbor in graph[t]:
            EST[neighbor] = max(EST[neighbor], EFT[t])  # Update EST for dependent tasks
    
    # Calculate Late Finish Time (LFT) and Late Start Time (LST) for each task
    max_time = max(EFT.values())  # Determine the maximum EFT value for LFT calculation
    for t in tasks:
        LFT[t] = max_time  # Initialize LFT for each task to the maximum EFT value
    
    # Compute LFT and LST by iterating in reverse topological order
    for t in reversed(order):
        if graph[t]:
            LFT[t] = min(LFT[t], min(LFT[neighbor] for neighbor in graph[t]))  # Update LFT based on dependent tasks
        LST[t] = LFT[t] - durations[t]  # Calculate LST based on LFT and task duration
    
    # Print the results
    earliest_completion_time = max(EFT.values())  # Determine the earliest completion time
    latest_completion_time = max(LFT.values())  # Determine the latest completion time
    print(f"Earliest completion time: {earliest_completion_time}")
    print(f"Latest completion time: {latest_completion_time}")

if __name__ == "__main__":
    find_schedule()
