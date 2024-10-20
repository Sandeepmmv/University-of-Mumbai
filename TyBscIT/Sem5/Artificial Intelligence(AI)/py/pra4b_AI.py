class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

def generate_successors(state):
    x, y = state
    successors = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        successors.append(((new_x, new_y), 1))
    return successors

def heuristic_fn(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

def aostar(initial_state, goal_state, generate_successors, heuristic_fn):
    open_list = [Node(initial_state, None, 0, heuristic_fn(initial_state, goal_state))]
    closed_list = {}
    
    while open_list:
        current_node = min(open_list, key=lambda node: node.total_cost)
        open_list.remove(current_node)
        
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.insert(0, current_node.state)
                current_node = current_node.parent
            return path
        
        closed_list[current_node.state] = current_node.total_cost
        
        successors = generate_successors(current_node.state)
        for successor_state, action_cost in successors:
            successor_node = Node(successor_state, current_node, current_node.cost + action_cost, 
                                  heuristic_fn(successor_state, goal_state))
            if successor_state in closed_list and closed_list[successor_state] <= successor_node.total_cost:
                continue
            if successor_node not in open_list:
                open_list.append(successor_node)
    
    return None

initial_state = (0, 0)
goal_state = (4, 4)
path = aostar(initial_state, goal_state, generate_successors, heuristic_fn)

if path is not None:
    print("Optimal path:", path)
else:
    print("No path found.")
