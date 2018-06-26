import csv
from _pydecimal import Decimal
import numpy as np
import math

def getTargetSignList(predictUserNo):
    with open('E:\Level4_Project\WritingTargets5.csv', "r") as f:
        reader = csv.reader(f)
        indexSignArray = []
        print("user no")
        print(str(predictUserNo))
        for line_num, content in enumerate(reader):
            if content == predictUserNo:
                print(content, line_num + 1)
                indexSignArray.append((line_num + 1))
    print(indexSignArray)
    #return indexSignArray
    #getMeanValueOfPredictFeatureArray(indexSignArray)

    with open('E:\Level4_Project\WritingFeatures5.csv') as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        # row_you_want = readCSV[14]
        somelist = [14, 15]
        meanArray = []
        print("array list ")
        print(indexSignArray)
        for index, item in enumerate(indexSignArray):
            # print("item at {} is {}".format(index, item))
            print(readCSV[index])
            featureArray = readCSV[index]
            featureArray = np.asfarray(featureArray, float)
            print(featureArray)
            print(featureArray)
            m1 = np.mean(featureArray)
            print(m1)
            meanArray.append(m1)

    print("mean array")
    print(meanArray)
    print("mean of array")
    print(np.mean(meanArray))
    predictSignMeanValueOfFeatureArray = np.mean(meanArray)
    print("predict messssssssssssssssssssssssssssss")
    print(predictSignMeanValueOfFeatureArray)
    return predictSignMeanValueOfFeatureArray

def getMeanValueOfPredictFeatureArray(indexSignArray):
    with open('E:\Level4_Project\WritingFeatures5.csv') as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        # row_you_want = readCSV[14]
        somelist = [14, 15]
        meanArray = []
        print("array list ")
        print(indexSignArray)
        for index, item in enumerate(indexSignArray):
            # print("item at {} is {}".format(index, item))
            print(readCSV[index])
            featureArray = readCSV[index]
            featureArray = np.asfarray(featureArray, float)
            print(featureArray)
            print(featureArray)
            m1 = np.mean(featureArray)
            print(m1)
            meanArray.append(m1)

    print("mean array")
    print(meanArray)
    print("mean of array")
    print(np.mean(meanArray))
    predictSignMeanValueOfFeatureArray = np.mean(meanArray)
    print("predict messssssssssssssssssssssssssssss")
    print(predictSignMeanValueOfFeatureArray)
    return predictSignMeanValueOfFeatureArray

def getTargetSealList(predictCompantNo):
    with open('E:\Level4_Project\WritingTargets5.csv', "r") as f:
        reader = csv.reader(f)
        indexSealArray = []
        for line_num, content in enumerate(reader):
            if content[0] == str(predictCompantNo):
                print(content, line_num + 1)
                indexSealArray.append((line_num + 1))
    print("index array")
    print(indexSealArray)
    #return indexSignArray
    #getMeanValueOfPredictSealFeatureArray(indexSealArray)

    with open('E:\Level4_Project\WritingFeatures5.csv') as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        # row_you_want = readCSV[14]
        somelist = [14, 15]
        meanArray = []
        for index, item in enumerate(indexSealArray):
            # print("item at {} is {}".format(index, item))
            print(readCSV[index])
            featureArray = readCSV[index]
            featureArray = np.asfarray(featureArray, float)
            print(featureArray)
            print(featureArray)
            m1 = np.mean(featureArray)
            print(m1)
            meanArray.append(m1)

    print("mean array")
    print(meanArray)
    print(np.mean(meanArray))
    predictSealMeanValueOfFeatureArray = np.mean(meanArray)
    print("predict mean valu to accuracy")
    print(predictSealMeanValueOfFeatureArray)
    return (predictSealMeanValueOfFeatureArray)

def accuracyOfSignature(predictUserNo,arrayToPredict):
    test_featureArray = arrayToPredict
    print("test array")
    print(test_featureArray)
    testFeatureArray_mean = np.mean(test_featureArray)
    print("test mean")
    print(testFeatureArray_mean)
    print("predict mean")

    predictFeatureArray_mean = getTargetSignList(predictUserNo)
    print("predict value")
    print(predictFeatureArray_mean)
    multiValue = (Decimal(testFeatureArray_mean - predictFeatureArray_mean)*Decimal(testFeatureArray_mean - predictFeatureArray_mean))
    print("multivalue")
    print(multiValue)
    squareRootValue =format(math.sqrt(multiValue))
    print("squroot")
    print(squareRootValue)
    #squareRootValue = math.sqrt((testFeatureArray_mean - predictFeatureArray_mean) * (testFeatureArray_mean - predictFeatureArray_mean))
    testFeatureArray_mean = format(testFeatureArray_mean, '.6f')
    division = float(squareRootValue) / float(predictFeatureArray_mean)
    # print("dive")
    # print(format(dive,'.7f'))
    # print(format(((math.sqrt((m1-m2)*(m1-m2)))//m1),'.6f'))
    # print((dive)*100)
    accuracy = ((1.0 - division) * 100)
    print("Accuracy")
    print(accuracy)
    return accuracy

def accuracyOfSeal(predictCompantNo, arrayToPredict):
    test_featureArray = arrayToPredict
    print("test array")
    print(test_featureArray)
    testFeatureArray_mean = np.mean(test_featureArray)
    print("test mean")
    print(testFeatureArray_mean)
    print("predict mean")

    predictFeatureArray_mean = getTargetSealList(predictCompantNo)
    print("predict value")
    print(predictFeatureArray_mean)
    multiValue = (Decimal(testFeatureArray_mean - predictFeatureArray_mean)*Decimal(testFeatureArray_mean - predictFeatureArray_mean))
    print("multivalue")
    print(multiValue)
    squareRootValue =format(math.sqrt(multiValue))
    print("squroot")
    print(squareRootValue)
    #squareRootValue = math.sqrt((testFeatureArray_mean - predictFeatureArray_mean) * (testFeatureArray_mean - predictFeatureArray_mean))
    testFeatureArray_mean = format(testFeatureArray_mean, '.6f')
    division = float(squareRootValue) / float(predictFeatureArray_mean)
    # print("dive")
    # print(format(dive,'.7f'))
    # print(format(((math.sqrt((m1-m2)*(m1-m2)))//m1),'.6f'))
    # print((dive)*100)
    accuracy = ((1.0 - division) * 100)
    print("Accuracy")
    print(accuracy)
    return accuracy

