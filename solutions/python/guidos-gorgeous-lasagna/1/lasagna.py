"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    Parameters:
        number_of_layers (int): number of layers.

    Returns:
        int: The preparation bake time (in minutes).

    Function that takes the number of layers and multiplies it by 2 and returns how     long preparation time takes.
    """
    return 2 * number_of_layers
   

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time of cooking.

    Parameters:
        number_of_layers (int): number of layers added to the lasagne
        elapsed_bake_time (int): The number of minutes the lasagne has spent baking     in the oven already
        
    Returns:
        int: The total time (in minutes) you have been in the kitchen cooking.

    Function that takes the number_of_layers and elapsed_bake_time as arguments and     returns the total minutes you have been in the kitchen cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    
