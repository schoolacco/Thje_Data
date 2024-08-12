from tkinter import *
import pandas as pd
import time
import os
os.system('cls')
root = Tk()
root.title("Sydney House Inflation") #GUI name
root.configure(background= "white") #Background colour
root.maxsize(10000,10000)
root.minsize(500,500)
root.geometry("500x500+20+100")
changed = False
mean = False
Thje_df = pd.read_csv('SydneyHousePrices.csv') #Defining the dataset
Thje_df = Thje_df.drop(columns=['Id']) #Removing something useless.
#Text Test
text = Label(root, text="STEP 1:") 
text.pack()
text2 = Label(root, text="Check options to be removed from dataset.")
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

def selectItems4():
    global new_df, changed, previous_df
    if  var4.get():  # If the button is checked,
        previous_df = new_df        
        new_df = previous_df.drop(columns=["sellPrice"])  # Print print the cb's text
        changed = True
    else:
        new_df = previous_df        
        new_df["sellPrice"] = Thje_df["sellPrice"]

def selectItems5():
    global new_df, changed, previous_df
    if  var5.get():  # If the button is checked,
        previous_df = new_df        
        new_df = previous_df.drop(columns=["bed"])  # Print print the cb's text
        changed = True
    else:
        new_df = previous_df        
        new_df["bed"] = Thje_df["bed"]

def selectItems6():
    global new_df, changed, previous_df
    if  var6.get():  # If the button is checked,
        previous_df = new_df        
        new_df = previous_df.drop(columns=["bath"])  # Print print the cb's text
        changed = True
    else:
        new_df = previous_df        
        new_df["bath"] = Thje_df["bath"]

def selectItems7():
    global new_df, changed, previous_df
    if  var7.get():  # If the button is checked,
        previous_df = new_df        
        new_df = previous_df.drop(columns=["car"])  # Print print the cb's text
        changed = True
    else:
        new_df = previous_df        
        new_df["car"] = Thje_df["car"]

def selectItems8():
    global new_df, changed, previous_df
    if  var8.get():  # If the button is checked,
        previous_df = new_df        
        new_df = previous_df.drop(columns=["propType"])  # Print print the cb's text
        changed = True
    else:
        new_df = previous_df        
        new_df["propType"] = Thje_df["propType"]

def Table():
        global new_df, changed
        if changed != True:
             new_df = Thje_df
        print(new_df)  # Print print the cb's text
        time.sleep(5)
        os.system('cls')

def Exit():
    global root, text
    root.destroy()
    root = Tk()
    root.title("Bonus Measurements") #GUI name
    root.configure(background= "white") #Background colour
    root.maxsize(10000,10000)
    root.minsize(500,500)
    root.geometry("500x500+20+100")
    text = Label(root, text="STEP 2:") 
    text.pack()
    text2 = Label(root, text="Check extra measurements to be added to dataset")
    text2.pack()
    var = IntVar()  # variable class
    item1 = Checkbutton(root, text="Sell Price Mean",
            variable=var, command=Mean("sellPrice"))
    item1.pack(anchor='w')
def Mean(var):
    global mean
    if mean != True:
      new_df[f"{var} Mean"] = new_df[var].mean(skipna=True, numeric_only=True)
      mean = True
      print(new_df)
    else:
        mean = False

    
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

var4 = IntVar()  # variable class
item4 = Checkbutton(root, text="Sell Price",
        variable=var4, command=selectItems4)
item4.pack(anchor='w')

var5 = IntVar()  # variable class
item5 = Checkbutton(root, text="Bedrooms",
        variable=var5, command=selectItems5)
item5.pack(anchor='w')

var6 = IntVar()  # variable class
item6 = Checkbutton(root, text="Bathrooms",
        variable=var6, command=selectItems6)
item6.pack(anchor='w')

var7 = IntVar()  # variable class
item7 = Checkbutton(root, text="Car Spaces",
        variable=var7, command=selectItems7)
item7.pack(anchor='w')

var8 = IntVar()  # variable class
item8 = Checkbutton(root, text="Property Types",
        variable=var8, command=selectItems8)
item8.pack(anchor='w')

itemd = Button(root, text="Display", command=Table)
itemd.pack(anchor='w')

iteme = Button(root, text="Exit", command=Exit)
iteme.pack(anchor='w')
root.mainloop()