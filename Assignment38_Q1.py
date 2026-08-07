import pandas as pd 

Border = "-"*35

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

#####################################################
#First Five Record
#####################################################
print(Border)
print("First Five Record: ")
print(df.head())
print(Border)

#####################################################
#Last Five Record
#####################################################
print(Border)
print("Last Five Record: ")
print(df.tail())
print(Border)

#####################################################
# Total number of rows and columns
#####################################################
print(Border)
print("Total number of rows and columns: ")
print(df.shape)
print(Border)

#####################################################
# List of column names
#####################################################
print(Border)
print("List of column names: ",list(df.columns))
print(Border)

#####################################################
# Data types of each column
#####################################################
print(Border)
print("Data types of each column: ")
print(df.dtypes)
print(Border)