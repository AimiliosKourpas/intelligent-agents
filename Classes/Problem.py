class Problem:
    """
    The abstract class for a formal problem. This outlines the structure of a problem, including the initial state,
    goal state, and the methods to determine actions, results, goal tests, and path costs.
    """

    def __init__(self, initial, goal=None):
        """
        Initialize a problem instance.
        :param initial: The initial state of the problem.
        :param goal: The goal state of the problem (if there is a unique goal).
        """
        self.initial = initial
        self.goal = goal

    def result(self, state, action):
        """
        Return the state that results from executing the given action in the given state.
        This method should be overridden by subclasses.
        :param state: The state before the action is taken.
        :param action: The action to be taken.
        :return: The resulting state after the action.
        """
        raise NotImplementedError("result() must be overridden by subclasses.")

    def path_cost(self, c, state1, action, state2):
        """
        Return the cost of a solution path that arrives at state2 from state1 via action.
        The default method costs 1 for every step in the path.
        :param c: The cost to reach state1.
        :param state1: The state from which the action is taken.
        :param action: The action taken.
        :param state2: The resulting state after the action.
        :return: The cost to reach state2.
        """
        return c + 1

    def actions(self, state):
        """
        Return the actions that can be executed in the given state.
        This method should be overridden by subclasses.
        :param state: The state from which actions are sought.
        :return: A list of possible actions.
        """
        raise NotImplementedError("actions() must be overridden by subclasses.")

    def goal_test(self, state):
        """
        Return True if the given state is a goal state.
        :param state: The state to be tested.
        :return: True if the state is a goal state, False otherwise.
        """
        if isinstance(self.goal, list):
            return state in self.goal
        else:
            return state == self.goal
