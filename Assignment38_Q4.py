import pandas as pd 

Border = "-"*35

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)


result = df["FinalResult"].value_counts()
print(result)

print(Border)

percentage = df["FinalResult"].value_counts(normalize = True)*100
print(percentage)