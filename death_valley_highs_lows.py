import csv
from datetime import datetime

from matplotlib import pyplot as plt

def fahrenheit_to_celsius(fahrenheit: int) -> int:
    celsius = int((fahrenheit - 32) / 1.8)
    return celsius

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Reading dates, max and min temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = fahrenheit_to_celsius(int(row[4]))
            low = fahrenheit_to_celsius(int(row[5]))
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Data plotting to diagram
plt.style.use('seaborn-v0_8-paper')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatting diagram
plt.title(
    'Daily high and low temperatures - 2018\nDeath Valley, CA',
    fontsize=24
)
plt.xlabel('', fontsize=20)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=18)

plt.show()
