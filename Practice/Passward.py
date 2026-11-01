import random 
import string
letter = string.ascii_letters
passward = ""
for i in range (8):
    passward = passward + random.choice(letter)
print("Passward generated :",passward)
