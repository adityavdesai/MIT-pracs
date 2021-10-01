from queue import PriorityQueue
from puzzle import Puzzle

# A* seach algorithm
def Astar_search(initial_state, final_state):
    count = 0
    explored = []
    start_node = Puzzle(initial_state, final_state, None, None, 0)
    q = PriorityQueue()
    q.put((start_node.evaluation_function, count, start_node))

    while not q.empty():
        node = q.get()
        node = node[2]
        explored.append(node.state)
        if node.goal_test():
            return node.find_solution()

        children = node.generate_child()
        for child in children:
            if child.state not in explored:
                count += 1
                q.put((child.evaluation_function, count, child))
    return