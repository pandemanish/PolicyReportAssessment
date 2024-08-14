class FSM:
    def __init__(self, states, alphabet, initial_state, transition_function, output_function=None):
        """
        Initializes a finite state machine.
        
        Args:
            states (list): A list of states (Q).
            alphabet (list): A list of input symbols (Σ).
            initial_state: The initial state (q0).
            transition_function (dict): The transition function (δ) mapping states and inputs to new states.
            output_function (dict, optional): A function or mapping that converts states to outputs (e.g., remainders).
        """
        self.states = states
        self.alphabet = alphabet
        self.current_state = initial_state
        self.transition_function = transition_function
        self.output_function = output_function or {}

    def transition(self, input_symbol):
        """
        Transitions the FSM to the next state based on the input symbol.
        
        Args:
            input_symbol: The input symbol to process (σ).
        """
        if (self.current_state, input_symbol) in self.transition_function:
            self.current_state = self.transition_function[(self.current_state, input_symbol)]
        else:
            raise ValueError(f"No transition defined for state {self.current_state} with input {input_symbol}")

    def get_current_state(self):
        """
        Returns the current state of the FSM.
        
        Returns:
            The current state.
        """
        return self.current_state

    def get_output(self):
        """
        Returns the output corresponding to the current state, if an output function is defined.
        
        Returns:
            The output corresponding to the current state.
        """
        return self.output_function.get(self.current_state, None)
