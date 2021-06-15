#!/usr/bin/env python3

#check what year it is and check whether or not it is a leap year

year =int(input("What year is it? "))

if year % 4  == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print("Leap year")
		else:
			print("Not leap year")
	else:
		print("Leap year")
else:
	print("Not Leap year😎")
	