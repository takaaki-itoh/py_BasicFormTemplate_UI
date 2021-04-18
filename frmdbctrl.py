'''
*******************************************************
* For example: Mysql Connection Form. and Database operation item.
* file name: frmdbctl.py
* Ver. 2021. 4.18
* Developer: takaaki itoh
*******************************************************
'''
import tkinter as tk
import tkinter.messagebox as mb
from frmbase import FormBase


class DataBaseCtrl(FormBase):
    def __init__(self, master, titlebar, sw):
        super().__init__(master)
        self.pack()
        # Title setting
        self.master.title(titlebar)
        # Menu bar creation
        self.menubr = tk.Menu(master)
        self.master.config(menu=self.menubr)
        # Create default parent menu item in menu bar
        menu_ctrl = tk.Menu(self.menubr, tearoff=0)
        self.menubr.add_cascade(label='operation', menu=menu_ctrl)
        # Operation item menu
        menu_ctrl.add_command(label='Exit', command=quit)

        # Label 
        self.label1 = tk.Label(self,text="The character string you want to display")
        self.label1.place(x=0, y=100)
        self.label1.pack()
        canvas = tk.Canvas(self, width=800, height=600, bg="#336699")
        canvas.place(x=100, y=100)
        canvas.pack()
        label_fname = tk.Label(self, text='【first name】', font=("Times New Roman", 12), fg="blue", bg="skyblue")
        label_fname.place(x=230, y=100)
        fnamebox = tk.Entry(self, font=("Times New Roman", 12), width=30)
        fnamebox.place(x=330, y=100)
        label_lname= tk.Label(self, text='【last name】', font=("Times New Roman", 12), fg="blue", bg="skyblue")
        label_lname.place(x=230, y=150)
        lnamebox = tk.Entry(self, font=("Times New Roman", 12), width=30)
        lnamebox.place(x=330, y=150)
        button = tk.Button(self, text='Registration', font=("Times New Roman", 12), command=self.msg, bg="skyblue")
        button.place(x=230, y=240)
 
    def msg(self):
        print("takaaki itoh", "Registration OK!\nProcessing description as needed")

    def quit(self):
        self.destroy()

