import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*35

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

plt.figure(figsize=(8,5))

sns.boxplot(y=df["Attendance"])

plt.ylabel("Attendance (%)")
plt.title("Box Plot of Student Attendance")

plt.show()