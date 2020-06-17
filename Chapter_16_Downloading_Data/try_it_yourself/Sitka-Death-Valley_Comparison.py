import csv
from matplotlib import pyplot as plt 
from datetime import datetime

filename = 'death_valley_2014.csv'
filename2= 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)

	for index, column_header in enumerate(header_row):
		#print(index, column_header)
		pass

	dates, lows, highs = [],[], []

	for row in reader:
		try: 
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'missing data')
		else: 
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
			#print("lows " + str(len(lows)) + " highs " + str(len(highs)))
			

with open(filename2) as f2:
	reader2 = csv.reader(f2)
	header_row2 = next(reader2)
	#print(header_row)

	for index2, column_header2 in enumerate(header_row2):
		#print(index2, column_header2)
		pass
	dates2, lows2, highs2 = [],[], []

	for row2 in reader2:
		try: 
			current_date2 = datetime.strptime(row2[0], "%Y-%m-%d")
			high2 = int(row2[1])
			low2 = int(row2[3])
			print('low ' + str(low2) + ' high ' + str(high2))
		except ValueError:
			print(current_date2, 'missing data')
		else: 
			dates2.append(current_date2)
			highs2.append(high2)
			lows2.append(low2)



	#print(highs)


#plot data.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=1.0)
plt.plot(dates, lows, c='blue', alpha=1.0)
plt.plot(dates2, highs2, c='green', alpha=1.0)
plt.plot(dates2, lows2, c='purple', alpha=1.0)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.5)
plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=.5)
# Format plot 
plt.title("Comparison Death Valley and Sitka Temp Ranges 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("temperature (F)", fontsize =16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()














