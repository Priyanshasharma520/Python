#Create a program that asks the user to enter their name and their age.
 #Print out a message that will tell them the year that they will turn 95 years old.





import datetime

age=int(input("please enter the age: "))
date=datetime.datetime.today()
year=date.year
x=str((year-age)+95)
print("Year in which you will celebrate your 95th birtday is: "+ x )
