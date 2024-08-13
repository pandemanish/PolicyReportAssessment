class FSM:
    def __init__(self, states, alphabet, initial_state, final_states, transition_function):
        """
        Initializes a finite state machine.
        
        Args:
            states (list): A list of states (Q).
            alphabet (list): A list of input symbols (Σ).
            initial_state: The initial state (q0).
            final_states (list): A list of final states (F).
            transition_function (dict): The transition function (δ) mapping states and inputs to new states.
        """
        self.states = states
        self.alphabet = alphabet
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

    def transition(self, input_symbol):
        """
        Transitions the FSM to the next state based on the input symbol.
        
        Args:
            input_symbol: The input symbol to process (σ).
        """
        self.current_state = self.transition_function[(self.current_state, input_symbol)]

    def get_current_state(self):
        """
        Returns the current state of the FSM.
        
        Returns:
            The current state.
        """
        return self.current_state
