import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import MiniBatchKMeans
from sklearn.linear_model import LinearRegression
style.use("ggplot")
from sklearn import svm, linear_model
import pandas
import csv
import pandas as pd
import numpy.ma as ma
import ExtractFeaturesOfTestInput
#import SelectToPredicOrTrain
import popupMesseges
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import pickle
from sklearn import metrics as ms
import detectAccuracyOfSealSignModule

file_path = ""

def trainModel():
    X = []
    y = []
    with open('E:\Level4_Project\WritingFeatures5.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rowFeature = []
        for rowFeature in readCSV:
            X.append(rowFeature)
    with open('E:\Level4_Project\WritingTargets5.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rowTarget = []
        for rowTarget in readCSV:
            y.append(rowTarget)
    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(X, y)

    with open('E:\Level4_Project\svmSignature_classifier.pkl', 'wb') as svmSignModel:
        pickle.dump(clf, svmSignModel)

    with open('E:\Level4_Project\svmSignature_X.pkl', 'wb') as svmSignModel_X:
        pickle.dump(X, svmSignModel_X)

    with open('E:\Level4_Project\svmSignature_y.pkl', 'wb') as svmSignModel_y:
        pickle.dump(y, svmSignModel_y)
        # print(clf)
    # svmFile = open(r"E:\Level4_Project\svmModel.txt", "w+")
    # svmFile.write(str(clf))
    # #print(str(clf))
    # svmFile.close()
    #return clf
    predictModel()

def trainModelToClf():
    def trainModel():
        X = []
        y = []
        with open('E:\Level4_Project\WritingFeatures5.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            rowFeature = []
            for rowFeature in readCSV:
                X.append(rowFeature)
        with open('E:\Level4_Project\WritingTargets5.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            rowTarget = []
            for rowTarget in readCSV:
                y.append(rowTarget)
        clf = svm.SVC(kernel='linear', C=1.0)
        clf.fit(X, y)
        return clf
        #predictModel(clf)

def predictModel():
    # with open('E:\Level4_Project\svmSignature_classifier.pkl', 'wb') as svmSignModel:
    #     svm_loaded = pickle.load(svmSignModel)

    svmFile = open('E:\Level4_Project\svmSignature_classifier.pkl', 'rb')
    clf = pickle.load(svmFile)
    XFile = open('E:\Level4_Project\svmSignature_X.pkl', 'rb')
    X = pickle.load(XFile)
    yFile = open('E:\Level4_Project\svmSignature_y.pkl', 'rb')
    y = pickle.load(yFile)
    #clf = svm_loaded
    # svmFile = open(r"E:\Level4_Project\svmModel.txt", "w+")
    # svmFile = svmFile.read()
    # clf = svc(svmFile)
    #svmFile.close()
    arrayToPredict, y_test = ExtractFeaturesOfTestInput.getTextInputArray()
    #print(clf.predict([arrayToPredict]))
    predictUserNo = clf.predict([arrayToPredict])
    popupMesseges.predictSignatureOwnerNo(predictUserNo)

    accuracyModule = detectAccuracyOfSealSignModule.accuracyOfSignature(predictUserNo,arrayToPredict)

    print("The final Accuracy")
    print(accuracyModule)


    #print([predictUserNo])
    predictUserNo = int(predictUserNo)
    print("predict user")
    print(predictUserNo)
    print("ytest")
    y_test = int(y_test)
    print(y_test)
    # clf.fit(X, y)
    # clf.predict_proba([arrayToPredict])

    print(ms.accuracy_score([y_test], [predictUserNo]))
    accuracy_1 =(ms.accuracy_score([y_test], [predictUserNo])*100)
    print(accuracy_1)
    # file_path =('E:/Level4_Project/sign_list/01001001.jpg')
    # predictArray = ExtractFeaturesOfTestInput.getPredictInputArray()
    # print("Print array")
    # print(predictArray)
    # accuracy_2 = clf.score([y_test], [predictUserNo])
    # print(accuracy_2)

    # scores = cross_val_score(clf, X, y, cv=25)
    # print(scores.mean()*100)
    # print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean()*100, scores.std() * 2))
    # print((scores.mean(), scores.std() * 2))
    # accuracy = scores.mean()*100
    # SdValue = (scores.std() * 2)
    selctionModule(accuracy_1, accuracyModule, y_test, predictUserNo)

    #popupMesseges.predictValue(predictUserNo)

def trainSealModel():
    X = []
    y = []
    with open('E:\Level4_Project\WritingSealFeatures.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rowFeature = []
        for rowFeature in readCSV:
            X.append(rowFeature)
    with open('E:\Level4_Project\WritingSealTargets.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rowTarget = []
        for rowTarget in readCSV:
            y.append(rowTarget)
    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(X, y)

    with open('E:\Level4_Project\svmSeal_classifier.pkl', 'wb') as svmSealModel:
        pickle.dump(clf, svmSealModel)

    with open('E:\Level4_Project\svmSeal_X.pkl', 'wb') as svmSealModel_X:
        pickle.dump(X, svmSealModel_X)

    with open('E:\Level4_Project\svmSeal_y.pkl', 'wb') as svmSealModel_y:
        pickle.dump(y, svmSealModel_y)
        # print(clf)
    # svmFile = open(r"E:\Level4_Project\svmModel.txt", "w+")
    # svmFile.write(str(clf))
    # #print(str(clf))
    # svmFile.close()
    #return clf
    predictSealModel()

# def trainSealModelToClf():
#     def trainModel():
#         X = []
#         y = []
#         with open('E:\Level4_Project\WritingSealFeatures.csv') as csvfile:
#             readCSV = csv.reader(csvfile, delimiter=',')
#             rowFeature = []
#             for rowFeature in readCSV:
#                 X.append(rowFeature)
#         with open('E:\Level4_Project\WritingSealTargets.csv') as csvfile:
#             readCSV = csv.reader(csvfile, delimiter=',')
#             rowTarget = []
#             for rowTarget in readCSV:
#                 y.append(rowTarget)
#         clf = svm.SVC(kernel='linear', C=1.0)
#         clf.fit(X, y)
#         return clf
#         #predictModel(clf)

def predictSealModel():
    # with open('E:\Level4_Project\svmSignature_classifier.pkl', 'wb') as svmSignModel:
    #     svm_loaded = pickle.load(svmSignModel)

    svmFile = open('E:\Level4_Project\svmSeal_classifier.pkl', 'rb')
    clf = pickle.load(svmFile)
    XFile = open('E:\Level4_Project\svmSeal_X.pkl', 'rb')
    X = pickle.load(XFile)
    yFile = open('E:\Level4_Project\svmSeal_y.pkl', 'rb')
    y = pickle.load(yFile)
    # clf = svm_loaded
    # svmFile = open(r"E:\Level4_Project\svmModel.txt", "w+")
    # svmFile = svmFile.read()
    # clf = svc(svmFile)
    # svmFile.close()
    arrayToPredict, y_test = ExtractFeaturesOfTestInput.getSealInputArray()
    # print(clf.predict([arrayToPredict]))
    predictCompantNo = clf.predict([arrayToPredict])
    popupMesseges.predictSignatureOwnerNo(predictCompantNo)
    # print([predictUserNo])
    predictCompantNo = int(predictCompantNo)

    accuracyModule = detectAccuracyOfSealSignModule.accuracyOfSeal(predictCompantNo, arrayToPredict)

    print("The final Accuracy")
    print(accuracyModule)


    print("predict company")
    print(predictCompantNo)
    print("ytest")
    y_test = int(y_test)
    print(y_test)
    # clf.fit(X, y)
    # clf.predict_proba([arrayToPredict])
    print(ms.accuracy_score([y_test], [predictCompantNo]))
    accuracy_seal = (ms.accuracy_score([y_test], [predictCompantNo]) * 100)
    print(accuracy_seal)

    selctionFromSeal(accuracy_seal, accuracyModule, y_test, predictCompantNo)

    #popupMesseges.predictValue(predictUserNo)

def selctionModule(accuracy_1, accuracyModule, y_test, predictUserNo):
    if accuracy_1 == 100 :
            # and SdValue < 5:
        print("Go to Printed Or Hand Written Module")
        popupMesseges.GoToPrintedOrHandWrittenModule()
        # if invoiceImage = "Printed":
        #     print("Go to Printed Module")
        # else :
        #     print("Go to HandWritten Module")
    elif accuracyModule > 75:
            # and SdValue < 5:
        print("Go to Printed Or Hand Written Module")
        popupMesseges.GoToPrintedOrHandWrittenModule()
        # if invoiceImage = "Printed":
        #     print("Go to Printed Module")
        # else :
        #     print("Go to HandWritten Module")
    else:
        popupMesseges.fackSignInvoiceDetect()
        print("Invalid Signature of The Invoice is Detected")

def selctionFromSeal(accuracy_seal, accuracyModule, y_test, predictCompantNo):
    if accuracy_seal == 100:
        # and SdValue < 5:
        print("Go to Printed Or Hand Written Module")
        popupMesseges.GoToPrintedOrHandWrittenModule()
        # if invoiceImage = "Printed":
        #     print("Go to Printed Module")
        # else :
        #     print("Go to HandWritten Module")
    elif accuracyModule > 75:
        # and SdValue < 5:
        print("Go to Printed Or Hand Written Module")
        popupMesseges.GoToPrintedOrHandWrittenModule()
        # if invoiceImage = "Printed":
        #     print("Go to Printed Module")
        # else :
        #     print("Go to HandWritten Module")
    else:
        popupMesseges.fackSealInvoiceDetect()
        print("Invalid Signature of The Invoice is Detected")


