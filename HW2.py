# Frequency Counter Program

def char_frequency(string):
    frequency = {}
    for char in string:
        if char.isalpha():  # Only count alphabetic characters
            char = char.lower()  # Convert to lowercase for uniformity
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

input_string = input("Enter string: ")
result = char_frequency(input_string)

for char, count in result.items():
    print(f"{char}={count}", end=", ")
