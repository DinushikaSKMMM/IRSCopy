import tkinter
import sys
import self as self
import Seal_Signature_Verification
import featureExtraction_TrainData
import featureExtractions_TestData
import popupMesseges
import tkinter as tk
from tkinter import ttk, font, filedialog
from tkinter import Menu
import TrainAndPredict

win = tk.Tk()
tkvar = tkinter.StringVar(win)
bigfont = font.Font(family="Helvetica", size=40)
helv35 = font.Font(family='Helvetica', size=46)

def doForSignature():
    def browsefunc():
        filename = filedialog.askopenfilename()
        button.config(text=filename)
    filewin = tkinter.Toplevel(win)
    filewin.geometry('{}x{}'.format(8000, 8000))
    #tkinter.Label(filewin, text="Choose Invoice Verification Method", font='Helvetica 18 bold').grid(row=1, column=1)
    button = tkinter.Button(filewin, text="Upload signature data set to Feature Extraction",command= browsefunc)
    button.pack()
    featureExtraction_TrainData.signatureFeature_TrainInput()
    popupMesseges.completeSignExtractMessege()
    #self.master.destroy()
    #popupMesseges.popupMesseges()

def doForSeal():
    # filewin = tkinter.Toplevel(win)
    # filewin.geometry('{}x{}'.format(8000, 8000))
    # tkinter.Label(filewin, text="Upload seal data set to Feature Extraction", font='Helvetica 20 bold').grid(row=1, column=1)
    # def browsefunc():
    #     filename = filedialog.askopenfilename()
    #     button.config(text=filename)
    # #tkinter.Label(filewin, text="Choose Invoice Verification Method", font='Helvetica 18 bold').grid(row=1, column=1)
    # button = tkinter.Button(filewin, text="Upload seal data set to Feature Extraction",command= browsefunc)
    # button.pack()
    featureExtraction_TrainData.sealFeature_TrainInput()
    popupMesseges.completeSealExtractMessege()
    #self.master.destroy()
    #popupMesseges.popupMesseges()

def GUICreate(*args):
    # Create Menubar in Python GUI Application
    #win.resizable(width=False, height=False)
    # popupMesseges.hide(win)
    #bigfont = font.Font(family="Helvetica",size=20)
    win.option_add("*Font", bigfont)
    win.geometry('{}x{}'.format(8000, 8000))
    win.title("Signature & Seal Verification of the Invoice")

    # Exit action
    def _quit():
        win.quit()
        win.destroy()
        exit()

    # Create Menu Bar
    menuBar = Menu(win, font=('Tempus Sans ITC', 18))
    win.config(menu=menuBar)
    # File Menu
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="Extract Features From Signature Dataset", command=doForSignature, font='Helvetica 10 bold')
    fileMenu.add_separator()
    fileMenu.add_command(label="Extract Features From Seal Dataset", command=doForSeal, font='Helvetica 10 bold')
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=_quit,font='Helvetica 10 bold')
    menuBar.add_cascade(label="Extract Features", menu=fileMenu, font='Helvetica 10 bold')
    # Help Menu
    helpMenu = Menu(menuBar, tearoff=0, font='Helvetica 18 bold')
    helpMenu.add_command(label="Exit", command=_quit ,font='Helvetica 10 bold')
    menuBar.add_cascade(label="Setting", menu=helpMenu, font='Helvetica 10 bold')

    #Drop down menu
    mainframe = tkinter.Frame(win)
    mainframe.grid(column=0, row=0, sticky=('nw'))
    mainframe.columnconfigure(0, weight=2)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    #choices = {'By using Signature', 'By Using Seal', 'By using Seal & Signature'}
    choices = {'By using Signature', 'By Using Seal'}
    tkvar.set('Select The Method of verification to Feature Extraction')  # set the default option
    popupMenu = tkinter.OptionMenu(mainframe, tkvar, *choices,)

    popupMenu.config(font=bigfont)
    tkinter.Label(mainframe, text="Signature & Seal Verification Module", font='Helvetica 30 bold').grid(row=1, column=1)
    tkinter.Label(mainframe, text="", font='Helvetica 5 bold').grid(row=2, column=1)
    tkinter.Label(mainframe, text="Choose Invoice Verification Method", font='Helvetica 22 bold').grid(row=3, column=1)
    tkinter.Label(mainframe, text="", font='Helvetica 5 bold').grid(row=6, column=1)
    popupMenu.grid(row=7, column=1)
    tkvar.trace('w', change_dropdown)
    print(tkvar.get())
    #radioButton()
    win.mainloop()

def change_dropdown(*args):
        print(tkvar.get())
        if ((tkvar.get())==('By using Signature')):
            #featureExtractions_TestData.signatureFeature_testInput()
            radioButtonMethodForSignature()
            #popupMesseges.completeSignExtractMessege()
        if ((tkvar.get())==('By Using Seal')):
            #featureExtractions_TestData.signatureFeature_testInput()
            radioButtonMethodForSeal()
            #popupMesseges.completeSealExtractMessege()
        # if ((tkvar.get())==('By using Seal & Signature')):
        #     featureExtraction.signatureFeatureExtraction()

# def quit_loop(var,master):
#     print ("Selection:",var.get())
#     global selection
#     selection = var.get()
#     print(selection)
#     master.quit()

# def radioButton():
#     #master = win
#     #master = tkinter.Frame(win)
#     master = tk.Tk()
#     var = tkinter.IntVar()
#     var.set(1)
#     tk.Label(master, text="Select action which you need").grid(row=0, sticky='nw')
#     tk.Radiobutton(master, text="To tarin New SVM & predict Test Input", variable=var, value=1).grid(row=1, sticky='nw')
#     tk.Radiobutton(master, text="Predict TestInput with existing SVM", variable=var, value=2).grid(row=2, sticky='nw')
#     tk.Button(master, text="OK", command=quit_loop(var,master)).grid(row=3, sticky='nw')
#     print(var.get())
#     #return var
#     master.mainloop()


# def radioButtonMethod():
#     def validate():
#         value = option.get()
#         if value == "male":
#             print("Welcome dude")
#         elif value == "female":
#             print("Welcome gurl")
#         else:
#             print("An option must be selected")
#
#     root2 = tk.Tk()
#     root2.geometry("100x100")
#     option = tkinter.StringVar(root2 = root2)
#     option.set(0)
#     R1 = tkinter.Radiobutton(root2, text="MALE", value="male", var=option)
#     R2 = tkinter.Radiobutton(root2, text="FEMALE", value="female", var=option)
#     button = tkinter.Button(root2, text="OK", command=validate)
#     R1.pack()
#     R2.pack()
#     button.pack()
#     root2.mainloop()
def radioButtonMethodForSeal():
    def validate():
        value = option.get()
        if value == "PredictExistingSVM":
            #print("Welcome dude")
            print("To Predict By Using Existing SVM")
            TrainAndPredict.predictSealModel()
        elif value == "PredictNewSVM":
            #print("Welcome gurl")
            #clf = TrainAndPredict.trainModelToClf()
            #print(clf)
            #TrainAndPredict.predictModel(clf)
            print("To train New SVM & predict Test Input")
            #detectFakenessOfSignature.GUI
            TrainAndPredict.trainSealModel()
        else:
            print("An option must be selected")

    root = tk.Tk()
    root.geometry("300x300")
    option = tkinter.StringVar(root)
    option.set(0)
    R1 = tkinter.Radiobutton(root, text="Predict Existing SVM", value="PredictExistingSVM", var=option)
    R2 = tkinter.Radiobutton(root, text="Predict New SVM", value="PredictNewSVM", var=option)
    button = tkinter.Button(root, text="OK", command=validate)
    R1.pack()
    R2.pack()
    button.pack()
    root.mainloop()

def radioButtonMethodForSignature():
    def validate():
        value = option.get()
        if value == "PredictExistingSVM":
            #print("Welcome dude")
            print("To Predict By Using Existing SVM")
            TrainAndPredict.predictModel()
        elif value == "PredictNewSVM":
            #print("Welcome gurl")
            #clf = TrainAndPredict.trainModelToClf()
            #print(clf)
            #TrainAndPredict.predictModel(clf)
            print("To train New SVM & predict Test Input")
            #detectFakenessOfSignature.GUI
            TrainAndPredict.trainModel()
        else:
            print("An option must be selected")

    root = tk.Tk()
    root.geometry("300x300")
    option = tkinter.StringVar(root)
    option.set(0)
    R1 = tkinter.Radiobutton(root, text="Predict Existing SVM", value="PredictExistingSVM", var=option)
    R2 = tkinter.Radiobutton(root, text="Predict New SVM", value="PredictNewSVM", var=option)
    button = tkinter.Button(root, text="OK", command=validate)
    R1.pack()
    R2.pack()
    button.pack()
    root.mainloop()
# def selectionMethod(method):
#     if method == 1:
#         print("To tarin New SVM & predict Test Input")
#         TrainAndPredict.trainModel()
#     elif method == 2:
#         print("Predict TestInput with existing SVM")
#         clf = TrainAndPredict.trainModelToClf()
#         print(clf)
#         TrainAndPredict.predictModel(clf)


if __name__ == "__main__":
    #selct_SealSignature()
    #popupMesseges.hide()
    #radioButtonMethod()
    GUICreate()
    change_dropdown()
