# =========================
# DATA STRUCTURES (4)
# =========================

def split_coordinates(coords):
    """
    Given a list of (x, y) tuples, return two lists:
    one containing all x values and one containing all y values.

    Example:
    [(1, 2), (3, 4)] -> ([1, 3], [2, 4])
    """
    x_coord = []
    y_coord = []
    for i, j in coords:
        x_coord.append(i)
        y_coord.append(j)
    return x_coord, y_coord
# print(split_coordinates([(1,2),(3,4)]))


def count_occurrences(items):
    """
    Return a dictionary counting how many times each element appears.

    Example:
    ["a", "b", "a"] -> {"a": 2, "b": 1}
    """
    counts = {}

    for item in items:
        counts[item] = counts.get(item, 0) + 1

    return counts
# print(count_occurrences(["a","b","a"]))



def common_elements(a, b):
    """
    Return a set of elements that appear in both lists.

    Example:
    [1,2,3], [2,3,4] -> {2,3}
    """
    elements = set()
    for i in a:
        for x in b:
            if i == x:
                elements.add(i)
    return elements
# print(common_elements([1,2,3],[2,3,4]))


def remove_duplicates(lst):
    """
    Return a list with duplicate elements removed.

    Example:
    [1,2,2,3] -> [1,2,3]
    """
    duplicates = set()
    for l in lst:
        duplicates.add(l)
    return list(duplicates)
# print(remove_duplicates([1,2,2,3]))



# =========================
# DATA MANIPULATION (4)
# =========================

def square_evens(nums):
    """
    Return a list of squared values of even numbers only.

    Example:
    [1,2,3,4] -> [4,16]
    """
    evens = []
    for num in nums:
        x = num ** 2 
        if x % 2 == 0:
            evens.append(x)
    return evens
# print(square_evens([1,2,3,4]))


def sort_by_length(words):
    """
    Return the list of words sorted by their length.

    Example:
    ["hi", "apple"] -> ["hi", "apple"]
    """
    return sorted(words,key=len)
# print(sort_by_length(["apple","hi"]))


def filter_students(data):
    """
    Return a dictionary with students who scored >= 50.

    Example:
    {"Ann":40, "Bob":60} -> {"Bob":60}
    """
    
    for key,value in data.items():
        if value >= 50:
            return {key:value}
# print(filter_students({"Ann":40, "Bob":60}))



def flatten_once(lst):
    """
    Flatten a list by ONE level only.

    Example:
    [1, [2,3], 4] -> [1,2,3,4]
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result
# print(flatten_once([1,[2,3],4]))


# =========================
# RECURSION (4)
# =========================
def sum_numbers(n):
    """
    Return the sum from 1 to n using recursion.

    Example:
    4 -> 10
    """
    if n <= 0:
        return 0
    return n + sum_numbers(n - 1)
# print(sum_numbers(4))


def reverse_string(s):
    """
    Return the reversed string using recursion.

    Example:
    "cat" -> "tac"
    """
    if s == "":
        return ""
    return s[-1] + reverse_string(s[:-1])
# print(reverse_string("cat"))


def count_digits(n):
    """
    Return the number of digits in n using recursion.

    Example:
    123 -> 3
    """
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
# print(count_digits(123))
    

def factorial(n):
    """
    Return n! (factorial) using recursion.

    Example:
    4 -> 24
    """
    if n == 1:
        return 1
    return n * factorial(n-1)
# print(factorial(4))


# =========================
# STRING FORMATTING (4)
# =========================

def greet_user(name, age):
    """
    Return: "Hello <name>, you are <age> years old."
    """
    return f"Hello {name}, you are {age} years old."
# print(greet_user("Alice", 30))


def format_price(price):
    """
    Format price to 2 decimal places with 'R'.

    Example:
    45 -> "R45.00"
    """
    return f"R{price:.2f}"
# print(format_price(45))


def format_table(names, scores):
    """
    Return a formatted table string:

    Name   | Score
    --------------
    Ann    | 50
    """
    table = "Name   | Score\n--------------\n"
    for name, score in zip(names, scores):
        table += f"{name:<6} | {score}\n"
    return table
# print(format_table(["Ann","Bob"],[50,60]))

def format_email(name, domain):
    """
    Return a formatted email address:

    Example:
    ("ann", "gmail.com") -> "ann@gmail.com"
    """
    return f"{name}@{domain}"
# print(format_email("slindile","gmail.com"))



