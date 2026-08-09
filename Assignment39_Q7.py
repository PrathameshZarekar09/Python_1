import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

Border = "-"*40

############################################################
# Load the Data
############################################################
print(Border)
print("Loading The Data")
print(Border)

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

print("Data Loaded Sucessfully!..")
print(Border)



############################################################
# EDA 
############################################################
print(Border)
print("Performing EDA")
print(Border)

print("Shape of the Dataset : ",df.shape)

print("Coloumn names : ",list(df.columns))

print("Missing Values Per Column: ")
print(df.isnull().sum())

print("Statistical report of dataset: ")
print(df.describe())

print(Border )




############################################################
# Dependent and Independent Variables 
############################################################
print(Border)
print("Dependent and Independent Variables")
print(Border)

# X = Independent Variables / Features
# Y = Dependent Variables / Labels

Features_column = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[Features_column]
Y = df["FinalResult"]

print("X Shape: ",X.shape)
print("Y Shape: ",Y.shape)

print(Border)




############################################################
# Visualisation of Dataset
############################################################
#print(Border)
#print("Visualisation of Dataset")
#print(Border)




############################################################
# split dataset for training and testing 
############################################################
print(Border)
print("split dataset for training and testing ")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 42)
print("Dataset has splited into traing and testing part")

print("X: ",X.shape)             #(30,5)
print("Y: ",Y.shape)             #(30,1)

print("X Train: ",X_train.shape)        #(24,5)
print("Y Train: ",Y_train.shape)        #(24,)

print("X Test: ",X_test.shape)          #(6,5)
print("Y Test: ",Y_test.shape)          #(6,)

print(Border)




############################################################
# Build the model
############################################################
print(Border)
print("Building the model....")
print(Border)

Model = DecisionTreeClassifier(max_depth = None)

print("Model created sucessfully!!")
print(Border)




############################################################
# Train the model
############################################################
print(Border)
print("Training the model...")
print(Border)

Model.fit(X_train, Y_train)

print("Model Trained Successfully!!!!!")
print(Border)




############################################################
# Test The Model
############################################################
print(Border)
print("Testing the model.....")
print(Border)

Y_Pred = Model.predict(X_test)

print("Model Testing Done")

print("Expected Answer: ",Y_test)

print("Predicted Answer: ",Y_Pred)




############################################################
# Calculate accuracy
############################################################
print(Border)
print("Calculating Accuracy...")
print(Border)

accuracy = accuracy_score(Y_test, Y_Pred)
print("Accuracy: ",accuracy*100)




############################################################
# Confusion matrix
############################################################
print(Border)
print("Confusion Matrix")
print(Border)

cm = confusion_matrix(Y_test, Y_Pred)
print(cm)




############################################################
# Training and Testing Accuracy
############################################################
print(Border)
print("Calculating Training and Testing Accuracy.....")
print(Border)

Y_train_pred = Model.predict(X_train)

trainaccuracy = accuracy_score(Y_train,Y_train_pred)

print("Training Accuracy: ",trainaccuracy*100,"%")



Y_test_pred = Model.predict(X_test)

testaccuracy = accuracy_score(Y_test,Y_test_pred)

print("Testing Accuracy: ",testaccuracy*100,"%")

print(Border)




############################################################
# tesing model on new student (study hours=6,attendence=85,previousscore=66,assignmentcomplete=7,sleephour=7)
############################################################
print(Border)
print("tesing model on new student (study hours=6,attendence=85,previousscore=66,assignmentcomplete=7,sleephour=7)...........")
print(Border)

newstudent = pd.DataFrame(
    [[6,85,66,7,7]],columns = Features_column
)
prediction = Model.predict(newstudent)
print("Prediction: ",prediction[0])

print(Border)