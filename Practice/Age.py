from datetime import Calendar
date = int (input("Enter your birth date :"))
month = int (input("Enter your birht month :"))
year = int(input("Enter your birth year :"))

today = date.today()

birthdate = date(date,month,year)
