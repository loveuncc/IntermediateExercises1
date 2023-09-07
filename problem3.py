def count_letters(s):
    s = s.lower()
    letter_count = {}
    for char in s:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

user_input = input("Enter a string: ")
print(count_letters(user_input))

