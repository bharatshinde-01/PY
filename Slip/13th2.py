# str = input("Enter Sting :")
# remove = ""
# for i in range (len(str)):
#     if i % 2 == 0:
#      remove = remove + str[i]

# print(remove)  
def remove (str):
    result = ""
    for i in range (len(str)):
        if i % 2 != 0:
            result = result + str[i]
    return result 

name = input("Enter String :")
print("Original Stirng :",name)
print("New Stirng ",remove(name))
