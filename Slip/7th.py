#  Write a Python script to display datetime in various formats using datetime module
# a. Current date and time
# b. Month of year
# c. Week number of the year
# d. Day of year
# e. Day of the month
import datetime
now = datetime.datetime.now()
print("Cureent date and time :",now)
print("Current month of the year :",now.strftime("%B"))
print("Current week of the year :",now.strftime("%W"))
print("Day of year :",now.strftime("%j"))
print("day of the month :",now.strftime("%D"))