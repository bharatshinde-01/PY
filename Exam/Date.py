import datetime
now = datetime.datetime.now()
print("Current Date and time :", now)
print("Current Month of year :",now.strftime("%B"))
print("Current Week number of year :",now.strftime("%W"))
print("Current Day of year :",now.strftime("%j"))
print("Current dya of month :",now.strftime("%d"))