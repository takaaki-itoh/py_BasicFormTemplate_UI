'''
*******************************************************
* Use: Base form when adding a new form
* file name: frmbase.py
* Ver. 2021. 4.18
* Developer: takaaki itoh
*******************************************************
'''
import tkinter as tk
import tkinter.messagebox as mb

class FormBase(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # Window size specification
        master.geometry("800x600")
        # Title setting
        master.title("Base Form")
        # Menu bar creation
        menubr = tk.Menu(master)
        master.config(menu=menubr)
        # Add child menu item to menu bar
        menu_ctrl = tk.Menu(menubr, tearoff=0)
        menubr.add_cascade(label='操作', menu=menu_ctrl)
        # Add menu to child menu and Event addition
        menu_ctrl.add_command(label='Operation of something', command = mb.showinfo)
        menu_ctrl.add_separator()
        menu_ctrl.add_command(label='Exit', command = quit)


    def ctrl_01(self):
        mb.showinfo("takaaki itoh", "Describe some processing.")

    def quit(self):
        self.destroy()