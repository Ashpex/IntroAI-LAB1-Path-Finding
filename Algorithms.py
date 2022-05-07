import math
from queue import PriorityQueue
import numpy as np

def heuristic(matrix, start):
    """
    Compute Huristic function h(X) = Euclidean distance between node x and goal point.
    Parameters:
    ---------------------------
    matrix: list
        list of points
    start: integer
        starting node
    Returns: list of huristic values

    ---------------------
    h: float
        Huristic function
    """

    heuristic = {}
    heuristic[start] = 1

    queue = [start]
    visited = []
    while bool(queue):
        point = queue.pop()
        for i in range(matrix.shape[0]):
            if matrix[point][i] > 0 and i not in visited and i not in queue:
                queue.append(i)
                heuristic[i] = heuristic[point] + 1
        visited.append(point)
    return heuristic


def euclidean_distance(pos, current, goal):
    return math.sqrt((pos[current][0]-pos[goal][0])*(pos[current][0]-pos[goal][0])+(pos[current][1]-pos[goal][1])*(pos[current][1]-pos[goal][1]))

def DFS(matrix, start, end):
    """
    DFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 

    path=[]
    visited={}

    if(end >= matrix.shape[0]):
        return visited, path
    
    path.append(start)
    current_point = path[len(path)-1]


    while end not in path:
        for i in range(matrix.shape[0]):
            if matrix[current_point][i] == 1 and i not in path:
                path.append(i)
                visited[i] = current_point
                current_point = i
                break
            if i == matrix.shape[0]-1:
                current_point = visited[current_point]

    print("Path: ", path)
    print("Visited", visited)            

    return visited, path

def BFS(matrix, start, end):
    """
    BFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    print("Implement BFS algorithm")
    path=[]
    visited={}
    priority_queue = []

    if(end >= matrix.shape[0]):
        return visited, path
    
    path.append(start)
    priority_queue.append(start)

    while end not in path:
        current_point = priority_queue.pop(0)
        for i in range(matrix.shape[0]):
            if matrix[current_point][i] == 1 and i not in path:
                path.append(i)
                visited[i] = current_point
                priority_queue.append(i)

    print("Path: ", path)
    print("Visited", visited)  
    
    return visited, path

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    path=[]
    visited={}
    list = {}
    checked_point = []
    print("Implement UCS algorithm")

    if(end >= matrix.shape[0]):
        return visited, path
    
    list[start] = 0
    get_point = -1
    
    while get_point != end:
        min_value = 999999999999999999
        for key in list:
            if list[key] < min_value:
                get_point = key
                min_value = list[key]
        if get_point == end:
            break
        
        checked_point.append(get_point)
        for i in range(matrix.shape[0]):
            if matrix[get_point][i] > 0 and i not in checked_point:
                value = list[get_point] + matrix[get_point][i]
                if i in list and value > list[i]:
                    continue
                list[i] = value
                visited[i] = get_point
        del list[get_point]

    point = end
    path.append(end)
    while point != start:
        path.append(visited[point])
        point = visited[point]

    path.reverse()
    print("Path: ", path)
    print("Visited", visited)  
    return visited, path

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    priority_queue={}
    queueVisited = []
    priority_queue[start] = 0
    print("Implement GBFS algorithm")

    while priority_queue != {}:
        heuristic_values = heuristic(matrix, start)
        current_point = 0
        heuristicGoal = heuristic_values[end]
        for i in priority_queue:
            current_point = i
            break
        for i in priority_queue:
            if heuristicGoal - heuristic_values[i] <= heuristicGoal - heuristic_values[current_point]:
                if i == end:
                    current_point = i
                    break
                current_point = i
        if current_point == end:
            break
        priority_queue.pop(current_point)
        queueVisited.append(current_point)
        for i in range(matrix.shape[0]):
            if matrix[current_point][i] > 0 and i not in priority_queue and i not in queueVisited:
                priority_queue[i] = matrix[current_point][i]
                visited[i] = current_point
    
    point = end
    path.append(end)
    while point != start:
        path.append(visited[point])
        point = visited[point]
    path.reverse()
    print("Path: ", path)
    print("Visited", visited)  

    return visited, path


def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    priority_queue={}
    queueVisited = []
    priority_queue[start] = 0
    print("Implement A* algorithm")

    while priority_queue != {}:
        heuristic_values = heuristic(matrix, start)
        current_point = 0
        heuristicGoal = heuristic_values[end]
        for i in priority_queue:
            current_point = i
            break
        for i in priority_queue:
            if heuristicGoal - heuristic_values[i] + euclidean_distance(pos, i, end) <= heuristicGoal - heuristic_values[current_point] + euclidean_distance(pos,current_point, end):
                if i == end:
                    current_point = i
                    break
                current_point = i
        if current_point == end:
            break
        priority_queue.pop(current_point)
        queueVisited.append(current_point)
        for i in range(matrix.shape[0]):
            if matrix[current_point][i] > 0 and i not in priority_queue and i not in queueVisited:
                priority_queue[i] = matrix[current_point][i]
                visited[i] = current_point
    
    point = end
    path.append(end)
    while point != start:
        path.append(visited[point])
        point = visited[point]
    path.reverse()
    print("Path: ", path)
    print("Visited", visited)

    return visited, path

