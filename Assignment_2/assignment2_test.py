import pytest
from assignment2 import remainder_when_divided_by_3

class TestRemainderWhenDividedBy3:

    # Input binary string '1101' returns 1
    def test_binary_string_1101_returns_1(self):
        assert remainder_when_divided_by_3('1101') == 1

    # Input empty string returns 0
    def test_empty_string_returns_0(self):
        with pytest.raises(ValueError):
            remainder_when_divided_by_3('') == 0

    # Input binary string '1110' returns 2
    def test_binary_string_1110_returns_2(self):
        assert remainder_when_divided_by_3('1110') == 2

    # Input binary string '1111' returns 0
    def test_binary_string_1111_returns_0(self):
        assert remainder_when_divided_by_3('1111') == 0

    # Input binary string '0' returns 0
    def test_input_binary_string_0_returns_0(self):
        assert remainder_when_divided_by_3('0') == 0

    # Input binary string '1' returns 1
    def test_input_binary_string_1_returns_1(self):
        assert remainder_when_divided_by_3('1') == 1

    # Input binary string with all '0's returns 0
    def test_binary_string_all_zeros_returns_0(self):
        assert remainder_when_divided_by_3('0000') == 0

    # Input binary string with all '1's returns 0
    def test_input_all_ones_returns_0(self):
        assert remainder_when_divided_by_3('1111') == 0

    # Input binary string with leading '0's returns correct remainder
    def test_binary_string_with_leading_zeros_returns_correct_remainder(self):
        assert remainder_when_divided_by_3('0001101') == 1

    # Input binary string with non-binary characters raises an error
    def test_non_binary_input_raises_error(self):
        with pytest.raises(ValueError):
            remainder_when_divided_by_3('1102')

    # Input binary string with very large length is processed correctly
    def test_large_binary_string_returns_correct_remainder(self):
        assert remainder_when_divided_by_3('110110110110110110110110110110') == 0

    # Input binary string with only one character is processed correctly
    def test_single_character_binary_string(self):
        assert remainder_when_divided_by_3('0') == 0
        assert remainder_when_divided_by_3('1') == 1

    # Input binary string with trailing '0's returns correct remainder
    def test_binary_string_with_trailing_zeros_returns_correct_remainder(self):
        assert remainder_when_divided_by_3('1101') == 1