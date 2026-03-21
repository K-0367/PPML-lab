paragraph = input("Enter a paragraph: ")
words = paragraph.lower().split()

word_count = len(words)

palindrome_count = 0
palindrome_words = []

for word in words:
    clean_word = ''.join(char for char in word if char.isalnum())

    if clean_word == clean_word[::-1] and len(clean_word) > 1:
        palindrome_count += 1
        palindrome_words.append(clean_word)

print("Total number of words:", word_count)
print("Number of palindrome words:", palindrome_count)
print("Palindrome words:", palindrome_words)
