from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

# Create dice
dice = Dice()

# Modeling series of dice rolling with saving results into list
results = []
for roll_num in range(1_000):
    results.append(dice.roll())

# Result Analysis
frequencies = []
for value in range(1, dice.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Result Visualisation
x_values = list(range(1, dice.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config,
    yaxis=y_axis_config
)
offline.plot(
    {'data':data, 'layout':my_layout},
    filename='image/d6.html'
)

print(frequencies)