from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
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
Thje_df = pd.read_csv('SydneyHousePrices.csv') #Defining the dataset
Thje_df = Thje_df.drop(columns=['Id']) #Removing something useless.
#Text Test
text = Label(root, text="STEP 1:") 
text.pack()
text2 = Label(root, text="Check options to be removed from dataset.")
text2.pack()
new_df = Thje_df
previous_df = new_df
def selectItems(var,string):
    global new_df, changed, previous_df
    if  var.get():  # If the button is checked,    
        changed = previous_df = new_df
        return new_df == previous_df.drop(columns=[string])  # Print print the cb's text
    else:      
       return new_df[string] == previous_df[string]
def Table():
        global new_df, changed
        df_var = new_df
        if changed != True:
             df_var = Thje_df
        print(df_var)  # Print print the cb's text
        time.sleep(5)
        os.system('cls')
#For Bugtesting
def Next_Step():
    global root, text, new_df, Thje_df, Columns
    root.destroy()
    root = Tk()
    root.title("Bonus Measurements") #GUI name
    root.configure(background= "white") #Background colour
    root.maxsize(10000,10000)
    root.minsize(500,500)
    root.geometry("500x500+20+100")
    text = Label(root, text="STEP 2:") 
    text.pack()
    text2 = Label(root, text="Choose extra measurements to be added to the data.")
    text2.pack()
    options = [ 
    "(None)",
    "Mean",
    "Median",
    "Highest Value",
    "Lowest Value",
    "Range",
    "Lower Quartile",
    "Upper Quartile",
    "Interquartile Range",
    "All"
    ] 
    clicked = StringVar() 
    clicked.set( "(None)" ) 
    drop = OptionMenu( root , clicked , *options ) 
    drop.pack() 
    Columns = ["(None)"]
    try:
      if Thje_df["sellPrice"].equals(new_df["sellPrice"]):
        Columns.append("Sell Price")
        var0 = True
    except:
        None
    try:
      if Thje_df["bed"].equals(new_df["bed"]):
          Columns.append("Bedroom Count")
          var1 = True
    except:
        None
    try:
      if Thje_df["bath"].equals(new_df["bath"]):
        Columns.append("Bathroom Count")
        var2 = True
    except:
        None
    try:
      if Thje_df["car"].equals(new_df["car"]):
        Columns.append("Car Space Count")
        var3 = True
    except:
        None
    try:
        if var1 == var2 == var3 == var0 == True:
            Columns.append("All")
    except:
        None
    clicked2 = StringVar() 
    clicked2.set( "Default" ) 
    drop2 = OptionMenu( root , clicked2 , *Columns ) 
    drop2.pack() 
    item9 = Button(root, text="Add",
            command=Statistical_Command(clicked.get(), clicked2.get()))
    item9.pack(anchor='w')
    item10 = Button(root, text="Display",
            command=Table)
    item10.pack(anchor='w')
    root.mainloop()
def Statistical_Command(var1,var2):
    global Columns
    if var1 == "Sell Price":
        var1 == "sellPrice"
    elif var1 == "Bedroom Count":
        var1 == "bed"
    elif var1 == "Bathroom Count":
        var1 == "bath"
    elif var1 == "Car Space Count":
        var1 == "car"
    if var1 == "All":
        for var1 in Columns:
          if var2 == "Mean":
              Mean(var1)
          elif var2 == "Median":
              Median(var1)
          elif var2 == "Highest Value":
              Max(var1)
          elif var2 == "Lowest Value":
              min(var1)
          elif var2 == "Range":
              range(var1)
          elif var2 == "Lower Quartile":
              LQ(var1)
          elif var2 == "Upper Quartile":
              UQ(var1)
          elif var2 == "Interquartile Range":
              IQrange(var1)
          elif var2 == "All":
             All(var)
    if var2 == "Mean":
        Mean(var1)
    elif var2 == "Median":
        Median(var1)
    elif var2 == "Highest Value":
        Max(var1)
    elif var2 == "Lowest Value":
        min(var1)
    elif var2 == "Range":
        range(var1)
    elif var2 == "Lower Quartile":
        LQ(var1)
    elif var2 == "Upper Quartile":
        UQ(var1)
    elif var2 == "Interquartile Range":
        IQrange(var1)
    elif var2 == "All":
       All(var)
def Mean(var):
      global new_df
      new_df[f"{var} Mean"] = new_df[var].mean(skipna=True, numeric_only=True)
      print(new_df)
def Median(var):
      global new_df
      new_df[f"{var} Median"] = new_df[var].median(skipna=True, numeric_only=True)
      print(new_df)
def Max(var):
      global new_df
      new_df[f"{var} Maximum"] = new_df[var].max(skipna=True, numeric_only=True)
      print(new_df)
def Min(var):
      global new_df
      new_df[f"{var} Minimum"] = new_df[var].min(skipna=True, numeric_only=True)
      print(new_df)
def LQ(var):
      global new_df
      new_df[f"{var} Lower Quartile"] = new_df[var].quantile(q= 0.25, skipna=True, numeric_only=True)
      print(new_df)
def UQ(var):
      global new_df
      new_df[f"{var} Upper Quartile"] = new_df[var].quantile(q= 0.75, skipna=True, numeric_only=True)
      print(new_df)
def range(var):
      global new_df
      new_df[F"{var} Range"] = new_df[var].max(skipna = True, numeric_only=True) - new_df[var].min(skipna = True, numeric_only=True)
      print(new_df)
def IQrange(var):
        global new_df
        new_df[F"{var} Interquartile Range"] = new_df[var].quantile(q=0.75, skipna = True, numeric_only = True)-new_df[var].quantile(q=0.25, skipna = True, numeric_only = True)
def All(var):
    Mean(var)
    Median(var)
    Max(var)
    Min(var)
    range(var)
    LQ(var)
    UQ(var)
    IQrange(var)
var = IntVar()  # variable class
item1 = Checkbutton(root, text="Date",
        variable=var, command=selectItems(var,"Date"))
item1.pack(anchor='w')


var2 = IntVar()  # variable class
item2 = Checkbutton(root, text="Suburb",
        variable=var2, command=selectItems(var2,"suburb"))
item2.pack(anchor='w')

var3 = IntVar()  # variable class
item3 = Checkbutton(root, text="Postal Code",
        variable=var3, command=selectItems(var3,"postalCode"))
item3.pack(anchor='w')

var4 = IntVar()  # variable class
item4 = Checkbutton(root, text="Sell Price",
        variable=var4, command=selectItems(var4,"sellPrice"))
item4.pack(anchor='w')

var5 = IntVar()  # variable class
item5 = Checkbutton(root, text="Bedrooms",
        variable=var5, command=selectItems(var5,"bed"))
item5.pack(anchor='w')

var6 = IntVar()  # variable class
item6 = Checkbutton(root, text="Bathrooms",
        variable=var6, command=selectItems(var6,"bath"))
item6.pack(anchor='w')

var7 = IntVar()  # variable class
item7 = Checkbutton(root, text="Car Spaces",
        variable=var7, command=selectItems(var7,"car"))
item7.pack(anchor='w')

var8 = IntVar()  # variable class
item8 = Checkbutton(root, text="Property Types",
        variable=var8, command=selectItems(var8,"propType"))
item8.pack(anchor='w')

itemd = Button(root, text="Display", command=Table)
itemd.pack(anchor='w')

iteme = Button(root, text="Next Step", command=Next_Step)
iteme.pack(anchor='w')
root.mainloop()