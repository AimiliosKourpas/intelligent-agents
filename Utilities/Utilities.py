import functools
import random
from sys import exit


def exit_program():
    """Exit the program."""
    print("Thank you for using our application.")
    exit()


def gcd(a, b):
    """Return the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a


def generate_random_state(number_of_blocks):
    """
    Generate a random state for the blocks world problem.

    Args:
        number_of_blocks (int): The number of blocks of the problem.

    Returns:
        tuple: The generated state represented as a tuple of tuples.
    """
    random.seed()  # Seed the random number generator with system time
    no_of_stacks = random.randint(1, number_of_blocks)  # Random number of stacks
    state_list = [[] for _ in range(no_of_stacks)]  # Initialize stacks

    for block_num in range(number_of_blocks):
        stack_num = random.randint(0, no_of_stacks - 1)
        state_list[stack_num].append(block_num)

    # Convert to tuple of tuples, excluding empty stacks
    return tuple(tuple(stack) for stack in state_list if stack)


@functools.lru_cache(maxsize=32)
def memoize(fn):
    """
    Memoize a function using LRU cache.

    Args:
        fn (function): The function to memoize.

    Returns:
        function: The memoized function.
    """
    return fn


# Example usage:
if __name__ == "__main__":
    print("GCD of 48 and 18:", gcd(48, 18))
    print("Generated state with 5 blocks:", generate_random_state(5))

    # Memoization example
    @memoize
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    print("Fibonacci of 10:", fib(10))

    exit_program()
