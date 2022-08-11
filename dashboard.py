# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
#
#
# root = Tk()
#
# root.geometry("1200x800")
#
# root.title('Dashboard - Center')
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
#
# ttk.Label(root, text='Welcome').pack()

import tkinter as tk
# from tkHyperlinkManager import HyperlinkManager

root = tk.Tk()
root.title("Ohio Academy | DASHBOARD")


# Sections
titlebar = tk.Frame(width=500, height=50, bg='#06283D').pack()
navbar = tk.Frame(width=500, height=50, bg='#06283D').pack()
main = tk.Frame(width=500, height=500, bg="#DFF6FF").pack()
footer = tk.Frame(width=500, height=50, bg='#06283D').pack()


# Labels for the SECTIONS
tblabel = tk.Label(titlebar, text="OHIO ACADEMY", bg="#06283D", fg="white").place(x=210, y=10)
navdashboard = tk.Button(navbar, text="Dashboard", bg="#06283D", fg="white").place(x=20, y=60)
navcourses = tk.Button(navbar, text="Courses", bg="#06283D", fg="white").place(x=100, y=60)
navcalendar = tk.Button(navbar, text="Calendar", bg="#06283D", fg="white").place(x=180, y=60)
navfees = tk.Button(navbar, text="Fees", bg="#06283D", fg="white").place(x=240, y=60)
navbooks = tk.Button(navbar, text="Books", bg="#06283D", fg="white").place(x=320, y=60)
navsettings = tk.Button(navbar, text="Settings", bg="#06283D", fg="white").place(x=400, y=60)
footerlabel = tk.Button(footer, text="@ Copyright 2022 || Ohio Academy", bg="#06283D", fg="white").place(x=150, y=610)


# Grid the main
# tk.Label(root, ).grid(column=4,row=5)

root.mainloop()


root.mainloop()