import pytest
from functions import *

# =========================
# DATA STRUCTURES
# =========================

def test_split_coordinates():
    assert split_coordinates([(1,2),(3,4)]) == ([1,3],[2,4])

def test_count_occurrences():
    assert count_occurrences(["a","b","a"]) == {"a":2,"b":1}

def test_common_elements():
    assert common_elements([1,2,3],[2,3,4]) == {2,3}

def test_remove_duplicates():
    assert remove_duplicates([1,2,2,3]) == [1,2,3]


# =========================
# DATA MANIPULATION
# =========================

def test_square_evens():
    assert square_evens([1,2,3,4]) == [4,16]

def test_sort_by_length():
    assert sort_by_length(["apple","hi"]) == ["hi","apple"]

def test_filter_students():
    assert filter_students({"Ann":40,"Bob":60}) == {"Bob":60}

def test_flatten_once():
    assert flatten_once([1,[2,3],4]) == [1,2,3,4]


# =========================
# RECURSION
# =========================

def test_sum_numbers():
    assert sum_numbers(4) == 10

def test_reverse_string():
    assert reverse_string("cat") == "tac"

def test_count_digits():
    assert count_digits(123) == 3

def test_factorial():
    assert factorial(4) == 24


# =========================
# STRING FORMATTING
# =========================

def test_greet_user():
    assert greet_user("Ann",20) == "Hello Ann, you are 20 years old."

def test_format_price():
    assert format_price(45) == "R45.00"

def test_format_table():
    result = format_table(["Ann"], [50])
    assert "Ann" in result and "50" in result

def test_format_email():
    assert format_email("ann","gmail.com") == "ann@gmail.com"