# Write python program to generate a random password with upper and lower
# case letters
import random , string
latters = string.ascii_letters
password = ""
for i in range(8):
    password = password + random.choice(latters)
print("Random Passward:",password)

