from Utilities.SearchAlgorithms import bfs, a_star
from Utilities.Utilities import gcd, _exit, state_generator
from Classes.BlocksWorld.BlocksWorldH2 import BlocksWorldH2
from Utilities.Constants import MSG_SELECT_GAME, ALLOWED_ANSWERS, DEFAULT_ANSWER
from Utilities.Constants import MSG_INPUT_1, MSG_INPUT_2, MSG_INPUT_TARGET, MSG_NO_POSSIBLE_SOLUTION_WATER


def jugs_problem():
    jug_1_capacity = int(input(MSG_INPUT_1))
    jug_2_capacity = int(input(MSG_INPUT_2))
    final_destination = int(input(MSG_INPUT_TARGET))

    if final_destination % gcd(jug_1_capacity, jug_2_capacity) != 0:
        print(MSG_NO_POSSIBLE_SOLUTION_WATER)
        return

    solution = bfs(final_destination, jug_1_capacity, jug_2_capacity)
    print(solution)


def block_world():
    print("Block world problem")
    blocks = int(input("Number of blocks: "))

    initial_state = state_generator(blocks)  # Generate random states for initial and goal state
    goal_state = state_generator(blocks)
    print(f"Initial: {initial_state}")
    print(f"Goal: {goal_state}")

    if initial_state == goal_state:
        print("Initial State is the same as the Goal State")
        return

    problem = BlocksWorldH2(initial_state, goal_state)

    result = a_star(problem)  # A* search using second heuristic
    solution = result.solution()
    path = result.path()

    print("{:=^41}".format(" Solution "))
    print("{:^16} | {:<50}".format("ACTION", "STATE"))
    print("{:<16} | {:<50}".format('Initial State', str(initial_state)))

    for i in range(1, len(path)):
        state = path[i].state
        action = solution[i - 1]

        if action[1] != ' ':
            msg = f"Move from {action[0]} to {action[1]}"
        else:
            msg = f"Move {action[0]} down"

        print("{:<16} | {:<50}".format(msg, str(state)))


def show_menu():
    while True:
        problem = input(MSG_SELECT_GAME).strip().upper()
        if problem in ALLOWED_ANSWERS:
            break

    if problem == "1":
        jugs_problem()
    elif problem == "2":
        block_world()
    elif problem == "Q":
        _exit()
