import matplotlib.pyplot as plt

from random_walk import RandomWalk

# New Random walks builds while program is active
while True:
    # Build random walk
    rw = RandomWalk(num_points=50_000)
    rw.fill_walk()

    # Plotting points to diagram
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors='none',
        s=1
    )

    # Select first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(
        rw.x_values[-1],
        rw.y_values[-1],
        c='red',
        edgecolors='none',
        s=100
    )

    # Delete axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.savefig(fname='image/random_walk.png', bbox_inches='tight')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
