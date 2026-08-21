import math

def Distance(P1, P2):
    Ans = math.sqrt((P1["Study Hours"] - P2["Study Hours"])**2 + (P1["Attendence"] - P2["Attendence"])**2)
    return Ans

def KNNClassifier():
    Border = "--"*45

    Dataset = [
        {"Study Hours" : 2, "Attendence" : 60, "Result" : "Fail"},
        {"Study Hours" : 5, "Attendence" : 80, "Result" : "Pass"},
        {"Study Hours" : 6, "Attendence" : 85, "Result" : "Pass"},
        {"Study Hours" : 1, "Attendence" : 50, "Result" : "Fail"}
    ]

    print(Border)
    print("KNNClassifier")
    print(Border)

    for i in Dataset:
        print(i)

    print(Border)

    Study_Hours = int(input("Enter Study Hours: "))
    Attendence = int(input("Enter Attendance: "))

    new_point = {"Study Hours":Study_Hours, "Attendence":Attendence}

    print("Distance for all points: ")
    
    for d in Dataset:
        d["Distance"] = Distance(d,new_point)

    for d in Dataset:
        print(d)
    print(Border)

    sorted_data = sorted(Dataset, key = lambda item : item["Distance"])

    print(Border)
    print("Sorted Data: ")
    for d in sorted_data:
        print(d)

    print(Border)
    K = 3
    nearest = sorted_data[:K]

    print("Nearest 3 are: ")
    for d in nearest:
        print(d)

    votes = {}
    for neighbours in nearest:
        Result = neighbours["Result"]
        votes[Result] = votes.get(Result,0)+1

    print(Border)
    print("Voting Result: ")

    for d in votes:
        print("Name: ",d, "Number of Votes ",votes[d])

    print(Border)
    iMax = 0
    Name = ""

    for d in votes:
        if(votes[d]>iMax):
            iMax = votes[d]
            Name = d

    print("Final Predicition is : ",Name)





def main():
    KNNClassifier()

if __name__ == "__main__":
    main()