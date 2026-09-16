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
                        
print("Data before Droping The English Column: ")
print(df)



print("Data After Droping The English Column: ")
print(df.drop(columns = ["English"]))
