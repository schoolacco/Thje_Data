from tkinter import *
root = Tk()
root.title("Epik GUI")
root.configure(background= "black")
root.maxsize(1000,1000)
root.minsize(100,100)
root.geometry("500x500+20+100")


#Label Test
text = Label(root, text="It's a GUI :D")
text.pack()
text2 = Label(root, text="Yipee!")
text2.pack()
root.mainloop()