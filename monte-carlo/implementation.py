import random

def monte_carlo():
    # instantiate variables
    num_circ = 0
    num_square = 0
    NUM_ITERATIONS = 1000

    for i in range(NUM_ITERATIONS**2):
        # randomly generated x and y values from a uniform distribution (unit circle is between -1 to 1)
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # distance between (x, y) and the origin
        d = (x**2) + (y**2)
        
        # check if (x, y) lies inside teh cricle
        if d <= 1:
            num_circ += 1
        num_square += 1

    # estimate the value of pi by multiplying 4 by ratio of number of points inside circle to total number of points (number of points inside square)
    return 4 * num_circ / num_square


pi = monte_carlo()
print(pi)