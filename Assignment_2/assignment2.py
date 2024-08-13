class ModThreeFSM:
    """
    A Finite State Machine to compute the remainder when a binary string is divided by 3.

    States:
        S0: Remainder 0
        S1: Remainder 1
        S2: Remainder 2

    Transitions:
        S0 -> '0' -> S0
        S0 -> '1' -> S1
        S1 -> '0' -> S2
        S1 -> '1' -> S0
        S2 -> '0' -> S1
        S2 -> '1' -> S2
    """

    def __init__(self):
        self.state = 'S0'
        self.transition_table = {
            'S0': {'0': 'S0', '1': 'S1'},
            'S1': {'0': 'S2', '1': 'S0'},
            'S2': {'0': 'S1', '1': 'S2'}
        }

    def process_input(self, bit):
        """Process a single bit and update the FSM state."""
        self.state = self.transition_table[self.state][bit]

    def get_remainder(self):
        """Return the remainder based on the current FSM state."""
        return {'S0': 0, 'S1': 1, 'S2': 2}[self.state]


def remainder_when_divided_by_3(binary_string):
    """
    Calculate the remainder when a binary string is divided by 3 using a Finite State Machine.

    Args:
        binary_string (str): A binary string to calculate the remainder for.

    Returns:
        int: The remainder when the binary string is divided by 3.

    Raises:
        ValueError: If the input contains characters other than '0' or '1'.
    """

    # Validate input
    if not binary_string or not all(bit in {'0', '1'} for bit in binary_string):
        raise ValueError("Input must contain only binary characters (0 or 1)")

    # Initialize FSM
    fsm = ModThreeFSM()

    # Process each bit in the binary string
    for bit in binary_string:
        fsm.process_input(bit)

    # Return the remainder
    return fsm.get_remainder()


if __name__ == "__main__":
   
    print("Remainder when divided by 3 for '1101' is ", remainder_when_divided_by_3('1101'))
    print("Remainder when divided by 3 for '1110' is ", remainder_when_divided_by_3('1110'))
    print("Remainder when divided by 3 for '1111' is ", remainder_when_divided_by_3('1111'))
    print("Remainder when divided by 3 for '1010' is ", remainder_when_divided_by_3('1010'))
    print("Remainder when divided by 3 for '0' is ", remainder_when_divided_by_3('0'))
    print("Remainder when divided by 3 for '1' is ", remainder_when_divided_by_3('1'))
    print("Remainder when divided by 3 for '1010101010101010101010101010101' is ", remainder_when_divided_by_3('1010101010101010101010101010101'))
    print("Remainder when divided by 3 for '0000' is ", remainder_when_divided_by_3('0000'))
    print("Remainder when divided by 3 for '1111' is ", remainder_when_divided_by_3('1111'))
