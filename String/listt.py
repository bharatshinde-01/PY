    # Unlike String lists are mutable than can u changes 
    #A list can be indexed like a string 

friends = ["Apples", "Orange","Mayur"]
print(friends)
friends[1] = "Banana"
print (friends)

# Methods of lists 

# 1 . append() 

friends.append("Bharat")
print(friends)

# 2 . sort()
# print("Sort data ")
# friends.sort()
# print(friends)

# 3. reverse()

# print("Reverse list ")
# friends.reverse()
# print(friends)

# 4 . insert(2,8) adds 8 at the 3 index 

# print("Insert element ")
# friends.insert(3,"insert")
# print(friends)

# 5. pop(3) will delete element at index 2 and return its value 

# print("Pop element ")
# # delete = friends.pop(2)
# print(friends.pop(2))
# print(friends)

# 6. reverse(21) will remove 21 list form list 
print("Remove element :")
friends.remove("Apples")
print(friends)

