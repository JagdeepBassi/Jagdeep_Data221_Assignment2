import pandas as pd

df = pd.read_csv("student.csv")

#create grade_band
def grade_band(g):
    if g <= 9:
        return "Low"
    elif g <= 14:
        return "Medium"
    else:
        return "High"

df["grade_band"] = df["grade"].apply(grade_band)

#grouped summary table
summary = df.groupby("grade_band").agg(
    num_students=("grade", "size"),
    avg_absences=("absences", "mean"),
    pct_internet=("internet", "mean")
).reset_index()

# convert proportion to percent
summary["pct_internet"] = summary["pct_internet"] * 100

# save to file
summary.to_csv("student_bands.csv", index=False)

print(summary)
