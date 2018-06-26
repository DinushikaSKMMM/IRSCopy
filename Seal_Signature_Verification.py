import featureExtraction
import tkinter
from tkinter import messagebox, font
import popupMesseges

def select_method_of_verifing(*args):
# hide main window
    root = tkinter.Tk()
    root.withdraw()
    root = tkinter.Tk()
    root.title("Signature & Seal Recognition Verification of the Invoice")

# Add a grid
    mainframe = tkinter.Frame(root)
    mainframe.grid(column=0, row=0, sticky=('nw'))
    mainframe.columnconfigure(0, weight=2)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

# Create a Tkinter variable
    tkvar = tkinter.StringVar(root)
    bigfont = font.Font(family="Helvetica",size=20)
    root.option_add("*Font", bigfont)
    # Dictionary with options
    helv35=font.Font(family='Helvetica', size=36)
    choices = {'By using Signature', 'By Using Seal', 'By using Seal & Signature'}
    tkvar.set('By using Signature')  # set the default option

    popupMenu = tkinter.OptionMenu(mainframe, tkvar, *choices)

    popupMenu.config(font=helv35)

    tkinter.Label(mainframe, text="Choose Invoice Verification Method", font='Helvetica 18 bold').grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

# on change dropdown value
    def change_dropdown(*args):
        print(tkvar.get())
        if ((tkvar.get())==('By using Signature')):
            featureExtraction.signatureFeature_testInput()
            #popupMesseges.popupMesseges()
            #print(featureExtraction.signatureFeatureExtraction.features_array)
        if ((tkvar.get())==('By Using Seal')):
            featureExtraction.signatureFeature_testInput()
            #popupMesseges.popupMesseges()
            #print(featureExtraction.signatureFeature_testInput.features_array)
        if ((tkvar.get())==('By using Seal & Signature')):
            featureExtraction.signatureFeature_testInput()
            #popupMesseges.popupMesseges()
            #print(featureExtraction.signatureFeatureExtraction.features_array)

# link function to change dropdown
    tkvar.trace('w', change_dropdown)

    root.mainloop()

