def process_list():
    """
    Function to process a list of numbers entered by the user. It calculates the minimum absolute value,
    and the sum of elements located between the first and last positive elements.

    Returns:
    None
    """
    raw_input = input("Enter list items separated by spaces: ")
    elements = raw_input.split()

    try:
        float_elements = [float(el) for el in elements]
    except ValueError:
        print("Incorrect data entered. Please enter numbers.")
        return

    print("Your list: ", float_elements)

    min_abs_element = min(float_elements, key=abs)
    print("Minimum modulo list element: ", min_abs_element)

    positive_indices = [i for i, el in enumerate(float_elements) if el > 0]
    if len(positive_indices) >= 2:
        first_positive, last_positive = positive_indices[0], positive_indices[-1]
        sum_between = sum(float_elements[first_positive+1:last_positive])
        print("Sum of list elements located between the first and last positive elements: ", sum_between)
    else:
        print("There are less than two positive elements in the list.")