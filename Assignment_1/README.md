To tackle this problem, I'll walk you through the steps to create a function that evaluates the best confidence score threshold that yields a recall of at least 0.9. We'll also define a data structure to store the true positives, true negatives, false positives, and false negatives for each threshold.

Step 1: Define the Data Structure<br />
I have used a dictionary to store the counts for each threshold. The dictionary will have thresholds as keys and another dictionary as values, containing the counts for true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN).

Step 2: Define the Function<br />
I have created a function to iterate over the thresholds, calculate recall for each threshold, and return the best threshold that meets the recall requirement.

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
python Assignment_1/assignment1.py
```

### Run the tests
```
pytest Assignment_1/assignment1_test.py
```

## Explanation:
Data Structure: threshold_data is a dictionary where the keys are confidence thresholds (e.g., 0.1, 0.2) and the values are dictionaries containing TP, TN, FP, and FN counts.

Function: find_best_threshold iterates over the thresholds, calculates recall, and selects the threshold with the highest recall that is at least 0.9.
