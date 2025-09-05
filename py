import matplotlib.pyplot as plt
import os

# Zorg dat output map bestaat
os.makedirs("output", exist_ok=True)

# Maak een eenvoudige plot
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Voorbeeldplot")
plt.xlabel("x")
plt.ylabel("x^2")

# Sla op als artifact
plt.savefig("R_plot.png")
plt.savefig("output/R_plot.png")
print("Plot opgeslagen als R_plot.png en output/R_plot.png")
