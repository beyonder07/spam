def find_unique_non_repeating_chars(s):
    stack = []
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            stack.append(char)
    
    return ''.join(stack)

user_input = input("Enter a string: ")
result = find_unique_non_repeating_chars(user_input)
print("Unique non-repeating characters:", result)