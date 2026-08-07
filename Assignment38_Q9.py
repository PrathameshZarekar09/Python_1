import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*35

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="AssignmentsCompleted",
    hue="FinalResult"
)

# Add labels
plt.xlabel("Assignments Completed")
plt.ylabel("Number of Students")
plt.title("Assignments Completed vs Final Result")

# Show legend
plt.legend(title="Final Result")

plt.show()