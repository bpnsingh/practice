'''
"""
Exercise 5.1.
The time module provides a function, also named time, that returns the current
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a
reference point. On UNIX systems, the epoch is 1 January 1970.
>>> import time
>>> time.time()
1437746094.5735958
Write a script that reads the current time and converts it to a time of day
in hours, minutes, and seconds, plus the number of days since the epoch.
"""
'''


import  time



def get_date_and_time(epoch_time):
	'''
	days= total_time//60*60*24
	remaing_time= epoch_time%(60*60*24)
	number_hrs=remaing_time//60*60
	remainig_minutes=remaing_time%60*60
	minutes=remainig_minutes//60
	seconds=minutes%60

	'''	
	number_of_Seconds_in_day = 60*60*24
	days = epoch_time//number_of_Seconds_in_day
	remaing_time = epoch_time%number_of_Seconds_in_day
	number_hrs = remaing_time//(60*60)
	remainig_minutes = remaing_time%(60*60)
	minutes = remainig_minutes//60
	seconds = remainig_minutes%60
	return days,number_hrs,minutes,seconds

if __name__ == '__main__':
	current_time= time.time()
	a,b,c,d = get_date_and_time(current_time)
	lista=[a,b,c,d]
	print (map(int(),lista))
	# print (listb)

	print (f"days:{a}\nhours:{b}\nminutes:{c}\nSeconds:{d}")


