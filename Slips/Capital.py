str = input("Enter your string :")
count = 0
lower = 0 

for ch in str:
 if ch.isupper():
   count +=1
   print("this is run")
 elif ch.islower():
   lower +=1

print("Upper case latters is :",count)
print("Lower case latters is :",lower)
