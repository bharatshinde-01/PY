t = tuple(map(int,input("Enter tuple numbers :").split()))

for i in t:
    if t.count(i) > 1 :
        print (i)
        