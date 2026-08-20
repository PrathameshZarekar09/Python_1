import pandas as pd 
import matplotlib.pyplot as plt 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler 

Border = "-"*45

def LoadData(filename):
    print(Border)
    print("Performing Step1: Load Data")
    print(Border)

    df = pd.read_csv(filename)
    print("Data Loaded Successfully!")

    print(Border)
    return df




def EDA(df):
    print(Border)
    print("Performing Step2: EDA")
    print(Border)

    df.dropna(inplace = True)
    print("Shape of the Dataset: ",df.shape)
    print("Total Number Of Columns: ",df.shape[1])
    print("Total Number Of Entries: ",df.shape[0])
    print("Name of Columns: ",list(df.columns))
    print("Satistical Report of The Dataset: ")
    print(df.describe())
    print("EDA Completed!")
    
    print(Border)
    return df




def SplitData(df):
    print(Border)
    print("Seperating X and Y Variables")
    print(Border)

    X = df.drop("Class", axis = 1)
    Y = df["Class"]
    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state = 42)
    print("Dataset Splited successfully!")

    print(Border)
    return X_train, X_test, Y_train, Y_test





def main():
    #Step 1 Load Data:
    df = LoadData("WinePredictor.csv")

    #Step 2 EDA:
    df = EDA(df)

    #Step 3 Split Data:
    X_train, X_test, Y_train, Y_test = SplitData(df)


if __name__ == "__main__":
    main()