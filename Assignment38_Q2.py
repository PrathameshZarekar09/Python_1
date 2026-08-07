import pandas as pd 

Border = "-"*35

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

###########################################
# Total number of students
###########################################
print(Border)
print("Total number of students: ",len(df))
print(Border)



###########################################
# Student Passed (Final Result = 1)
###########################################
print(Border)
count=0
for result in df["FinalResult"]:
    if result == 1:
        count = count+1
print("Student Passed: ",count)
print(Border)



###########################################
# Student failed (Final Result = 0)
###########################################
print(Border)
count=0
for result in df["FinalResult"]:
    if result == 0:
        count = count+1
print("Student Failed: ",count)
print(Border)