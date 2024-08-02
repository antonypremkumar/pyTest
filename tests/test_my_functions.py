import pytest
import src.my_functions as my_fuctions

def test_add():
    result = my_fuctions.add(number_one=1, number_two=4)
    assert result == 5

def test_divide():
    result = my_fuctions.divide(number_one=10, number_two=5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_fuctions.divide(number_one=10, number_two=0)

def test_add_strings():
    result = my_fuctions.add(number_one="i like ", number_two="burgers")
    assert result == "i like burgers"
