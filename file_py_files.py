from time import localtime

activities = {
	
	8 : "Good Morning",
	9 : "Ready to go to Office",
	10 : "Attend Meeting",
	11 : "Code",
	12 : "Plan the meeting",
	13 : "lunch",
	14: "Work till 6",
	15:"Come back home",
	16:"have dinner",
	17: "Spend time with family and sleep"
}

# time_now = localtime()
# print (time_now)
# hour = time_now.tm_month
# print (hour)

hour =  int (input("Enter the hour you want :"))
print (hour)

for activity in sorted(activities.keys()):
	if hour == activity:
		print (activities[activity])
		break

else :
	print ("Unknown , AFK or Sleeping")