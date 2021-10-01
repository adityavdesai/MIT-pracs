from Astar_search import Astar_search
from puzzle import Puzzle

print('Enter the initial state of puzzle!\n( 0 for blank):')
initial_state = [list(map(int, input().split(" "))) for _ in range(3)]
initial_state = sum(initial_state, [])

print('\n\nEnter the initial state of puzzle!\n( 0 for blank):')
goal_state = [list(map(int, input().split(" "))) for _ in range(3)]
goal_state = sum(goal_state, [])

print('\n\nSolution:\n', Astar_search(initial_state, goal_state))