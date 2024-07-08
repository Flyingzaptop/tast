def find_longest_word(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            longest_word = max(words, key=len)
        return longest_word
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    filename = 'input.txt'
    longest_word = find_longest_word(filename)
    print(f"The longest word is: {longest_word}")
