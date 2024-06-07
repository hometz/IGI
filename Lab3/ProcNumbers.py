import math
from functools import lru_cache


@lru_cache
def summarize(x, n):
    if n == 0:
        return 1
    return x ** n / math.factorial(n) + summarize(x, n - 1)


def series_expansion(x, eps):
    """
    Function to calculate the Taylor series for the exponential function.

    Parameters:
    x (float): The point at which the Taylor series is calculated.
    eps (float): The precision of the Taylor series calculation.

    Returns:
    result (float): The approximate value of the exponential function at point x.
    n (int): The number of iterations needed to achieve the specified precision.
    """
    try:
        result = n = diff = 0
        for n in range(0, 500):
            result += x ** n / math.factorial(n)

            if result - diff < eps:
                break

            diff = result

        return x, result, n, eps
    except ValueError:
        print("Incorrect input")
        return


def summarize_every_second():
    """
    Function to calculate the sum of every second number entered by the user.

    Returns:
    summary (int): The sum of every second number entered by the user.
    """
    number = summary = n = 0
    while True:
        try:
            while True:
                number = int(input("Number: "))

                if number == 1:
                    break

                n += 1

                if n % 2 == 0:
                    summary += number

            return summary

        except ValueError:
            print("Incorrect input, enter last number again: ")
            continue
