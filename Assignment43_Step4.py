import pandas as pd

from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


Border = "---" * 40


def LoadData(data):
    print(Border)
    print("Loading Data.....")
    print(Border)

    df = pd.read_csv(data)

    print("Data Loaded Successfully!")
    print("Following are some entries of the data:")
    print(df.head())

    print(Border)

    return df


def EDA(df):
    print(Border)
    print("Performing EDA.......")
    print(Border)

    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")

    print("Missing values per column:")
    print(df.isnull().sum())

    print("Data Types and Information:")
    df.info()

    print("Unique Categories in Features:")

    for col in df.columns:
        print(f"Column {col} unique values: {df[col].unique()}")

    print(Border)

    return df


def Preprocessing(df):
    print(Border)
    print("Preprocessing & Encoding Data.......")
    print(Border)

    X_raw = df[['Whether', 'Temperature']]
    y_raw = df['Play']

    # One Hot Encoding for Whether
    ohe = OneHotEncoder(sparse_output=False)

    whether_encoded = ohe.fit_transform(
        X_raw[['Whether']]
    )

    whether_df = pd.DataFrame(
        whether_encoded,
        columns=ohe.get_feature_names_out(['Whether'])
    )

    # Ordinal Encoding for Temperature
    temp_order = [['Cool', 'Mild', 'Hot']]

    oe = OrdinalEncoder(categories=temp_order)

    temp_encoded = oe.fit_transform(
        X_raw[['Temperature']]
    )

    temp_df = pd.DataFrame(
        temp_encoded,
        columns=['Temperature_encoded']
    )

    # Combine encoded features
    X = pd.concat(
        [whether_df, temp_df],
        axis=1
    ).values

    # Label Encoding for target
    le = LabelEncoder()

    y = le.fit_transform(y_raw)

    print("Encoding Completed Successfully!")
    print(f"Final Encoded Features Matrix Shape (X): {X.shape}")
    print(f"Final Encoded Labels Target Shape (y): {y.shape}")

    print(Border)

    return X, y


def SplitData(X, y):
    print(Border)
    print("Splitting Data.......")
    print(Border)

    print("Shape of X:", X.shape)
    print("Shape of Y:", y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Dataset Split Successfully!")

    print("Shape of X_train:", X_train.shape)
    print("Shape of X_test :", X_test.shape)
    print("Shape of Y_train:", Y_train.shape)
    print("Shape of Y_test :", Y_test.shape)

    print(Border)

    return X_train, X_test, Y_train, Y_test


def BuildModel():
    print(Border)
    print("Building Model....")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=3)

    print("Model Built Successfully!")

    print(Border)

    return model

def Train(model, X_train, Y_train):
    print(Border)
    print("Training the Model...")
    print(Border)

    model.fit(X_train, Y_train)
    print("Modle trainrd Successfully!")

    print(Border)
    return model

def TestModel(model, X_test, Y_test):
    print(Border)
    print("Testing Model...")
    print(Border)

    Prediction = model.predict(X_test)
    print("Prediction: ")
    print(Prediction)

    print(Border)
    return Prediction

def main():

    # Step 1: Load Data
    df = LoadData("PlayPredictor.csv")

    # Step 2: EDA
    df = EDA(df)

    # Step 3: Encoding
    X, y = Preprocessing(df)

    # Step 4: Split Data
    X_train, X_test, Y_train, Y_test = SplitData(X, y)

    # Step 5: Build Model
    model = BuildModel()

    model = Train(model, X_train,Y_train)

    Prediction = TestModel(model, X_test, Y_test)


if __name__ == "__main__":
    main()