import math

def Distance(P1,P2):
    Ans = math.sqrt((P1["X"]-P2["X"])**2 + (P1["Y"]-P2["Y"])**2)
    return Ans

def KNNClassifier():
    Border = "--"*45

    Dataset = [
        {"Point" : "A", "X" : 1, "Y" : 2, "Label" : "Red"},
        {"Point" : "B", "X" : 2, "Y" : 3, "Label" : "Red"},
        {"Point" : "C", "X" : 3, "Y" : 1, "Label" : "Blue"},
        {"Point" : "D", "X" : 6, "Y" : 5, "Label" : "Blue"}
    ]

    print(Border)
    print("KNNClassifier")
    print(Border)

    for i in Dataset:
        print(i)

    print(Border)

    X = int(input("Enter point X: "))
    Y = int(input("Enter point Y: "))

    new_point = {"X":X, "Y":Y}

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
    K = 1
    nearest = sorted_data[:K]

    print("Nearest 3 are: ")
    for d in nearest:
        print(d)

    votes = {}
    for neighbours in nearest:
        label = neighbours["Label"]
        votes[label] = votes.get(label,0)+1

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