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

def main():
    #Step 1 Load Data
    df = LoadData("WinePredictor.csv")

if __name__ == "__main__":
    main()