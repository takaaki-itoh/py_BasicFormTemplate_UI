'''
*******************************************************
* Use: Class for implementing functions from the main menu bar to child menu items.
* file name: frmmenufunc.py
* Ver. 2021. 4.18
* Developer: takaaki itoh
*******************************************************
'''
import tkinter as tk
import tkinter.messagebox as mb
import sys
import frmbase
import frmdbctrl as db

class MenuFunc:
    def __init__(self):
       pass

    # Event called from menu operation
    def ctrl_01(self):
        mb.showinfo("operation", "Success!")
        
    def ctrl_exit(self):
        sys.exit()

    def databasectrl_01(self):
        subfrmdb = db 
        frmsub = tk.Tk()
        subfrmdb.DataBaseCtrl(frmsub, 'Database initialization', 1)

    def databasectrl_02(self):
        subfrmdb = db 
        frmsub = tk.Tk()
        subfrmdb.DataBaseCtrl(frmsub, 'Database master', 2)

    def databasectrl_03(self):
        pass

    def view_list(self):
        mb.showinfo("takakai itoh", "List display")
        
    def view_search(self):
        mb.showinfo("takakai itoh", "Search display")

    def info_developer(self):
        mb.showinfo("takakai itoh", "TAKAAKI ITOH")

    def info_version(self):
        mb.showinfo("takakai itoh", "Version 2021. 4.18")

