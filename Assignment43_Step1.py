import pandas as pd 


Border = "---"*40
def LoadData(data):
    print(Border)
    print("Loading Data.....")
    print(Border)

    df = pd.read_csv(data)
    print("Data Loaded Successfully!")
    print("Following are some entries of the data: ")
    print(df.head())

    print(Border)
    return df


def main():
    #Step1 Load the Data:
    df = LoadData("PlayPredictor.csv")


if __name__ == "__main__":
    main()