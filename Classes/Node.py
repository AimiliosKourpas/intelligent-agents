class Node:
    """
    A node in a search tree. Contains pointers to the parent node, the state of the current node,
    the action that led to this state, and the total path cost to reach this node.
    """

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """
        Initialize a search tree node.
        :param state: The state represented by this node.
        :param parent: The parent node.
        :param action: The action that led to this node.
        :param path_cost: The path cost to reach this node.
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = parent.depth + 1 if parent else 0

    def __repr__(self):
        return f"<Node {self.state}>"

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def expand(self, problem):
        """
        List the nodes reachable in one step from this node.
        :param problem: The problem instance that provides actions and results.
        :return: A list of child nodes.
        """
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """
        Create and return a child node based on the action result.
        :param problem: The problem instance that provides actions and results.
        :param action: The action taken to generate the child node.
        :return: A new child node.
        """
        next_state = problem.result(self.state, action)
        return Node(
            next_state,
            parent=self,
            action=action,
            path_cost=problem.path_cost(self.path_cost, self.state, action, next_state)
        )

    def solution(self):
        """
        Return the sequence of actions to go from the root to this node.
        :return: A list of actions.
        """
        return [node.action for node in self.path()[1:]]

    def path(self):
        """
        Return a list of nodes forming the path from the root to this node.
        :return: A list of nodes from the root to this node.
        """
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)
