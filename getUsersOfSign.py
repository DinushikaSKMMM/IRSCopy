import csv
import ntpath
import os

def getSignOwner(imagePath):
    #s = "E:/Level4_Project/sign  list/01001002.jpg"
    #print(os.path.split(imagePath)[-1])

    #print(os.path.splitext(imagePath)[0])
    newPath = os.path.splitext(imagePath)[0]
    #print(newPath.rpartition('/')[-1])
    target = []
    target = newPath.rpartition('/')[-1]
    targetUser = target[2] + target[3] + target[4]
    #print("User's no of the test input: " + target[2] + target[3] + target[4])
    #print(targetUser)
    with open(r'E:\Level4_Project\WritingTargets5.csv', mode='a+', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([targetUser])
    csvFile.close()

def getSignOwnerOfTestInput(imagePath):
    #s = "E:/Level4_Project/sign  list/01001002.jpg"
    #print(os.path.split(imagePath)[-1])

    #print(os.path.splitext(imagePath)[0])
    newPath = os.path.splitext(imagePath)[0]
    #print(newPath.rpartition('/')[-1])
    target = []
    target = newPath.rpartition('/')[-1]
    #targetUser = target[2] + target[3] + target[4]
    targetUser = target[3] + target[4]
    #print("User's no of the test input: " + target[2] + target[3] + target[4])
    #print(targetUser)
    return targetUser


    # with open(r'E:\Level4_Project\WritingTargets5.csv', mode='a+', newline='') as csvFile:
    #     writer = csv.writer(csvFile)
    #     writer.writerow([targetUser])
    # csvFile.close()

