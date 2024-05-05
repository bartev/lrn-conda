import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2*pi with a small interval
x_values = np.arange(0, 2 * np.pi, 0.1)

# Calculate corresponding y values for a sine wave
y_values = np.sin(x_values)

# Plot the sine wave
plt.plot(x_values, y_values, label='Sine Wave')

# Add labels and a legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave Plot')
plt.legend()

# Show the plot
plt.show()
