class BlocksWorld:
    def __init__(self, n):
        self.blocks = [[] for _ in range(n)]

    def initial_state(self):
        self.blocks[0] = [0, 1]
        self.blocks[1] = [2, 3]
        for i in range(2, len(self.blocks)):
            self.blocks[i] = []

    def move(self, source, destination):
        if source == destination or not self.blocks[source]:
            return False
        block = self.blocks[source].pop()
        self.blocks[destination].append(block)
        return True

    def is_goal_state(self, goal):
        for i in range(len(goal)):
            if self.blocks[i] != goal[i]:
                return False
        return True

    def solve(self, goal):
        actions = []
        n = len(goal)
        for i in range(n):
            for j in range(n):
                if i != j:
                    source = i
                    destination = j
                    if self.move(source, destination):
                        actions.append(f"Move block from {source} to {destination}")
                        if self.is_goal_state(goal):
                            return actions
        return None

def main():
    n = 4  # Number of positions
    goal_state = [[] for _ in range(n)]
    goal_state[2] = [0, 1, 2, 3]
    world = BlocksWorld(n)
    world.initial_state()
    actions = world.solve(goal_state)
    if actions:
        print("Actions to reach the goal:")
        for action in actions:
            print(action)
    else:
        print("No solution found!")

if __name__ == '__main__':
    main()