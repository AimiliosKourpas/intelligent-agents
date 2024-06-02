from Classes.BlocksWorld.BlocksWorld import BlocksWorld


class BlocksWorldH2(BlocksWorld):
    def h(self, node):
        """
        Heuristic that counts the number of moves needed for every block to reach its correct place.
        :param node: current node
        :return: heuristic value (number of moves)
        """
        blocks_not_in_place = 0
        goal_stack_lookup = {block: (i, j) for i, stack in enumerate(self.goal) for j, block in enumerate(stack)}

        for stack in node.state:
            for i, block in enumerate(stack):
                if block in goal_stack_lookup:
                    goal_stack_index, goal_block_index = goal_stack_lookup[block]
                    if stack[:i+1] != self.goal[goal_stack_index][:i+1]:
                        # Count moves needed for blocks above the current block
                        blocks_not_in_place += len(stack) - i
                        # Count moves needed for blocks below the current block
                        for j in range(i+1, len(stack)):
                            if goal_stack_lookup[stack[j]][0] != goal_stack_index:
                                blocks_not_in_place += 1
        
        return blocks_not_in_place
