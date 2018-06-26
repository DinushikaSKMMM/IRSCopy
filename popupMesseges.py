import tkinter
import main
import tkinter as tk
from tkinter import ttk, font, filedialog, messagebox
from tkinter import Menu
from sys import exit

def hide(top):
    top.withdraw()

def show(top):
    top.update()
    top.deiconify()

def completeMessege():
    tkinter.messagebox.showinfo("Feature Extration Process Progres", "Your input invoice's signature features extraction process is completed successfully! ")

def completeSignExtractMessege():
    tkinter.messagebox.showinfo("Feature Extration Process Progres", "Your input invoice's signature features extraction process is completed successfully! ")

def completeSealExtractMessege():
    tkinter.messagebox.showinfo("Feature Extration Process Progres", "Your input invoice's seal features extraction process is completed successfully! ")

def predictValue(predictUserNo):
    tkinter.messagebox.showinfo("Owner of Signature of given Input Invoice", "Your input invoice's signature owner number is "+str(predictUserNo))

def predictSealValue(predictUserNo):
    tkinter.messagebox.showinfo("Owner of Signature of given Input Invoice", "Your input invoice's company number is "+str(predictUserNo))

def predictSignatureOwnerNo(predictUserNo):
    tkinter.messagebox.showinfo("Owner of Signature of given Input Invoice", "Your input invoice's company number is "+str(predictUserNo))

def goToPrintedModule():
    tkinter.messagebox.showinfo("Progress Report","Go To Printed Invoice Module ")

def goToHandWrittenModule():
    tkinter.messagebox.showinfo("Progress Report","Go To Hand Written Invoice Module ")

def GoToPrintedOrHandWrittenModule():
    tkinter.messagebox.showinfo("Progress Report","Go To Printed or Hand Written Invoice Modules")

def fackSignInvoiceDetect():
    tkinter.messagebox.showerror("Invalid Signature","Invalid Signature is detected in this Invoice")

def fackSealInvoiceDetect():
    tkinter.messagebox.showerror("Invalid Seal","Invalid Seal is detected in this Invoice")

def fackInvoiceDetect():
    tkinter.messagebox.showerror("Invalid Invoice","Invalid Invoice is detected" )

def popupMesseges():

    win = main.win
    #win = tk.Tk()
    popupRoot = win
    popupRoot.after(2000, exit)
    popupButton = tkinter.Button(popupRoot, text ="jsgkhjlfkjsz", font = ("Verdana", 12), bg ="yellow", command = exit)
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()

def featureExtractionMessege():
    win = main.win
    #win = tk.Tk()
    popupRoot = win
    popupRoot.after(2000, exit)
    popupButton = tkinter.Button(popupRoot, text ="jsgkhjlfkjsz", font = ("Verdana", 12), bg ="yellow", command = exit)
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()
#
# if __name__ == "__main__":
#  popupMesseges()