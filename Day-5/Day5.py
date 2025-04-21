# String Methods... Why are there so many?

Name = "my name is Charlie!!!"

x = Name.capitalize() # Capitalizes first character
print(x)

x = Name.count('a') # Check all instances of a character or word in the string
print(x)

x = Name.index('i') # Finds where first instance of character occurs
print(x)

Name = " ".join(Name) # Creates a space between each character of name
print(Name)

Name = Name.replace("a", "O") # Replaces all instances of characters or words with whatever you want
print(Name)

Name = Name.split() # Splits each word into an element in a list
print(Name) 

# There are so many more I found on https://www.w3schools.com/python/python_ref_string.asp. I found these the most interesting 
