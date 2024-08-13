To solve this problem using a Finite State Machine (FSM), we'll design a solution where the FSM has states corresponding to the possible remainders when a binary number is divided by 3. Specifically, the FSM will have three states:

- State 0: The remainder is 0.
- State 1: The remainder is 1.
- State 2: The remainder is 2.

The FSM will process the binary string one bit at a time, starting from the leftmost bit, and will transition between states based on the current state and the current bit being processed.

### State Transition Table
The state transitions can be summarized as follows:

- State 0:
    - Input `0` -> Stay in State 0 (because appending a 0 does not change the number)
    - Input `1` -> Move to State 1 (because appending a 1 gives a remainder of 1)
- State 1:
    - Input `0` -> Move to State 2 (because appending a 0 to a remainder of 1 doubles the number and shifts it towards a remainder of 2)
    - Input `1` -> Move to State 0 (because appending a 1 completes a cycle and brings the remainder back to 0)
- State 2:
    - Input `0` -> Move to State 1 (because appending a 0 to a remainder of 2 shifts it back to a remainder of 1)
    - Input `1` -> Move to State 2 (because appending a 1 gives a remainder of 2)


### Create a virtual environment
```
python3 -m venv venv
```

### Activate the virtual environment
```
source venv/bin/activate
```

### Install the required packages
```
pip install -r requirements.txt
```

### Run the program
```
python Assignment_2/assignment2.py
```

### Run the tests
```
pytest Assignment_2/assignment2_test.py
```

## Explanation
- The function starts at State 0.
- As it reads each bit of the binary string, it transitions between states according to the state transition table.
- After processing the entire string, the final state represents the remainder when the binary number is divided by 3.