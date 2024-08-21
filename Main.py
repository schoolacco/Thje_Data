from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import time
import os
import numpy as np
plt.style.use('_mpl-gallery')
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
def Take_input():
    global inputtxt
    INPUT = inputtxt.get("1.0", "end-1c")
    return INPUT
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
def Forgor_step():
    global root, text, new_df, Thje_df
    root.destroy()
    root = Tk()
    root.title("Bonus Measurements") #GUI name
    root.configure(background= "white") #Background colour
    root.maxsize(10000,10000)
    root.minsize(500,500)
    root.geometry("500x500+20+100")
    text = Label(root, text="STEP 1.5:") 
    text.pack()
    text2 = Label(root, text="More Filtering")
    text2.pack()
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
    global root, inputtxt, INPUT
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
    clicked2 = StringVar()
    clicked2.set("(Placeholder)")
    clicked3 = StringVar()
    clicked3.set("(Placeholder)")
    clicked4 = StringVar()
    clicked4.set("(Placeholder)")
    clicked5 = StringVar()
    clicked5.set("(Placeholder)")
    graphs = ["Plot", "Scatter", "Bar", "Stem", "Step", "Fill_Between", "StackPlot", "Hist", "BoxPlot", "Errorbar", "ViolinPlot", "Eventplot", "Hist2d", "HexBin", "Pie"]
    x_options = new_df.head()
    y_options = new_df.head()
    z_options = new_df.head()
    text4 = Label(root, text="Graph Type")
    text4.pack()
    drop = OptionMenu(root, clicked, *graphs)
    drop.pack()
    text5 = Label(root, text="X value")
    text5.pack()
    drop2 = OptionMenu(root, clicked2, *x_options)
    drop2.pack()
    text6 = Label(root, text="Y Value")
    text6.pack()
    drop3 = OptionMenu(root,clicked3, *y_options)
    drop3.pack()
    text7 = Label(root, text="Z Value (for 3D, never implemented)")
    text7.pack()
    drop4 = OptionMenu(root, clicked4, *z_options)
    drop4.pack()
    text8 = Label(root, text="Extra y value for some graphs")
    text8.pack()
    drop5 = OptionMenu(root,clicked5, *y_options)
    drop5.pack()
    text3 = Label(root, text="Note that only the first 2 are of use unless you plan on using a more particular graph.")
    text3.pack()
    Label(text = "What is 24 * 5 ? ").pack()
    inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
    inputtxt.pack()
    try:
        var = int(Take_input())
    except:
        var = None
    Thatisit = Button(root, text = 'Graph', command = lambda: Graph(clicked.get(), clicked2.get(), clicked3.get(), clicked4.get(), clicked5.get(), var))
    Thatisit.pack(anchor='w')
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
def Graph(t,x,y,z,y2,yerr):
    global new_df
    x = new_df[x]
    y = new_df[y]    
    try:
      if t == "Bar":
       fig, ax = plt.subplots()
       ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
       ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
         ylim=(0, 8), yticks=np.arange(1, 8))
  
       plt.show()
      elif t == 'Plot':
          fig, ax = plt.subplots()
          
          ax.plot(x, y, linewidth=2.0)
          
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 8), yticks=np.arange(1, 8))
          
          plt.show()
      elif t == "Scatter":
          fig, ax = plt.subplots()
          sizes = np.random.uniform(15, 80, len(x))
          colors = np.random.uniform(15, 80, len(x))
          ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
          
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 8), yticks=np.arange(1, 8))
          
          plt.show()
      elif t == "Stem":
          fig, ax = plt.subplots()
          
          ax.stem(x, y)
          
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 8), yticks=np.arange(1, 8))
          
          plt.show()
      elif t == "Step":
          fig, ax = plt.subplots()
          
          ax.step(x, y, linewidth=2.5)
          
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 8), yticks=np.arange(1, 8))
          
          plt.show()
      elif t == 'Fill_Between':
          fig, ax = plt.subplots()
          y1 = y
          ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
          ax.plot(x, (y1 + y2)/2, linewidth=2)
          
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 8), yticks=np.arange(1, 8))
  
          plt.show()
      elif t == 'StackPlot':
          fig, ax = plt.subplots()
  
          ax.stackplot(x, y)
          
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 8), yticks=np.arange(1, 8))
          
          plt.show()
      elif t == 'Hist' and np.array_equal(new_df.x, new_df.x.astype(int)):
          fig, ax = plt.subplots()
  
          ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")
          
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 56), yticks=np.linspace(0, 56, 9))
          
          plt.show()
      elif t == 'BoxPlot' and np.array_equal(new_df.x, new_df.x.astype(int)):
          VP = ax.boxplot(x, positions=[2, 4, 6], widths=1.5, patch_artist=True,
                  showmeans=False, showfliers=False,
                  medianprops={"color": "white", "linewidth": 0.5},
                  boxprops={"facecolor": "C0", "edgecolor": "white",
                            "linewidth": 0.5},
                  whiskerprops={"color": "C0", "linewidth": 1.5},
                  capprops={"color": "C0", "linewidth": 1.5})
  
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
          ylim=(0, 8), yticks=np.arange(1, 8))
          plt.show()
      elif t == 'Errorbar' and yerr.is_integer():
        fig, ax = plt.subplots()
  
        ax.errorbar(x, y, yerr, fmt='o', linewidth=2, capsize=6)
  
        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))
  
        plt.show()
      elif t == 'ViolinPlot' and np.array_equal(new_df.x, new_df.x.astype(int)):
          fig, ax = plt.subplots()
          
          vp = ax.violinplot(x, [2, 4, 6], widths=2,
                             showmeans=False, showmedians=False, showextrema=False)
          # styling:
          for body in vp['bodies']:
              body.set_alpha(0.9)
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 8), yticks=np.arange(1, 8))
          
          plt.show()
      elif t == "Eventplot" and np.array_equal(new_df.x, new_df.x.astype(int)):
          fig, ax = plt.subplots()

          ax.eventplot(x, orientation="vertical", lineoffsets=x, linewidth=0.75)
          
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 8), yticks=np.arange(1, 8))
          
          plt.show()
      elif t == 'Hist2d' and np.array_equal(new_df.x, new_df.x.astype(int)) and np.array_equal(new_df.y, new_df.y.astype(int)):
          fig, ax = plt.subplots()
          
          ax.hist2d(x, y, bins=(np.arange(-3, 3, 0.1), np.arange(-3, 3, 0.1)))
          
          ax.set(xlim=(-2, 2), ylim=(-3, 3))
          
          plt.show()
      elif t == 'HexBin' and np.array_equal(new_df.x, new_df.x.astype(int)) and np.array_equal(new_df.y, new_df.y.astype(int)):
          fig, ax = plt.subplots()

          ax.hexbin(x, y, gridsize=20)
          
          ax.set(xlim=(-2, 2), ylim=(-3, 3))
          
          plt.show()
      elif t == 'Pie':
          colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
          fig, ax = plt.subplots()
          ax.pie(x, colors=colors, radius=3, center=(4, 4),
                 wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
          
          ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                 ylim=(0, 8), yticks=np.arange(1, 8))
          
          plt.show()
    except:
        print("Sorry... you either entered in an invalid value for the type of graph or maybe the graph itself was never valid.")
root.mainloop()