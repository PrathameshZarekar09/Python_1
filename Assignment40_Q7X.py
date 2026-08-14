import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "--"*50

def StudentClassifier(DataPath):

    ##########################################################################
    # Step 1: Load The Data Set
    ##########################################################################
    print(Border)
    print("Step 1: Load The Data Set")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Dataset Loaded Succesfully!")
    print("Here are some following entries of the dataset")
    print(df.head())
    print(Border)


    
    ##########################################################################
    # Step 2: EDA
    ##########################################################################
    print(Border)
    print("Step 2: EDA")
    print(Border)

    df.dropna(inplace = True)
    print("Shape of Dataset: ",df.shape)
    print("Total Columns: ",df.shape[1])
    print("Column Names: ",list(df.columns))
    print("Total Entries in the Dataset: ",df.shape[0])
    print("Statistical Report of the Dataset: ",df.describe())
    print(Border)



    ##########################################################################
    # Step 3: Seperate Independent and Dependent Variables
    ##########################################################################
    print(Border)
    print("Step 3: Seperate Independent and Dependent Variables")
    print(Border)

    #X = Independent Variable/ Features
    #Y = Dependent Variables / Label
    X = df.drop(columns=["FinalResult"]) 
    Y = df["FinalResult"]
    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)
    print("Input columns: ",X.columns.tolist())  ##not understod
    print("Output columns: FinalResult")
    print(Border)



    ##########################################################################
    # Step 4: Split Dataset for training and testing
    ##########################################################################
    print(Border)
    print("Step 4: Split Dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, random_state=10,stratify=Y)
    print("Following are some Details of Trained and Tested Data: ")
    print("Shape of Trained Data (X_train): ",X_train.shape)
    print("Shape of Test Data (X_test): ",X_test.shape)

    print("Shape of Trained Data (Y_train): ",Y_train.shape)
    print("Shape of Test Data (Y_test): ",Y_test.shape)

    print(Border)



    ##########################################################################
    # Step 5: Build The Model
    ##########################################################################
    print(Border)
    print("Step 5: Build The Model")
    print(Border)

    Model = DecisionTreeClassifier(max_depth = 5)
    print("Model Build Sucessfuly...")
    print(Border)



    ##########################################################################
    # Step 6: Train the model
    ##########################################################################
    print(Border)
    print(" Step 6: Training the Model....")
    print(Border)

    Model.fit(X_train,Y_train)
    print("Model Trained Sucessfully.....")
    print(Border)

    ##########################################################################
    # Step 7: Using model.feature_importances_
    ##########################################################################
    print(Border)
    print("Step 7: Using model.feature_importances_")
    print(Border)

    print(Model.feature_importances_)
    print(Border)



    ##########################################################################
    # Step 8: Using model.feature_importances_ and detailed explanation
    ##########################################################################
    print(Border)
    print("Step 8: Using model.feature_importances_ and detailed explanation")
    print(Border)

    for feature, importance in zip(X.columns, Model.feature_importances_):
        print(feature ,":", importance)
    print(Border)



    ##########################################################################
    # Step 9: Test The Model
    ##########################################################################
    print(Border)
    print("Step 9: Test The Model")
    print(Border)

    Y_Pred = Model.predict(X_test)
    print("Model Testing Done")
    for expect, predicted in zip(Y_test,Y_Pred):
        print("Expected", expect," : Predicted",predicted)



    #print("Expected Answer: ")
    #print(Y_test)
    #print("Predicted Answer: ")
    #print(Y_Pred)
    #print(Border)



    ##########################################################################
    # Step 10: Calculate Accuracy
    ##########################################################################
    print(Border)
    print("Step 10: Calculate Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_Pred)
    print("Accuracy is: ",accuracy*100,"%")
    print(Border)



    ##########################################################################
    # Step 11: Calculate Accuracy Manually
    ##########################################################################
    print(Border)
    print("Step 11: Calculate Accuracy Manually")
    print(Border)

    Correct = 0

    for expected, predicted in zip(Y_test,Y_Pred):
        if expected == predicted:
            Correct = Correct + 1
        
    Total = len(Y_test)
    Accuracy2=(Correct/Total)*100

    print("Correct Predictions: ",Correct)
    print("Total Predicitions: ",Total)
    print("Accuracy Calculated Manullay is: ",Accuracy2,"%")
    print(Border)

    
    
    ##########################################################################
    # Step 12: Identify Misclassified Students
    ##########################################################################
    print(Border)
    print("Step 12: Identify Misclassified Students")
    print(Border)
    
    Misclassified = Y_test!=Y_Pred

    print("Misclassified Students: ")
    print(X_test[Misclassified])

    print("Expected Result: ")
    print(Y_test[Misclassified])

    print("Predicted Result: ")
    print(Y_Pred[Misclassified])

    print("Total Misclassified Students: ",Misclassified.sum())
    print(Border)
    
    
    
    ##########################################################################
    # Step 12: Predict Result of 5 new students
    ##########################################################################
    '''print(Border)
    print("Step 12: Predict Result of 5 new students")
    print(Border)

    NewStudent = pd.DataFrame({
        "StudyHours":[6,3,8,4,7],
        "Attendance":[85,65,95,70,90],
        "PreviousScore":[75,55,92,60,88],
        "AssignmentsCompleted":[8,5,10,6,9],
        "SleepHours":[7,6,8,5,7]
        })
    
    Y_NewPred = Model.predict(NewStudent)
    print("Prediction of 5 new students: ")
    
    for i, prediction in enumerate(Y_NewPred):
        if prediction == 1:
            result = "Pass"
        else:
            result = "Fail"
        
        print("Student",i+1,":",result)

    print(Border)'''

def main():
    StudentClassifier("student_performance_ml.csv")

if __name__ == "__main__":
    main()