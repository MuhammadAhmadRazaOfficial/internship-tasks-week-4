import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [1200, 1500, 1700, 1600, 1800, 2000, 
              2100, 1900, 2200, 2300, 2500, 2700]
}
df = pd.DataFrame(data)
plt.plot(df["Month"], df["Sales"], marker='o', linestyle='-', linewidth=2)
plt.title("Monthly Sales of Company")
plt.xlabel("Month")
plt.ylabel("Sales (in USD)")
plt.grid(True)
plt.show()
