"""Functions for preprocessing"""

def label_map(y):
    """
    Converts string labels to integers
    """
    if y=="functional":
        return 2
    elif y=="functional needs repair":
        return 1
    else:
        return 0
    

def isNan(num):
    """
    Function to test for Nan. Returns True for NaNs, False otherwise.
    """
    return num != num

