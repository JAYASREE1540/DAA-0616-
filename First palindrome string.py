def first_palindrome(strings):
    for s in strings:
        if s == s[::-1]:  # Check if the string is a palindrome
            return s
    return "No palindrome found"

# Example usage
strings = ["apple", "level", "banana", "radar"]
result = first_palindrome(strings)
print("First palindrome string:", result)
