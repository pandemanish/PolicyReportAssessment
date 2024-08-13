from assignment1 import find_best_threshold

class TestFindBestThreshold:

    # Correctly identifies the best threshold with recall >= 0.9
    def test_correct_threshold_identification(self):
        threshold_data = {
            0.1: {'TP': 90, 'TN': 100, 'FP': 10, 'FN': 10},
            0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': 15},
            0.3: {'TP': 80, 'TN': 110, 'FP': 20, 'FN': 20},
            0.4: {'TP': 78, 'TN': 115, 'FP': 22, 'FN': 22},
            0.5: {'TP': 70, 'TN': 120, 'FP': 30, 'FN': 30},
            0.6: {'TP': 68, 'TN': 125, 'FP': 32, 'FN': 32},
            0.7: {'TP': 65, 'TN': 130, 'FP': 35, 'FN': 35},
            0.8: {'TP': 60, 'TN': 135, 'FP': 40, 'FN': 40},
            0.9: {'TP': 58, 'TN': 140, 'FP': 42, 'FN': 42}
        }
        result = find_best_threshold(threshold_data)
        assert result == 0.1

    # Handles empty threshold_data dictionary
    def test_empty_threshold_data(self):
        threshold_data = {}
        result = find_best_threshold(threshold_data)
        assert result is None

    # Returns None when no threshold meets the recall requirement
    def test_returns_none_when_no_threshold_meets_recall_requirement(self):
        threshold_data = {
            0.1: {'TP': 50, 'TN': 100, 'FP': 10, 'FN': 50},
            0.2: {'TP': 50, 'TN': 105, 'FP': 15, 'FN': 50},
            0.3: {'TP': 50, 'TN': 110, 'FP': 20, 'FN': 50},
            0.4: {'TP': 50, 'TN': 115, 'FP': 22, 'FN': 50},
            0.5: {'TP': 50, 'TN': 120, 'FP': 30, 'FN': 50},
            0.6: {'TP': 50, 'TN': 125, 'FP': 32, 'FN': 50},
            0.7: {'TP': 50, 'TN': 130, 'FP': 35, 'FN': 50},
            0.8: {'TP': 50, 'TN': 135, 'FP': 40, 'FN': 50},
            0.9: {'TP': 50, 'TN': 140, 'FP': 42, 'FN': 50}
        }
        result = find_best_threshold(threshold_data)
        assert result is None

    # Handles typical threshold data with valid TP and FN values
    def test_handles_typical_threshold_data(self):
        threshold_data = {
            0.1: {'TP': 90, 'TN': 100, 'FP': 10, 'FN': 10},
            0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': 15},
            0.3: {'TP': 80, 'TN': 110, 'FP': 20, 'FN': 20},
            0.4: {'TP': 78, 'TN': 115, 'FP': 22, 'FN': 22},
            0.5: {'TP': 70, 'TN': 120, 'FP': 30, 'FN': 30},
            0.6: {'TP': 68, 'TN': 125, 'FP': 32, 'FN': 32},
            0.7: {'TP': 65, 'TN': 130, 'FP': 35, 'FN': 35},
            0.8: {'TP': 60, 'TN': 135, 'FP': 40, 'FN': 40},
            0.9: {'TP': 58, 'TN': 140, 'FP': 42, 'FN': 42}
        }
        result = find_best_threshold(threshold_data)
        assert result == 0.1

    # Ignores thresholds with missing TP or FN values
    def test_ignores_missing_values(self):
        threshold_data = {
            0.1: {'TP': 90, 'TN': 100, 'FP': 10},
            0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': 15},
            0.3: {'TP': 80, 'TN': 110, 'FP': 20, 'FN': 20},
            0.4: {'TP': 78, 'TN': 115, 'FP': 22, 'FN': 22},
            0.5: {'TP': 70, 'TN': 120, 'FP': 30, 'FN': 30},
            0.6: {'TP': 68, 'TN': 125, 'FP': 32, 'FN': 32},
            0.7: {'TP': 65, 'TN': 130, 'FP': 35, 'FN': 35},
            0.8: {'TP': 60, 'TN': 135, 'FP': 40, 'FN': 40},
            0.9: {'TP': 58, 'TN': 140, 'FP': 42}
        }
        result = find_best_threshold(threshold_data)
        assert result == None

    # Ignores thresholds with non-numeric TP or FN values
    def test_ignores_non_numeric_values(self):
        threshold_data = {
            0.1: {'TP': 90, 'TN': 100, 'FP': 10, 'FN': 10},
            0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': 15},
            0.3: {'TP': 80, 'TN': 110, 'FP': 20, 'FN': 20},
            0.4: {'TP': 78, 'TN': 115, 'FP': 22, 'FN': 22},
            0.5: {'TP': 70, 'TN': 120, 'FP': 30, 'FN': 30},
            0.6: {'TP': 68, 'TN': 125, 'FP': 32, 'FN': 32},
            0.7: {'TP': 65, 'TN': 130, 'FP': 35, 'FN': 35},
            0.8: {'TP': 60, 'TN': 135, 'FP': 40, 'FN': 40},
            0.9: {'TP': 'invalid', 'TN': 140, 'FP': 42, 'FN': 42}
        }
        result = find_best_threshold(threshold_data)
        assert result == 0.1

    # Handles cases where all thresholds have recall < 0.9
    def test_all_thresholds_below_0_9(self):
        threshold_data = {
            0.1: {'TP': 80, 'TN': 100, 'FP': 20, 'FN': 20},
            0.2: {'TP': 75, 'TN': 105, 'FP': 25, 'FN': 25},
            0.3: {'TP': 70, 'TN': 110, 'FP': 30, 'FN': 30},
            0.4: {'TP': 68, 'TN': 115, 'FP': 32, 'FN': 32},
            0.5: {'TP': 60, 'TN': 120, 'FP': 40, 'FN': 40},
            0.6: {'TP': 58, 'TN': 125, 'FP': 42, 'FN': 42},
            0.7: {'TP': 55, 'TN': 130, 'FP': 45, 'FN': 45},
            0.8: {'TP': 50, 'TN': 135, 'FP': 50, 'FN': 50},
            0.9: {'TP': 48, 'TN': 140, 'FP': 52, 'FN': 52}
        }
        result = find_best_threshold(threshold_data)
        assert result is None

    # Handles cases where multiple thresholds have recall >= 0.9
    def test_multiple_thresholds_recall_above_0_9(self):
        threshold_data = {
            0.1: {'TP': 90, 'TN': 100, 'FP': 10, 'FN': 10},
            0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': 15},
            0.3: {'TP': 80, 'TN': 110, 'FP': 20, 'FN': 20},
            0.4: {'TP': 78, 'TN': 115, 'FP': 22, 'FN': 22},
            0.5: {'TP': 70, 'TN': 120, 'FP': 30, 'FN': 30},
            0.6: {'TP': 68, 'TN': 125, 'FP': 32, 'FN': 32},
            0.7: {'TP': 65, 'TN': 130, 'FP': 35, 'FN': 35},
            0.8: {'TP': 60, 'TN': 135, 'FP': 40, 'FN': 40},
            0.9: {'TP': 90, 'TN': 140, 'FP': 42, 'FN': 10}
        }
        result = find_best_threshold(threshold_data)
        assert result == 0.1

    # Handles large threshold_data dictionaries efficiently
    def test_large_threshold_data(self):
        threshold_data = {
            0.1: {'TP': 90, 'TN': 100, 'FP': 10, 'FN': 10},
            0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': 15},
            0.3: {'TP': 80, 'TN': 110, 'FP': 20, 'FN': 20},
            0.4: {'TP': 78, 'TN': 115, 'FP': 22, 'FN': 22},
            0.5: {'TP': 70, 'TN': 120, 'FP': 30, 'FN': 30},
            0.6: {'TP': 68, 'TN': 125, 'FP': 32, 'FN': 32},
            0.7: {'TP': 65, 'TN': 130, 'FP': 35, 'FN': 35},
            0.8: {'TP': 60, 'TN': 135, 'FP': 40, 'FN': 40},
            0.9: {'TP': 58, 'TN': 140, 'FP': 42, 'FN': 42}
        }
        result = find_best_threshold(threshold_data)
        assert result == 0.1

    # Handles threshold_data with negative TP or FN values
    def test_handles_negative_values(self):
        threshold_data = {
            0.1: {'TP': -5, 'TN': 100, 'FP': 10, 'FN': 10},
            0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': -15},
            0.3: {'TP': 80, 'TN': 110, 'FP': -20, 'FN': 20},
            0.4: {'TP': 78, 'TN': -115, 'FP': 22, 'FN': 22},
            0.5: {'TP': 70, 'TN': 120, 'FP': -30, 'FN': -30},
            0.6: {'TP': -68, 'TN': 125, 'FP': 32, 'FN': 32},
            0.7: {'TP': 65, 'TN': -130, 'FP': 35, 'FN': 35},
            0.8: {'TP': -60, 'TN': 135, 'FP': 40, 'FN': -40},
            0.9: {'TP': -58, 'TN': -140, 'FP': -42, 'FN': -42}
        }
        result = find_best_threshold(threshold_data)
        assert result is None

    # Handles threshold_data with zero TP and FN values
    def test_handles_zero_tp_fn_values(self):
        threshold_data = {
            0.1: {'TP': 0, 'TN': 100, 'FP': 10, 'FN': 0},
            0.2: {'TP': 0, 'TN': 105, 'FP': 15, 'FN': 0},
            0.3: {'TP': 0, 'TN': 110, 'FP': 20, 'FN': 0},
            0.4: {'TP': 0, 'TN': 115, 'FP': 22, 'FN': 0},
            0.5: {'TP': 0, 'TN': 120, 'FP': 30, 'FN': 0},
            0.6: {'TP': 0, 'TN': 125, 'FP': 32, 'FN': 0},
            0.7: {'TP': 0, 'TN': 130, 'FP': 35, 'FN': 0},
            0.8: {'TP': 0, 'TN': 135, 'FP': 40, 'FN': 0},
            0.9: {'TP': 0, 'TN': 140, 'FP': 42, 'FN': 0}
        }
        result = find_best_threshold(threshold_data)
        assert result is None

    # Handles threshold_data with very high TP and FN values
    def test_handles_high_tp_fn_values(self):
        threshold_data = {
            0.1: {'TP': 9000, 'TN': 100, 'FP': 10, 'FN': 1000},
            0.2: {'TP': 8500, 'TN': 105, 'FP': 15, 'FN': 1500},
            0.3: {'TP': 8000, 'TN': 110, 'FP': 20, 'FN': 2000},
            0.4: {'TP': 7800, 'TN': 115, 'FP': 22, 'FN': 2200},
            0.5: {'TP': 7000, 'TN': 120, 'FP': 30, 'FN': 3000},
            0.6: {'TP': 6800, 'TN': 125, 'FP': 32, 'FN': 3200},
            0.7: {'TP': 6500, 'TN': 130, 'FP': 35, 'FN': 3500},
            0.8: {'TP': 6000, 'TN': 135, 'FP': 40, 'FN': 4000},
            0.9: {'TP': 5800, 'TN': 140, 'FP': 42, 'FN': 4200}
        }
        result = find_best_threshold(threshold_data)
        assert result == 0.1

    # Handles threshold_data with very low TP and FN values
    def test_handles_low_tp_fn_values(self):
        threshold_data = {
            0.1: {'TP': 1, 'TN': 100, 'FP': 10, 'FN': 1},
            0.2: {'TP': 2, 'TN': 105, 'FP': 15, 'FN': 2},
            0.3: {'TP': 3, 'TN': 110, 'FP': 20, 'FN': 3},
            0.4: {'TP': 4, 'TN': 115, 'FP': 22, 'FN': 4},
            0.5: {'TP': 5, 'TN': 120, 'FP': 30, 'FN': 5},
            0.6: {'TP': 6, 'TN': 125, 'FP': 32, 'FN': 6},
            0.7: {'TP': 7, 'TN': 130, 'FP': 35, 'FN': 7},
            0.8: {'TP': 8, 'TN': 135, 'FP': 40, 'FN': 8},
            0.9: {'TP': 9, 'TN': 140, 'FP': 42, 'FN': 9}
        }
        result = find_best_threshold(threshold_data)
        assert result == None

    # Correctly calculates recall for each threshold
    def test_calculate_recall_for_each_threshold(self):
        # Define the input data
        threshold_data = {
            0.1: {'TP': 90, 'TN': 100, 'FP': 10, 'FN': 10},
            0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': 15},
            0.3: {'TP': 80, 'TN': 110, 'FP': 20, 'FN': 20}
        }
    
        # Call the function under test
        result = find_best_threshold(threshold_data)
    
        # Add assertions here to check if recall is calculated correctly for each threshold
        assert result is not None

    # Compares recall values to find the highest one
    def test_find_highest_recall_value(self):
        # Define the input data
        threshold_data = {
            0.1: {'TP': 90, 'TN': 100, 'FP': 10, 'FN': 10},
            0.2: {'TP': 85, 'TN': 105, 'FP': 15, 'FN': 15},
            0.3: {'TP': 80, 'TN': 110, 'FP': 20, 'FN': 20}
        }
    
        # Call the function under test
        result = find_best_threshold(threshold_data)
    
        # Add assertions here to check if the highest recall value is correctly identified
        assert result is not None