#Create a program that asks the user to enter their name and their age.
 #Print out a message that will tell them the year that they will turn 95 years old.



# importing the data and time module
import datetime

# taking the age as input from the user 
age=int(input("please enter the age: "))

#extracting the current date and time
date=datetime.datetime.today()
print("Date: "date)

#Extracting the curent year
year=date.year

#sub the age getting the year of birth and then adding  95 to it
x=str((year-age)+95)


print("Year in which you will celebrate your 95th birtday is: "+ x )

