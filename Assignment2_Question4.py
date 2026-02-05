import pandas as pd

#load the dataset
df = pd.read_csv("student.csv")

#filter the dataset
filtered = df[
    (df["studytime"] >= 3) &
    (df["internet"] == 1) &
    (df["absences"] <= 5)
]

#save to new file
filtered.to_csv("high_engagement.csv", index=False)

# print required outputs
print("Number of students saved:", len(filtered))
print("Average grade:", filtered["grade"].mean())