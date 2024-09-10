import doctest
from multiply import multiply_two_numbers  # Byt ut 'multiply' med ditt moduls namn

def run_doctests():
    doctest.testmod()

if __name__ == "__main__":
    run_doctests()
