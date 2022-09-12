
from tkinter import * 
from tkinter import ttk

root = Tk()

root.geometry("500x500")

pw = PanedWindow(orient ='vertical')

top = ttk.Button(pw, text ="Click Me !\nI'm a Button")
top.pack(side = TOP)

pw.add(top)

# Checkbutton Widget
bot = Checkbutton(pw, text ="Choose Me !")
bot.pack(side = TOP)
  
# This will add Checkbutton to panedwindow
pw.add(bot)
  
# adding Label widget
label = Label(pw, text ="I'm a Label")
label.pack(side = TOP)
  
pw.add(label)
  
# Tkinter string variable
string = StringVar()
  
# Entry widget with some styling in fonts
entry = Entry(pw, textvariable = string, font =('arial', 15, 'bold'))
entry.pack()
  
# Focus force is used to focus on particular
# widget that means widget is already selected for operations
entry.focus_force()
  
pw.add(entry)

pw.pack(fill = BOTH, expand = True)

pw.configure(sashrelief = RAISED)

mainloop()