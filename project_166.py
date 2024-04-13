from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PROJECT 166")
root.geometry("500x500")

canvas = Canvas(root, width = 990, height = 490, bg = "white", highlightbackground = "grey")
canvas.pack()

color_label = Label(root, text = "Choose Clour :- ")
color_label.place(relx = 0.6, rely = 0.9, anchor = CENTER)

fill_colour = ["Green", "Cyan", "Blue", "Magenta"]

colour_dropdown = ttk.Combobox(root, state = "readonly", values = fill_colour, width = 10)
colour_dropdown.place(relx = 0.8, rely = 0.9, anchor = CENTER)

coordinates_value = [10, 50, 100, 200, 300, 400, 500, 600, 800, 900]

startx = Label(root, text = "startx")
startx.place(relx = 0.1, rely = 0.85, anchor = CENTER)

d1 = ttk.Combobox(root, state = "readonly", values = coordinates_value, width = 10)
d1.place(relx = 0.2, rely = 0.85, anchor = CENTER)

starty = Label(root, text = "starty")
starty.place(relx = 0.3, rely = 0.85, anchor = CENTER)

d2 = ttk.Combobox(root, state = "readonly", values = coordinates_value, width = 10)
d2.place(relx = 0.4, rely = 0.85, anchor = CENTER)

endx = Label(root, text = "endx")
endx.place(relx = 0.5, rely = 0.85, anchor = CENTER)

d3 = ttk.Combobox(root, state = "readonly", values = coordinates_value, width = 10)
d3.place(relx = 0.6, rely = 0.85, anchor = CENTER)

endy = Label(root, text = "endy")
endy.place(relx = 0.7, rely = 0.85, anchor = CENTER)

d4 = ttk.Combobox(root, state = "readonly", values = coordinates_value, width = 10)
d4.place(relx = 0.8, rely = 0.85, anchor = CENTER)

root.mainloop()
