from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import time
import os
os.system('cls') #Clearing the terminal
var = None
var2 = None
var3 = None
var4 = None
var5 = None
var6 = None
var7 = None
var8 = None
item1 = None
item2 = None
item3 = None
item4 = None
item5 = None
item6 = None
item7 = None
item8 = None
root = Tk() #Defining the GUI
root.title("Sydney House Prices Inflation") #GUI name
root.configure(background= "white") #Background colour
root.maxsize(10000,10000) #Max GUI size
root.minsize(500,500) #Min GUI size
root.geometry("500x500+20+100")
changed = False #For the display function
Thje_df = pd.read_csv('SydneyHousePrices.csv') #Defining the dataset
Thje_df = Thje_df.drop(columns=['Id']) #Removing something useless.
text = Label(root, text="STEP 1:")  #Text within the GUI
text.pack() #Add it
text2 = Label(root, text="Check options to be removed from dataset.") #Instructions
text2.pack() #Add it
new_df = Thje_df
previous_df = new_df
Columns_renamed = []
def selectItems(var,string):
    global new_df, changed, previous_df, Thje_df
    if  var.get():  # If the button is checked,    
        changed = True
        previous_df = new_df.copy()
        new_df = new_df.drop(columns=[string])  # Print print the cb's text
        print(f"{string} should've been removed")
    else:      
       new_df[string] = Thje_df[string]
def Table():
        global new_df
        print(new_df)  # Print print the cb's text
        time.sleep(5)
        os.system('cls')
#For Bugtesting
def Next_Step():
    global root, text, new_df, Thje_df, Columns, Columns_renamed
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
        Columns_renamed.append("sellPrice")
        var0 = True
    except:
        None
    try:
      if Thje_df["bed"].equals(new_df["bed"]):
          Columns.append("Bedroom Count")
          Columns_renamed.append("bed")
          var1 = True
    except:
        None
    try:
      if Thje_df["bath"].equals(new_df["bath"]):
        Columns.append("Bathroom Count")
        Columns_renamed.append("bath")
        var2 = True
    except:
        None
    try:
      if Thje_df["car"].equals(new_df["car"]):
        Columns.append("Car Space Count")
        Columns_renamed.append("car")
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
            command=lambda : Statistical_Command(clicked2.get(), clicked.get()))
    item9.pack(anchor='w')
    item10 = Button(root, text="Display",
            command=Table)
    item10.pack(anchor='w')
    item11 = Button(root, text="Graphing Step", command=Exit2)
    item11.pack(anchor='w')
    root.mainloop()
def Exit2():
    global root
    root.destroy()
    Final_Step()
def Final_Step():
    global root
    root = Tk()
    root.title("Graphing")
    root.configure(background = "white")
    root.maxsize(10000,10000)
    root.minsize(500,500)
    root.geometry("500x500+20+20")
    text = Label(root, text="STEP 3")
    text.pack()
    text2 = Label(root, text="Choose type of graph and aesthetic options.")
    text2.pack()
    clicked = StringVar()
    clicked.set("(Placeholder)")
    graphs = ["Plot", "Scatter", "Bar", "Stem", "Step", "Fill_Between", "StackPlot", "ImShow", "PcolorMesh", "Contour", "Contourf", "Barbs", "Quiver", "Streamplot", "Hist", "BoxPlot", "Errorbar", "ViolinPlot", "Eventplot", "Hist2d", "HexBin", "Pie", "Tricontour", "Tricontourf", "Tripcolor", "Triplot", "3D ScatterPlot", "3D Surface", "Triangular 3D Surfaces", "Volumetric", "3D wireframe"]
    drop = OptionMenu(root, clicked, *graphs)
    drop.pack()
def Statistical_Command(var1,var2):
    global Columns, Columns_renamed
    var1 = var1.get() if isinstance(var1, (StringVar, IntVar)) else var1
    var2 = var2.get() if isinstance(var2, (StringVar, IntVar)) else var2
    column_map = {
        "Sell Price": "sellPrice",
        "Bedroom Count": "bed",
        "Bathroom Count": "bath",
        "Car Space Count": "car",
        "All": "All"
    }
    var1 = column_map.get(var1, var1)
    try:
      if var1 == "All":
          for i in Columns_renamed:
           Stats(i,var2)
      else:
        Stats(var1, var2)          
      print(var1, var2)

    except():
        print("Error")
def Stats(var1, var2):
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
         All(var1)
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
      new_df[f"{var} Lower Quartile"] = new_df[var].quantile(q= 0.25)
      print(new_df)
def UQ(var):
      global new_df
      new_df[f"{var} Upper Quartile"] = new_df[var].quantile(q= 0.75)
      print(new_df)
def range(var):
      global new_df
      new_df[f"{var} Range"] = new_df[var].max(skipna = True, numeric_only=True) - new_df[var].min(skipna = True, numeric_only=True)
      print(new_df)
def IQrange(var):
        global new_df
        new_df[f"{var} Interquartile Range"] = new_df[var].quantile(q=0.75)-new_df[var].quantile(q=0.25)
def All(var):
    Mean(var)
    Median(var)
    Max(var)
    Min(var)
    range(var)
    LQ(var)
    UQ(var)
    IQrange(var)

def Checkbuttons(var,item,string,string2):
    global root
    var = IntVar()  # variable class
    item = Checkbutton(root, text=string,
        variable=var, command=lambda: selectItems(var,string2))
    item.pack(anchor='w')
Checkbuttons(var,item1,"Date", "Date")
Checkbuttons(var2, item2, "Suburb", "suburb")
Checkbuttons(var3, item3, "Postal Code", "postalCode")
Checkbuttons(var4, item4, "Sell Price", "sellPrice")
Checkbuttons(var5, item5, "Bedrooms", "bed")
Checkbuttons(var6, item6, "Bathrooms", "bath")
Checkbuttons(var7, item7, "Car Spaces", "car")
Checkbuttons(var8, item8, "Property Types", "propType")
itemd = Button(root, text="Display", command=Table)
itemd.pack(anchor='w')

iteme = Button(root, text="Next Step", command=Next_Step)
iteme.pack(anchor='w')
root.mainloop()