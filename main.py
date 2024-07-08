def find_longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
    return longest_word

if __name__ == "__main__":
    filename = 'input.txt'
    longest_word = find_longest_word(filename)
    print(f"The longest word is: {longest_word}")
