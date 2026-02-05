import pandas as pd

#load the dataset
df = pd.read_csv("crime.csv")

#create risk column
df["risk"] = df["ViolentCrimesPerPop"].apply(
    lambda x: "High-Crime" if x >= 0.50 else "LowCrime"
)

#calculate average unemployment
avg_unemployment = df.groupby("risk")["PctUnemployed"].mean() * 100

#print results
print("Average Unemployment Rate by Crime Risk:")
for risk, value in avg_unemployment.items():
    print(f"{risk}: {value:.2f}%")