from fsm import FSM

def mod_three_fsm(binary_string):
    """
    Computes the remainder when the binary string is divided by 3 using a finite state machine.
    
    Args:
        binary_string (str): The binary string to evaluate.
        
    Returns:
        int: The remainder when the binary string is divided by 3.
    """
    # Define the states, alphabet, initial state, and transition function
    states = ['S0', 'S1', 'S2']
    alphabet = ['0', '1']
    initial_state = 'S0'
    transition_function = {
        ('S0', '0'): 'S0', ('S0', '1'): 'S1',
        ('S1', '0'): 'S2', ('S1', '1'): 'S0',
        ('S2', '0'): 'S1', ('S2', '1'): 'S2'
    }
    output_function = {'S0': 0, 'S1': 1, 'S2': 2}
    
    # Validate input
    if not binary_string or not all(bit in alphabet for bit in binary_string):
        raise ValueError("Input must contain only binary characters (0 or 1)")
    
    # Create an FSM instance
    fsm = FSM(states, alphabet, initial_state, transition_function, output_function)
    
    # Process the input binary string
    for bit in binary_string:
        fsm.transition(bit)
    
    # Get the output from the final state
    return fsm.get_output()
