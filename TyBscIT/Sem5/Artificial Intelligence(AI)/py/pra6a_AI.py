import math

class State():
    def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.boat = boat
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.parent = None
        
    def is_goal(self):
        return self.cannibalLeft == 0 and self.missionaryLeft == 0
    
    def is_valid(self): 
        if (self.missionaryLeft >= 0 and self.missionaryRight >= 0 and 
            self.cannibalLeft >= 0 and self.cannibalRight >= 0 and
            (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) and
            (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight)):
            return True
        return False
    
    def _eq_(self, other):
        return (self.cannibalLeft == other.cannibalLeft and
                self.missionaryLeft == other.missionaryLeft and
                self.boat == other.boat and
                self.cannibalRight == other.cannibalRight and
                self.missionaryRight == other.missionaryRight)
    
    def _hash_(self):
        return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))

def successors(cur_state):
    children = []
    if cur_state.boat == 'left':
        possible_moves = [
            (0, 2), (2, 0), (1, 1), (0, 1), (1, 0)
        ]
        for move in possible_moves:
            new_cannibal_left = cur_state.cannibalLeft - move[0]
            new_missionary_left = cur_state.missionaryLeft - move[1]
            new_cannibal_right = cur_state.cannibalRight + move[0]
            new_missionary_right = cur_state.missionaryRight + move[1]
            new_state = State(new_cannibal_left, new_missionary_left, 'right', new_cannibal_right, new_missionary_right)
            if new_state.is_valid():
                new_state.parent = cur_state
                children.append(new_state)
    else:
        possible_moves = [
            (0, 2), (2, 0), (1, 1), (0, 1), (1, 0)
        ]
        for move in possible_moves:
            new_cannibal_left = cur_state.cannibalLeft + move[0]
            new_missionary_left = cur_state.missionaryLeft + move[1]
            new_cannibal_right = cur_state.cannibalRight - move[0]
            new_missionary_right = cur_state.missionaryRight - move[1]
            new_state = State(new_cannibal_left, new_missionary_left, 'left', new_cannibal_right, new_missionary_right)
            if new_state.is_valid():
                new_state.parent = cur_state
                children.append(new_state)
    return children 

def breadth_first_search():
    initial_state = State(3, 3, 'left', 0, 0)
    if initial_state.is_goal():
        return initial_state
    frontier = [initial_state]
    explored = set()
    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if child not in explored and child not in frontier:
                frontier.append(child)
    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    for state in reversed(path):
        print(f"({state.cannibalLeft}, {state.missionaryLeft}, {state.boat}, {state.cannibalRight}, {state.missionaryRight})")

def main():
    solution = breadth_first_search()
    if solution:
        print("Missionaries and Cannibals solution:")
        print("(cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight)")
        print_solution(solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()