#  Write a Python script to display datetime in various formats using datetime module
# a. Current date and time
# b. Month of year
# c. Week number of the year
# d. Day of year
# e. Day of the month
import datetime
now = datetime.datetime.now()
print("Current Date and Time :",now)
print("Current Month of Year :",now.strftime("%B"))
print("Current Week number of year :",now.strftime("%W"))
print("Current Day of year :",now.strftime("%j"))
print("Cureent Day of the month is :",now.strftime("%d"))

