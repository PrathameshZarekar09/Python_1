import pandas as pd 
import matplotlib.pyplot as plt

Border = "-"*35

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

plt.figure(figsize=(8,5))

plt.hist(df["StudyHours"], bins=10)

plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.title("Histogram of Study Hours")

plt.show()