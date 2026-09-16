import pandas as pd 

Data = {
    "Name" : ["Amit", "Sagar", "Pooja"],
    "Math" : [85,90,78],
    "Science" : [92,88,80],
    "English" : [75,85,82]
}

df = pd.DataFrame(Data)

print("Shape Of Data: ")
print(df.shape[0],"Rows",df.shape[1],"Columns")              #If you're just accessing stored information → usually no ()

print("Data Types Of Data: ",df.dtypes)
#print(df.info())



print("Description of the Data: ")
print(df.describe())    #If Python has to perform an action → usually ()


                        
df["Total"] = df["Math"] + df["Science"] + df["English"]
print("New Data with Total: ")
print(df)



print("Students who Scored more than 85 in Science: ")
print(df[df["Science"]>85])