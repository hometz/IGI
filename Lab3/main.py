import math

import ProcList
import ProcNumbers
import ProcString

while True:
    """
    Main function to interact with the user. It prompts the user to enter a task number and calls the corresponding function.
    The loop continues until the user enters '0' as the task number.
    """
    try:
        func_number = int(input("Enter the number of task you would like to start (0 to finish): "))

        if func_number == 0:
            break

        elif func_number == 1:
            """
            Task 1: Calculate the Taylor series for the exponential function.
            """

            res = ProcNumbers.series_expansion(float(input("Enter x: ")), float(input("Enter eps: ")))

            print("x = ", res[0], "\ne^x = ", res[1], "\nn = ", res[2],
                  "\nMath F(x) = ", math.exp(res[0]), "\neps = ", res[3])
            
        elif func_number == 2:
            """
            Task 2: Calculate the sum of every second number entered by the user.
            """
            print(ProcNumbers.summarize_every_second())

        elif func_number == 3:
            """
            Task 3: Count the number of words in a text that start with a consonant.
            """
            print("Number of words starting with consonants: ",
                  ProcString.count_words_starting_with_consonant(input("Enter text: ")))

        elif func_number == 4:
            """
            Task 4: Process a text. It calculates the number of words with minimal length,
            lists the words followed by a period, and finds the longest word ending with 'r'.
            """
            ProcString.process_text(input("Enter text: "))

        elif func_number == 5:
            """
            Task 5: Process a list of numbers entered by the user. It calculates the minimum absolute value,
            and the sum of elements located between the first and last positive elements.
            """
            ProcList.process_list()

    except Exception:
        print("Incorrect input")
        continue
