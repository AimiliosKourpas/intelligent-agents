from Classes.Problem import Problem
from Classes.Node import Node
from Classes.PriorityQueue import PriorityQueue
from Utilities.Utilities import memoize
from Utilities.Constants import MSG_FOUND_SOLUTION_WATER, MSG_NO_SOLUTION_WATER, INFINITY


def bfs(final_destination, jug_1_capacity, jug_2_capacity):
    final_path = []
    front = [(0, 0)]
    visited = set(front)

    while front:
        current = front.pop(0)
        x, y = current
        final_path.append(current)

        if x == final_destination or y == final_destination:
            print(MSG_FOUND_SOLUTION_WATER)
            return final_path

        # Possible actions
        next_states = [
            (jug_1_capacity, y),  # Fill Jug 1
            (x, jug_2_capacity),  # Fill Jug 2
            (0, y),  # Empty Jug 1
            (x, 0),  # Empty Jug 2
            (min(x + y, jug_1_capacity), max(0, x + y - jug_1_capacity)),  # Pour Jug 2 into Jug 1
            (max(0, x + y - jug_2_capacity), min(x + y, jug_2_capacity))  # Pour Jug 1 into Jug 2
        ]

        for state in next_states:
            if state not in visited:
                front.append(state)
                visited.add(state)

    print(MSG_NO_SOLUTION_WATER)
    return []


def best_first_graph_search(problem: Problem, f):
    """
    Search the nodes with the lowest f scores first.
    :param problem: The problem to solve.
    :param f: The function to minimize (e.g., heuristic).
    :return: The solution node or None if no solution is found.
    """
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node

    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()

    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)

    return None


def a_star(problem: Problem, h=None):
    """
    A* search algorithm.
    :param problem: The problem to solve.
    :param h: Heuristic function (defaults to problem.h if not provided).
    :return: The solution node or None if no solution is found.
    """
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))
