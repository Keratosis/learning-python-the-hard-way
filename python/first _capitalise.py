
# def solve(x):
#     return x.title()

# y = solve("chris martin")
# print(y)

def solve(s):
    words = s.split()  # Split the string into individual words
    capitalized_words = [word.capitalize() for word in words]  # Capitalize each word
    result = ' '.join(capitalized_words)  # Join the words back into a string
    return result

# Example usage:
input_string = "1 w 2 r 3g"
y = solve("chris martin")
capitalized_string = solve(input_string)
capitalized_string1 = solve(y)

print(capitalized_string)
print(capitalized_string1)
    
