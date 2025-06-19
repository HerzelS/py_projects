import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Define the Lorenz system
def lorenz(t, state, sigma=10.0, rho=28.0, beta=8/3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


# Time span
t_start = 0
t_end = 40
t_points = 10000
t = np.linspace(t_start, t_end, t_points)

# Initial condition
initial_state = [1.0, 1.0, 1.0]

# Solve ODE
sol = solve_ivp(lorenz, [t_start, t_end], initial_state, t_eval=t, args=(10, 28, 8/3))

# Ploting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111,
                     projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2], lw=0.5)

# Labels and title
ax.set_title('Lorenz Attractor',
             fontsize=16)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
plt.show()