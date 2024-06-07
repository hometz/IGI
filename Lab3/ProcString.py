consonants = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVxXzZ'


def count_words_starting_with_consonant(text):
    """
    Function to count the number of words in a text that start with a consonant.

    Parameters:
    text (str): The text to be processed.

    Returns:
    count (int): The number of words that start with a consonant.
    """

    try:
        words = text.split()
        count = sum(1 for word in words if word[0] in consonants)
        return count
    except ValueError:
        return


def process_text(text):
    """
    Function to process a text. It calculates the number of words with minimal length,
    lists the words followed by a period, and finds the longest word ending with 'r'.

    Parameters:
    text (str): The text to be processed.

    Returns:
    None
    """
    while True:
        try:
            words = text.replace(',', ' ').split()

            min_length = min(len(word) for word in words)
            min_length_words = [word for word in words if len(word) == min_length]
            print(f"Number of words with minimal length {min_length}: {len(min_length_words)}")

            dot_words = [word for word in words if word.endswith('.')]
            print("Words followed by a period:", ', '.join(dot_words))

            r_words = [word for word in words if word.endswith('r')]
            longest_r_word = max(r_words, key=len, default=None)
            print("Longest word ending with 'r':", longest_r_word)
            return

        except ValueError:
            print("Incorrect input")
            continue
