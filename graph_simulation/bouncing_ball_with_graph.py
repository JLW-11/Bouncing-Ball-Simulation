import time
import matplotlib
matplotlib.use('TkAgg')  # Ensure Tkinter backend for rendering graphs
import matplotlib.pyplot as plt

# Set the initial position and velocity
y_pos = 200  # Initial y position (starts above ground)
y_velocity = 0  # Initial velocity (stationary)
gravity = -0.03  # Gravity (negative to simulate downward motion)
ground_level = 0  # Ground level (below the starting point)

# Initialize lists to store data for plotting
time_steps = []
y_positions = []

# Initialize time
current_time = 0
time_step = 0.02  # 20 ms for each time step

# Main loop to simulate the bouncing ball
while current_time < 30:  # Run the simulation for 10 seconds
    # Update velocity and position
    y_velocity += gravity  # Simulate gravity (pull down)
    y_pos += y_velocity  # Update the ball's position

    # Bounce the ball when it hits the ground
    if y_pos <= ground_level:
        y_pos = ground_level  # Stop at ground level
        y_velocity = -y_velocity * 0.8  # Reverse velocity with energy loss (bounce)

    # Record the time and ball position for the graph
    time_steps.append(current_time)
    y_positions.append(y_pos)

    # Print the ball's current position (for testing purposes)
    print(f"Time: {current_time:.2f} s, Ball position: {y_pos}")

    # Pause for a short moment to simulate real-time
    time.sleep(time_step)

    # Increment the current time
    current_time += time_step

# Ensure the plot is displayed after the simulation
plt.plot(time_steps, y_positions)
plt.title("Bouncing Ball Simulation")
plt.xlabel("Time (s)")
plt.ylabel("Ball Position (y_pos)")
plt.grid(True)

# Show the plot
plt.show()
