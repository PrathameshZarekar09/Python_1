#Error Dots are not visible 

import pandas as pd 
import matplotlib.pyplot as plt

Border = "-"*35

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

plt.figure(figsize=(8,5))


PassStudents = df[df["FinalResult"] == 'Pass']

plt.scatter(
    PassStudents["StudyHours"],
    PassStudents["PreviousScore"],
    color='green',
    label='Pass',
    alpha=1
)

# Plot Fail students
FailStudents = df[df["FinalResult"] == 'Fail']

plt.scatter(
    FailStudents["StudyHours"],
    FailStudents["PreviousScore"],
    color='red',
    label='Fail',
    alpha=1
)

# Add labels and title
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")

# Show legend
plt.legend()

# Display plot
plt.show()