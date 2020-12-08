import tkinter as tk

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
]

app = tk.Tk()

app.geometry('400x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))

variable.trace("w", callback)

app.mainloop()

######################################################################


# from tkinter import *
#
# root = Tk()
# root.title("Drop-down boxes for option selections.")
#
# var = StringVar(root)
# var.set("drop down menu button")
#
# def grab_and_assign(event):
#     chosen_option = var.get()
#     label_chosen_variable= Label(root, text=chosen_option)
#     label_chosen_variable.grid(row=1, column=2)
#     print(chosen_option)
#
# drop_menu = OptionMenu(root, var,  "one", "two", "three", "four", "meerkat", command=grab_and_assign)
# drop_menu.grid(row=0, column=0)
#
# label_left=Label(root, text="chosen variable= ")
# label_left.grid(row=1, column=0)
#
# root.mainloop()