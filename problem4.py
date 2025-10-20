"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """
    Count total words in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of words
    """
    # TODO: Open file and count words
    # Hint: Use split() to separate words
    pass
    total_words = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                total_words += len(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return 0
    return total_words




def count_lines(filename):
    """
    Count total lines in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of lines
    """
    # TODO: Open file and count lines
    total_lines = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                total_lines += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return 0
    return total_lines


def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.

    Args:
        filename (str): Name of the file to analyze
        include_spaces (bool): Whether to include spaces in count

    Returns:
        int: Total number of characters
    """
    # TODO: Open file and count characters
    # If include_spaces is False, don't count spaces
    total_characters = 0
    try:    
        with open(filename, 'r') as file:
            for line in file:
                if include_spaces:
                    total_characters += len(line)
                else:
                    total_characters += len(line.replace(" ", "").replace("\n", ""))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return 0
    return total_characters 


def find_longest_word(filename):
    """
    Find and return the longest word in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        str: The longest word found
    """
    # TODO: Find the longest word
    # Hint: You might need to remove punctuation
    longest_word = ""
    import string
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Remove punctuation
                    clean_word = word.strip(string.punctuation)
                    if len(clean_word) > len(longest_word):
                        longest_word = clean_word
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return ""
    return longest_word 


def word_frequency(filename):
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        dict: Dictionary with words as keys and frequencies as values
    """
    import string

    frequency = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Clean word
                    clean_word = word.strip(string.punctuation).lower()
                    if clean_word:
                        frequency[clean_word] = frequency.get(clean_word, 0) + 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return {}   


    # TODO: Open file
    # TODO: Read all words
    # TODO: Convert to lowercase
    # TODO: Remove punctuation (use string.punctuation)
    # TODO: Count frequency of each word

    return frequency


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()