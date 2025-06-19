import matplotlib.pyplot as plt

# Define logistic map function
def logistic_map(x, r):
    return r * x * (1 - x)


# Parameters
r = 3.9 # Value leads to chaos (must be between -3.57 and 4)
iterations = 100

# Two initial conditions very close to each other
x1 = 0.5000
x2 = 0.5001

# Store results
values1 = [x1]
values2 = [x2]

# Iterate the map
for i in range(iterations):
    x1 = logistic_map(x1, r)
    x2 = logistic_map(x2, r)
    values1.append(x1)
    values2.append(x2)


# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(values1, label='x0 = 0.5000')
plt.plot(values2, label='x0 = 0,5001')
linestyle='dashed'
plt.title('Chaos in the Logistic Map (r=3.9)')
plt.xlabel('Iteration')
plt.ylabel('x-value')
plt.legend()
plt.grid(True)
plt.show()