import datetime
d = int (input("Enter day of birth :"))
m = int (input("Enter month of birth :"))
y = int (input("Enter year of birth :"))

if (m <1 or m > 12):
    print("Invalid month ! " )
else :
    birth = datetime.date(y , m, d)
    today = datetime.date.today()
    age =  today.year - birth.year
    print("Your age is this :",age)
