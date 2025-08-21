import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
df = pd.read_csv("students.csv")

# Step 2: Clean data (fill missing values with column mean)
df_cleaned = df.fillna(df.mean(numeric_only=True))

# Step 3: Calculate total marks per student
df_cleaned["Total"] = df_cleaned[["Math", "English", "Science"]].sum(axis=1)

# Step 4: Plot bar chart
plt.bar(df_cleaned["Name"], df_cleaned["Total"])
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Bar Chart of Marks per Student")
plt.show()
