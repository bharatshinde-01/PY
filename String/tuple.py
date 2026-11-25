tup = ( 1, 2, 5, 6)
print(type(tup))
a = ()  #empty tuple 
a1 = ( 1,)  # tuple wirh only one element nees a coma 
a2 = ( 1,2,3)    # tuple with more than one element 

        # tuple is immutable data type u cannot change after initilize once value 

# typle methonds 

# 1 . count()  a count (1) will return number of times 1 occures in a 

tupll = ( 1,2,3,4,5,6,1)
num = tupll.count(1)
print(num)

# 2. index(1) will return the indeex of first occurrence of 1 in a 

i = tupll.index(5)
print(i)

# 3. len() return length of tuple 
print("length of tuple :",len(tupll))