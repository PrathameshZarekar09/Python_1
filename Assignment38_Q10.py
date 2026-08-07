import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*35

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="FinalResult",
    y="SleepHours"
)

# Add labels
plt.xlabel("Final Result")
plt.ylabel("Sleep Hours")
plt.title("Sleep Hours vs Final Result")

# Display plot
plt.show()