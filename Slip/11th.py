t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)
sum = []
for i in range (len(t1)):
    temp =  t1[i] + t2[i] + t3[i]
    sum.append(temp)
print("Sum of tuple is :",sum)