def add_two_small_numbers(num1, num2):
    """
    Add two numbers, but raise an exception if any number is greater than 100.
    
    >>> add_two_small_numbers(50, 30)
    80
    >>> add_two_small_numbers(150, 30)
    Traceback (most recent call last):
        ...
    ValueError: Both numbers must be smaller than or equal to 100
    """
    if num1 > 100 or num2 > 100:
        raise ValueError("Both numbers must be smaller than or equal to 100")
    return num1 + num2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
