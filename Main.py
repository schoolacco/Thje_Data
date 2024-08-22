from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import time
import os
import numpy as np
plt.style.use('_mpl-gallery')
try:
    os.system('clear') #If not Windows
except:
    None
try:
    os.system('cls')
except:
    None
# Define all the below variables as None
var = var2 = var3 = var4 = var5 = var6 = var7 = var8 = item1 = item2 = item3 = item4 = item5 = item6 = item7 = item8 = None
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
new_df = Thje_df #Quick definiton
previous_df = new_df #For reasons
Columns_renamed = [] #Setting up for later
def Take_input(): 
    global inputtxt
    INPUT = inputtxt.get("1.0", "end-1c") #This is how you recieve an input via tkinter
    return INPUT #Return it of course
def selectItems(var,string):
    global new_df, changed, previous_df, Thje_df
    if  var.get():  # If the button is checked,    
        changed = True #No longer needed, but I'm lazy
        previous_df = new_df.copy() #Just in case
        new_df = new_df.drop(columns=[string])  # Remove the column
        print(f"{string} should've been removed") #Debugging
    else:      
       new_df[string] = Thje_df[string] #Simple, bring back the column
def Table():
        global new_df
        subroot = Tk() #Create new GUI
        subroot.title("Data Frame") #Title
        Label(subroot, text=new_df).pack() # Show the dataframe.
#For Bugtesting
def Forgor_step():
    global root, text, new_df, Thje_df
    root.destroy() #Get rid of the previous
    root = Tk() #New GUI
    root.title("Bonus Measurements") #GUI name
    root.configure(background= "white") #Background colour
    root.maxsize(10000,10000) 
    root.minsize(500,500)
    root.geometry("500x500+20+100")
    text = Label(root, text="STEP 1.5:") #Step count
    text.pack()
    text2 = Label(root, text="More Filtering.") #Subject to change
    text2.pack()
    clicked = StringVar() #Reasons
    clicked.set('Default') #Default
    clicked2 = StringVar() #Reasons
    clicked2.set('Default') #Default
    clicked3 = StringVar() #Reasons
    clicked3.set('Default') #Default
    Dates = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'] #A list
    Date_drop = OptionMenu(root, clicked, *Dates) #Creating an option Menu
    Date_drop.pack()
    variable = list(new_df["propType"].drop_duplicates())
    OptionMenu(root,clicked2, *variable).pack()
    variable2 = list(new_df["suburb"].drop_duplicates())
    OptionMenu(root,clicked3, *variable2).pack()
    # append the list to the final list
    Button(root, text = 'Filter by Date', command = lambda: Datefilter(clicked)).pack() #The Button for the filter, lambda is a requirement for more complex functions for some reason...
    Button(root, text = 'Filter by Property Type', command = lambda: Filter(clicked2, "propType")).pack()
    Button(root, text = 'Filter by Suburb', command = lambda: Filter(clicked3, "suburb")).pack()
    Button(root, text = 'Next Step', command = Next_Step).pack()
    Button(root, text = 'Display', command = Table).pack()
def Datefilter(clicked):
  global previous_df, new_df
  previous_df=new_df
  try:
    new_df.loc[f'{clicked.get()}-01-01':f'{clicked.get()}-12-31'] #Remove all dates but those within the given year.
  except:
      new_df = previous_df
def Filter(clicked,Type):
  global new_df, previous_df
  previous_df = new_df
  try:
    new_df = new_df.drop(new_df[new_df[Type] != clicked.get()].index)
  except:
      new_df = previous_df
def Next_Step():
    global root, text, new_df, Thje_df, Columns, Columns_renamed
    root.destroy() #Destroy the GUI
    root = Tk() #New GUI
    root.title("Bonus Measurements") #GUI name
    root.configure(background= "white") #Background colour
    root.maxsize(10000,10000)
    root.minsize(500,500)
    root.geometry("500x500+20+100")
    text = Label(root, text="STEP 2:") #Step Count
    text.pack()
    text2 = Label(root, text="Choose extra measurements to be added to the data.") #Instructions
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
    ] #List of statistics
    clicked = StringVar()  #For later
    clicked.set( "(None)" ) #Default
    drop = OptionMenu( root , clicked , *options ) #Creating an options menu for the statistical options
    drop.pack() 
    Columns = ["(None)"] #Default
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
# It can all be summarised as checking for a column and then adding it to possible columns
    clicked2 = StringVar() 
    clicked2.set( "Default" ) 
    drop2 = OptionMenu( root , clicked2 , *Columns ) #An options menu for the columns
    drop2.pack() 
    item9 = Button(root, text="Add",
            command=lambda : Statistical_Command(clicked2.get(), clicked.get())) #A button that the statistical commands based on the options menu 
    item9.pack(anchor='w')
    item10 = Button(root, text="Display", #Debugging
            command=Table)
    item10.pack(anchor='w')
    item11 = Button(root, text="Graphing Step", command=Exit2) #Final Step
    item11.pack(anchor='w')
    root.mainloop()
def Exit2():
    global root
    root.destroy() #Destroy the GUI
    Final_Step() #Wait... why did I do this?
def Final_Step():
    global root, inputtxt
    root = Tk() 
    root.title("Graphing")
    root.configure(background="white")
    root.maxsize(10000, 10000)
    root.minsize(500, 500)
    root.geometry("500x500+20+20")

    text = Label(root, text="STEP 3") #Step Count
    text.pack()
    text2 = Label(root, text="Choose type of graph.") #Instructions
    text2.pack()

    graphs = [
        "Plot", "Scatter", "Bar", "Stem", "Step", "Fill_Between", "StackPlot",
        "Hist", "BoxPlot", "Errorbar", "ViolinPlot", "Eventplot", "Hist2d",
        "HexBin", "Pie", "Table", "Csv"
    ] #Graph list, not all of them work
    columns = new_df.columns.tolist() #Nessecary
    
    clicked = StringVar()
    clicked.set("Plot")
    clicked2 = StringVar()
    clicked2.set(columns[0])
    clicked3 = StringVar()
    clicked3.set(columns[0])
    clicked4 = StringVar()
    clicked4.set(columns[0])
    clicked5 = StringVar()
    clicked5.set(columns[0])

    Label(root, text="Graph Type").pack()
    OptionMenu(root, clicked, *graphs).pack()

    Label(root, text="X value").pack()
    OptionMenu(root, clicked2, *columns).pack()

    Label(root, text="Y Value").pack()
    OptionMenu(root, clicked3, *columns).pack()

    Label(root, text="Z Value (for 3D)").pack()
    OptionMenu(root, clicked4, *columns).pack()

    Label(root, text="Extra y value for some graphs").pack()
    OptionMenu(root, clicked5, *columns).pack()

    text3 = Label(root, text="Note that only the first 2 are of use unless you plan on using a more particular graph.")
    text3.pack()
    text4 = Label(root, text = "y error for a type of graph (integer only)")
    inputtxt = Text(root, height=10, width=25, bg="light yellow")
    inputtxt.pack()
    yerr = Take_input()
    Button(root, text='Graph', command=lambda: Graph(clicked.get(), clicked2.get(), clicked3.get(), clicked4.get(), clicked5.get(), yerr)).pack(anchor='w')
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

iteme = Button(root, text="Next Step", command= Forgor_step)
iteme.pack(anchor='w')

def Graph(t, x, y, z, y2, yerr):
    global new_df, root
    try:
        x_data = new_df[x]
        y_data = new_df[y]

        if t == "Table":
            root.destroy()
            root = Tk()
            root.title("Your data frame...")
            Label(root, text=new_df).pack()
            return

        fig, ax = plt.subplots()
        if t == "Bar":
            ax.bar(x_data, y_data, width=1, edgecolor="white", linewidth=0.7)
        elif t == 'Plot':
            ax.plot(x_data, y_data, linewidth=2.0)
        elif t == "Scatter":
            sizes = np.random.uniform(15, 80, len(x_data))
            colors = np.random.uniform(15, 80, len(x_data))
            ax.scatter(x_data, y_data, s=sizes, c=colors, vmin=0, vmax=100)
        elif t == "Stem":
            ax.stem(x_data, y_data)
        elif t == "Step":
            ax.step(x_data, y_data, linewidth=2.5)
        elif t == 'Fill_Between':
            y1 = y_data
            ax.fill_between(x_data, y1, y2, alpha=.5, linewidth=0)
            ax.plot(x_data, (y1 + y2) / 2, linewidth=2)
        elif t == 'StackPlot':
            ax.stackplot(x_data, y_data)
        elif t == 'Hist':
            ax.hist(x_data, bins=8, linewidth=0.5, edgecolor="white")
        elif t == 'BoxPlot':
            ax.boxplot(x_data, positions=[2, 4, 6], widths=1.5, patch_artist=True)
        elif t == 'Errorbar':
            if not np.issubdtype(type(yerr), np.number):
                raise ValueError("Invalid value for yerr")
            ax.errorbar(x_data, y_data, yerr, fmt='o', linewidth=2, capsize=6)
        elif t == 'ViolinPlot':
            ax.violinplot(x_data)
        elif t == "Eventplot":
            ax.eventplot(x_data, orientation="vertical")
        elif t == 'Hist2d':
            ax.hist2d(x_data, y_data, bins=(np.arange(-3, 3, 0.1), np.arange(-3, 3, 0.1)))
        elif t == 'HexBin':
            ax.hexbin(x_data, y_data, gridsize=20)
        elif t == 'Pie':
            colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x_data)))
            ax.pie(x_data, colors=colors, radius=3, center=(4, 4))
        elif t == 'Csv':
            new_df.to_csv('New_Csv.csv')
        else:
            print(f"Unknown plot type: {t}")
        plt.show()
    except:
        print("An error occured or maybe the graph never worked.")
root.mainloop()