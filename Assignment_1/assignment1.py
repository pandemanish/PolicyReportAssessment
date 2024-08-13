
def calculate_recall(TP, FN):
    # Calculate recall
    return  TP / (TP + FN) if (TP + FN) > 0 else 0  # Avoid division by zero


def find_best_threshold(threshold_data):
    """
    Finds the best threshold that yields a recall >= 0.9.
    
    Args:
    - threshold_data (dict): A dictionary where the key is the threshold and the value is 
      another dictionary containing TP, TN, FP, FN.
      
    Returns:
    - best_threshold (float): The threshold that gives the best recall >= 0.9.
    """
    # Initialize variables to keep track of the best threshold and its recall
    best_threshold = None
    # Initialize the best recall to 0
    best_recall = 0
    
    for threshold, counts in threshold_data.items():
        # Check if the counts dictionary has the required keys
        if 'TP' not in counts or 'FN' not in counts:
            continue
        
        TP = counts['TP']
        FN = counts['FN']
        
        # Check if TP and FN are valid numbers
        if not isinstance(TP, (int, float)) or not isinstance(FN, (int, float)) or TP < 0 or FN < 0:
            continue
        
        recall = calculate_recall(TP, FN)
        print(f"Threshold: {threshold}, Recall: {recall}")
        
        # Check if recall is >= 0.9 and update the best threshold
        if recall >= 0.9 and recall > best_recall:
            best_recall = recall
            best_threshold = threshold
    
    return best_threshold


if __name__ == "__main__":
    # data structure
    threshold_data = {
        0.1: {'TP': 90, 'TN': 100, 'FP': 10, 'FN': 40},
        0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': 5},
        0.3: {'TP': 80, 'TN': 110, 'FP': 20, 'FN': 20},
        0.4: {'TP': 78, 'TN': 115, 'FP': 22, 'FN': 22},
        0.5: {'TP': 70, 'TN': 120, 'FP': 30, 'FN': 30},
        0.6: {'TP': 68, 'TN': 125, 'FP': 32, 'FN': 32},
        0.7: {'TP': 65, 'TN': 130, 'FP': 35, 'FN': 35},
        0.8: {'TP': 60, 'TN': 135, 'FP': 40, 'FN': 40},
        0.9: {'TP': 58, 'TN': 140, 'FP': 42, 'FN': 42}
    }

    # function usage
    best_threshold = find_best_threshold(threshold_data)
    print(f"\nThe best threshold with recall >= 0.9 is: {best_threshold}")