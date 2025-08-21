import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Math": [85, 90, 75, 95],
    "English": [78, None, 80, 85],
    "Science": [92, 88, None, 89]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print("students.csv created successfully!\n")
df = pd.read_csv("students.csv")
print("Original Data:")
print(df)
df_cleaned = df.fillna(df.mean(numeric_only=True))
print("\nCleaned Data:")
print(df_cleaned)
averages = df_cleaned[['Math', 'English', 'Science']].mean()
print("\n Average Marks of the Whole Class:")
print(averages)
