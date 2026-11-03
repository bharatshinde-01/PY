# A) Write a python script to find the repeated items of a tupl

t = (10,20,30,10,40,10,20)
print("Repeated items are :")
for i in t :
    if t.count(i):
        print(i)
# tup = tuple(input("Enter numbers :").split())
tup = tuple(map(int ,input("Enter numbers :").split()))
print(tup)