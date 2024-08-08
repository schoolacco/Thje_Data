from tkinter import *
import pandas as pd
root = Tk()
root.title("Epik GUI")
root.configure(background= "black")
root.maxsize(10000,10000)
root.minsize(500,500)
root.geometry("500x500+20+100")
changed = False
Thje_df = pd.read_csv('SydneyHousePrices.csv')
Thje_df = Thje_df.drop(columns=['Id'])
#Text Test
text = Label(root, text="It's a GUI :D")
text.pack()
text2 = Label(root, text="Yipee!")
text2.pack()
new_df = Thje_df
previous_df = Thje_df
def selectItems():
    global new_df, changed, previous_df
    if  var.get():  # If the button is checked,
        previous_df = new_df        
        new_df = previous_df.drop(columns=["Date"])  # Print print the cb's text
        changed = True
    else:
        new_df = previous_df        
        new_df["Date"] = Thje_df["Date"]
def selectItems2():
    global new_df, changed, previous_df
    if  var2.get():  # If the button is checked,
        previous_df = new_df        
        new_df = previous_df.drop(columns=["suburb"])  # Print print the cb's text
        changed = True
    else:
        new_df = previous_df        
        new_df["suburb"] = Thje_df["suburb"]

def selectItems3():
    global new_df, changed, previous_df
    if  var3.get():  # If the button is checked,
        previous_df = new_df        
        new_df = previous_df.drop(columns=["postalCode"])  # Print print the cb's text
        changed = True
    else:
        new_df = previous_df        
        new_df["postalCode"] = Thje_df["postalCode"]

def Table():
        global new_df, changed
        if changed != True:
             new_df = Thje_df
        print(new_df)  # Print print the cb's text

var = IntVar()  # variable class
item1 = Checkbutton(root, text="Date",
        variable=var, command=selectItems)
item1.pack(anchor='w')


var2 = IntVar()  # variable class
item2 = Checkbutton(root, text="Suburb",
        variable=var2, command=selectItems2)
item2.pack(anchor='w')

var3 = IntVar()  # variable class
item3 = Checkbutton(root, text="Postal Code",
        variable=var3, command=selectItems3)
item3.pack(anchor='w')

iteme = Button(root, text="Display", command=Table)
iteme.pack(anchor='w')

root.mainloop()