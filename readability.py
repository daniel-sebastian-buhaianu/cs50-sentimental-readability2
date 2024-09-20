# Main program
def main():
    level = getGrade(getUserInput())

    if level <= 0:
        print("Before Grade 1")
    elif level >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {level}")

# Asks user for input with basic input validation
def getUserInput() -> str:
    while True:
        userInput = input("Text: ")
        if userInput.strip():  # Ensure the input isn't empty
            return userInput
        print("Please provide non-empty text.")

# Computes grade using Coleman-Liau formula
def getGrade(text: str) -> int:
    letters = countLetters(text)
    words = countWords(text)
    sentences = countSentences(text)

    # Calculate averages per 100 words
    L = letters / words * 100
    S = sentences / words * 100

    # Coleman-Liau index formula
    index = 0.0588 * L - 0.296 * S - 15.8

    return round(index)

# Counts number of letters in a text
def countLetters(text: str) -> int:
    # Use a generator expression to count alphabetic characters
    return sum(1 for char in text if char.isalpha())

# Counts number of words in a text
def countWords(text: str) -> int:
    # Split by whitespace and count words
    return len(text.split())

# Counts number of sentences in a text
def countSentences(text: str) -> int:
    # Count punctuation marks that usually indicate end of a sentence
    return sum(1 for char in text if char in ".!?")

# Runs the program
if __name__ == "__main__":
    main()

