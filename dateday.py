Date=input("Enter the date:")
date=int(Date.split("/")[0])
starting_day=input("Enter the day:")
weekdays = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
idx=weekdays.index(starting_day)
day=date%7
final_day=(day+idx) % 7
print(weekdays[final_day])