import pandas as pd 

Border = "-"*35

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)


###########################################
# Average Study Hours
###########################################
print(Border)
average = df["StudyHours"].mean()
print("Average of Study Hours: ",average)
print(Border)


###########################################
# Average Attendance
###########################################
print(Border)
average1 = df["Attendance"].mean()
print("Average of Attendance: ",average1)
print(Border)


###########################################
# Maximum Previous Score
###########################################
print(Border)
Maximum = df["PreviousScore"].max()
print("Maximum of Previous Score: ",Maximum)
print(Border)


###########################################
# Minimum Sleep Hours
###########################################
print(Border)
Minimum = df["SleepHours"].max()
print("Minimum Sleep Hours: ",Minimum)
print(Border)