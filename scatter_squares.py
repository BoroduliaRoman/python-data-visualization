from shutil import which

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-deep')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Setup title and axis labels
ax.set_title(label="Square Numbers", fontsize=24)
ax.set_xlabel(xlabel="Value", fontsize=14)
ax.set_ylabel(ylabel="Square of Value", fontsize=14)

# Setup tick label
ax.tick_params(axis='both', which='major', labelsize=14)

# Setup range for each axis
ax.axis([0, 1_100, 0, 1_100_000])

plt.savefig(fname='image/squares_plot.png', bbox_inches='tight')