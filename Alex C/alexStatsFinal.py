
import array
import math
list = []

def menu():
    user = 10
    while user != 0:
        printMenu()
        user = int(input("type in the number of your choice"))
        if user == 1:
            addToArray()
        if user == 2:
            deleteValue()
        if user == 3:
            deleteFromIndex()
        if user == 4:
            displayArray()
        if user == 5:
            computeMean()
        if user == 6:
            computeMedian()
        if user == 7:
            computeMidpoint()
        if user == 8:
            computeModes()
        if user == 9:
            standDeviation()
        if user == 0:
            print("thank you for using the menu")


def printMenu():
    print("1. Add Value to List")
    print("2. Delete Value from List (by value)")
    print("3. Delete Value from List (by location in list)")
    print("4. Display List")
    print("5. Compute Mean")
    print("6. Compute Median")
    print("7. Compute Midpoint")
    print("8. Compute Mode(s)")
    print("9. Compute Standard Deviation")
    print("0. exit")

def addToArray():

    list.append(float(input("What do you want to add to the list")))

def deleteValue():

    list.remove(float(input("What value to remove?")))

def deleteFromIndex():

    list.pop(int(input("What index to remove?")))

def displayArray():

    print(list)

def computeMean():
    total = 0
    i = 0

    for x in list:

        total += list[i]
        i=i+1


    mean = total/len(list)

    return mean
    print(mean)

def computeMedian():

    list.sort()
    i = computeMidpoint()
    print(list[i])

def computeMidpoint():

    middle = len(list)/2
    midpoint = round(middle)-1
    print(midpoint)
    return midpoint

def computeModes():

    list.sort()
    i = -1
    g = 0
    validIndex = False # checks if g is in the list's index range
    numValue = [1]
    numCount = [1]


    for x in list:
        i+=1
        g = i-1

        if g <= len(list) and g > -1:
            validIndex = True
            numValue.append(list[i])
            numCount.append(1)
            print(i)
        else:
                validIndex = False

        if validIndex == True and list[g] == list[i]:
            print(numCount)
            print(i)
            numCount[i]+=1

    i = 0
    highest = 0
    print(numValue)
    print(numCount)
    mode = 0

    for x in numValue:
        if numCount[i] > highest:
            highest = numCount[i]
            mode = numValue[i]

        i+=1

    print("the mode is "+str(mode))




def standDeviation():
    mean = computeMean()
    distance = 0.0 # value's numerical distance from the mean
    squaredSum = 0.0 # the distance but sqaured
    total = 0.0 # the sum of the individual value
    standDev = 0.0 # the square root of the added up sums
    allTotals = [] # all the sums of the values in a list
    addedUp = 0.0 # all the sums added up

    i = -1
    for x in list:
        i+=1
        distance = list[i] - mean
        squaredSum = distance*distance
        total = squaredSum/len(list)
        allTotals.append(total)

    i = -1
    for x in allTotals:
        i+=1
        addedUp += allTotals[i]

    standDev = math.sqrt(addedUp)

    print(standDev)


def main():
    menu()

if __name__ == '__main__':
    main()
