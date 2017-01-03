from timeit import default_timer as timer

def counting_sundays(day, years, day_of_week):
	all_years = years
	all_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	all_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

	#[year, month, day]
	all_day_profiles = []
	day_counter = 7
	for i in all_years:
		for j in all_months:
			if j in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
				for k in range(1, 32):
					all_day_profiles.append([k, j, i, all_days[day_counter % 7]])
					day_counter += 1
			elif j in ['April', 'June', 'September', 'November']:
				for k in range(1, 31):
					all_day_profiles.append([k, j, i, all_days[day_counter % 7]])
					day_counter += 1
			elif i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
				for k in range(1, 30):
					all_day_profiles.append([k, j, i, all_days[day_counter % 7]])
					day_counter += 1
			else:
				for k in range(1, 29):
					all_day_profiles.append([k, j, i, all_days[day_counter % 7]])
					day_counter += 1
	num_days = 0
	for d in all_day_profiles:
		if d[0] == day and d[3] == day_of_week and 1901 <= d[2] <= 2000:
			num_days += 1
	return num_days

start = timer()
print(counting_sundays(1, range(1901, 2001), 'Sunday'))
end = timer()
print("Time: ", end - start)