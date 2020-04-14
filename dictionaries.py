# Create an empty dictionary
animal = dict()
# Add k/v pairs
animal["name"] = "Kevin"
animal["breed"] = "Bulldog"
animal["age"] = 5

# Create the dictionary with k/v pairs and assign to variable
animal = {
    "name": "Kevin",
    "breed": "Bulldog",
    "age": 5
}

for (key, value) in animal.items():
    print(f"{key}: {value}")

# Output
# name: Kevin
# breed: Bulldog
# age: 5

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["monkey"] = "noun. mammal that looks like your mom"
word_definitions["turtle"] = "noun. animal that looks like Mitch McConnell"
word_definitions["fuck"] = "noun, verb, adjective. most powerful word in the dictionary"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print("MONKEY", word_definitions["monkey"])
print("FUCK", word_definitions["fuck"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for word in word_definitions:
    print(f'The definition of {word} is {word_definitions[word]}')