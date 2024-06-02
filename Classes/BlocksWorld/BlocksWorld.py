from Classes.Problem import Problem


class BlocksWorld(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def result(self, state, action):
        """
        Computes the resulting state based on a certain action and the current state.
        :param state: the current state (tuple of tuples)
        :param action: the action to be taken (source_stack, destination_stack)
        :return: the resulting state (tuple of tuples)
        """
        state_list = [list(stack) for stack in state]
        source_stack, destination_stack = action

        # Move the top block from the source stack
        moved_block = state_list[source_stack].pop()

        # Add the moved block to the destination stack
        if destination_stack == ' ':
            state_list.append([moved_block])
        else:
            state_list[destination_stack].append(moved_block)

        # Remove any empty stacks
        state_list = [stack for stack in state_list if stack]

        # Sort the state list by the length of stacks to maintain consistency
        state_list.sort(key=len)

        return tuple(tuple(stack) for stack in state_list)

    def actions(self, state):
        """
        Computes the possible actions to be taken in the current state.
        :param state: the current state (tuple of tuples)
        :return: list of possible actions [(source_stack, destination_stack), ...]
        """
        actions_list = []
        num_stacks = len(state)
        
        for i, stack in enumerate(state):
            if stack:
                # Move block from stack i to another stack j
                for j in range(num_stacks):
                    if i != j:
                        actions_list.append((i, j))
                # Move block from stack i to a new stack (if it's not a single block stack)
                if len(stack) > 1:
                    actions_list.append((i, ' '))
        
        return actions_list

    def goal_test(self, state):
        """
        Checks whether the goal state has been reached based on the current state.
        :param state: the current state (tuple of tuples)
        :return: True if goal state is reached, False otherwise
        """
        return all(stack in self.goal for stack in state)
