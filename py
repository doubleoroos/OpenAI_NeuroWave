import matplotlib.pyplot as plt
import numpy as np
import os

# Zorg dat de outputmap bestaat
os.makedirs("output", exist_ok=True)

# Genereer een eenvoudige sinus-plot
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sample Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Sla op in hoofdmap en in output/
plt.savefig('R_plot.png')
plt.savefig('output/R_plot.png')
plt.close()
print("Plot opgeslagen als R_plot.png en output/R_plot.png")
