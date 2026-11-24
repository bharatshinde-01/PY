# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.
name = input("Enter your name :")
print("Good Afternoon , ",name)
print(f"Good Afternoon, {name}")

# 2.  Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''


                     #Strings are immutable which means that you cannot change them by running function on them 


letter = '''
Dear <|Name|>,
You are selected!
<|Date '''

print(letter.replace("<|Name|>","Bharat").replace("<|Date","24 jun 2030")) # that is called chaing 

# 3. Write a program to detect double space in a string.

name = "hhello iam Bharat  i am learing  python"
print(name.find("  "))

# 4. Replace the double space from problem 3 with single spaces

print(f"{name.replace("  ", " ")}")

# 5. Write a program to format the following letter using escape sequence
# characters.
letter = "Dear Harry, \n \t This python course is nice. Thanks!"
print(letter)



