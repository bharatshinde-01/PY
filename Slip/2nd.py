# ) Write Python program to take accept your birthdate and output your age. 
import datetime 
date = int(input("Enter day of birth :"))
month = int(input("Enter month of birht :"))
year = int(input("Enter year of birth :"))
if month < 1 or month > 12:
    print("invalid month !")
else :
    birth = datetime.date(year,month,date)
    today = datetime.date.today()
    age = today.year -  birth.year
    print("Your ages is :",age)

now = datetime.date.day
print("today date is ❤️ ")