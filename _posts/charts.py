import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.show()


# Add a title and labels: 
plt.title("Basic Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Change line style and color:
plt.plot(x, y, linestyle='--', color='r')

# Add gridlines:
plt.grid(True)
plt.show()


# Scatter plot:
plt.scatter(x, y)
plt.show()

# Bar chart:
categories = ['A', 'B', 'C']
values = [3, 7, 5]
plt.bar(categories, values)
plt.show()

# Histogram:
data = [1, 2, 2, 3, 3, 3, 4, 5, 6]
plt.hist(data)
plt.show()





import numpy as np
import matplotlib.pyplot as plt

# Create smooth data points
x = np.linspace(0, 10, 100)
y = np.sin(x) * np.exp(-0.1 * x)  # A damped sine wave for a cool effect

# Set dark background
plt.style.use("dark_background")

# Create the plot
plt.figure(figsize=(8, 5))  # Adjust figure size
plt.plot(x, y, linestyle='-', linewidth=2, color='#00c8ff', label="Damped Sine Wave")  # Stylish color

# Add labels and title with stylish formatting
plt.title("Cool Looking Graph: Damped Sine Wave", fontsize=14, fontweight='bold', color="white")
plt.xlabel("Time (s)", fontsize=12, color="white")
plt.ylabel("Amplitude", fontsize=12, color="white")

# Add grid with transparency
plt.grid(True, linestyle='--', alpha=0.5)

# Add annotation
plt.annotate("Peak", xy=(1.57, 0.8), xytext=(3, 1),
             arrowprops=dict(facecolor='white', arrowstyle="->"),
             fontsize=12, color="white")

# Show legend
plt.legend()

# Display the plot
plt.show()
