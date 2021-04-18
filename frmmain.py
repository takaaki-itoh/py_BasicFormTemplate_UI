'''
*******************************************************
* Python: Entry point.
* Python ver.3.8.5
* file name: frmmain.py
* Ver. 2021. 4.18
* Developer: takaaki itoh
*******************************************************
'''
import tkinter as tk
from frmmenubar import FormApplication

# Application main
def main():
    win = tk.Tk()
    app = FormApplication(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()

