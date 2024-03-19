#Character Frequency Counter

def count_characters(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

string = input("Enter a string: ")
print("Character frequency:")
frequency = count_characters(string)
for char, count in frequency.items():
    print(f"{char}: {count}")