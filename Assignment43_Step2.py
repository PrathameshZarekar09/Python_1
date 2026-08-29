import pandas as pd 
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder
from sklearn.model_selection import train_test_split

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


def EDA(df):
    print(Border)
    print("Performing EDA.......")
    print(Border)

    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("Missing values per column: ",df.isnull().sum())
    print("Data Types and info", df.info())
    print("Unique Categories in Features: ")
    for col in df.columns:
        print( f"Column {col} unique values: {df[col].unique()}" )
    
    print(Border)
    return df 


def Preprocessing(df):
    print(Border)
    print("Preprocessing & Encoding Data.......")
    print(Border)

    X_raw = df[['Whether', 'Temperature']]
    y_raw = df['Play']

    ohe = OneHotEncoder(sparse_output=False)
    whether_encoded = ohe.fit_transform(X_raw[['Whether']])
    whether_df = pd.DataFrame(whether_encoded, columns=ohe.get_feature_names_out(['Whether']))


    temp_order = [['Cool', 'Mild', 'Hot']]
    oe = OrdinalEncoder(categories=temp_order)
    temp_encoded = oe.fit_transform(X_raw[['Temperature']])
    temp_df = pd.DataFrame(temp_encoded, columns=['Temperature_encoded'])

    X = pd.concat([whether_df, temp_df], axis=1).values

    le = LabelEncoder()
    y = le.fit_transform(y_raw)

    print("Encoding Completed Successfully!")
    print(f"Final Encoded Features Matrix Shape (X): {X.shape}")
    print(f"Final Encoded Labels Target Shape (y): {y.shape}")
    print(Border)
    
    return X, y




def main():
    #Step1 Load the Data:
    df = LoadData("PlayPredictor.csv")


    df = EDA(df)

    #Step2 Encoding the Data:
    X,y = Preprocessing(df)

if __name__ == "__main__":
    main()