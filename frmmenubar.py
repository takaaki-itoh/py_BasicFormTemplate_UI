'''
*******************************************************
* Use: Main menu bar construction class.
* file name: frmmenubar.py
* Ver. 2021. 4.18
* Developer: takaaki itoh
*******************************************************
'''
import sys
import tkinter as tk
from PIL import Image, ImageTk
from frmmenufunc import MenuFunc

class FormApplication(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        # Window size specification
        master.geometry("800x600")
        # ﾀｲﾄﾙ設定
        master.title("takaaki itoh")
        # Title setting
        menubr = tk.Menu(master)
        master.config(menu=menubr)
        # Item setting in the menu bar
        menu_ctrl = tk.Menu(menubr, tearoff=0)
        menubr.add_cascade(label='operation', menu=menu_ctrl)
        menu_databasectrl = tk.Menu(menubr,tearoff=0)
        menubr.add_cascade(label='Database', menu=menu_databasectrl)
        menu_view = tk.Menu(menubr, tearoff=0)
        menubr.add_cascade(label='display', menu=menu_view)
        menu_info = tk.Menu(menubr, tearoff=0)
        menubr.add_cascade(label='information', menu=menu_info)

        ### Instance of class for menu implementation
        func = MenuFunc() 
        ### Add child menu to parent menu
        # Operation items
        menu_ctrl.add_command(label='Connection test', command=func.ctrl_01)
        menu_ctrl.add_separator()
        menu_ctrl.add_command(label='Exit', command=func.ctrl_exit)
        # Database items
        menu_databasectrl.add_command(label='Initial setting', command=func.databasectrl_01)
        menu_databasectrl.add_separator()
        menu_databasectrl.add_command(label='Master registration', command=func.databasectrl_02)
        menu_databasectrl.add_separator()
        menu_databasectrl.add_command(label='Record registration', command=func.databasectrl_03)
        # Display items
        menu_view.add_command(label='Get database list', command=func.view_list)
        menu_view.add_separator()
        menu_view.add_command(label='Database search', command=func.view_search)
        # Information item
        menu_info.add_command(label='Developer', command=func.info_developer)
        menu_info.add_separator()
        menu_info.add_command(label='Version', command=func.info_version)

    def create_widgets(self):
        # Image settings
        read_image = Image.open('candy800600.png')
        # canvas create
        self.itoh_canvas = tk.Canvas(self, width=read_image.width, height=read_image.height)
        self.itoh_canvas.grid(row=0, column=0)
        # Image display on canvas
        img = ImageTk.PhotoImage(image=read_image)
        self.itoh_canvas.photo = img
        self.itoh_canvas.create_image(0, 0, anchor='nw', image=self.itoh_canvas.photo)

    def quit(self):
        sys.exit()




