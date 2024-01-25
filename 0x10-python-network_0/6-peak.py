def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    
    Args:
        list_of_integers (list): List of unsorted integers.
    
    Returns:
        int: Peak value in the list.
    """
    peak = list_of_integers[0]  # Initialize peak with the first element
    for num in list_of_integers:
        if num > peak:
            peak = num
    return peak
