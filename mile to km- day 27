from tkinter import *


def calculate():
    mile_n = float(miles_input.get())
    rez = round(mile_n * 1.609)
    kilo.config(text=f"{rez}")


window = Tk()
window.title('Mile to Km Converter')
window.minsize(280,120)
window.config(padx=20, pady=20)

# input box
miles_input = Entry(width=8)
miles_input.grid(column=3, row=0)

# text on screen
miles = Label(text='Miles')
miles.grid(column=6, row=0)
equal_to = Label(text='is equal to ')
equal_to.grid(column=0, row=3)
km = Label(text='Km')
km.grid(column=6, row=3)
kilo = Label(text='0')
kilo.grid(column=3, row=3)

# button
button = Button(text='Calculate', command=calculate)
button.grid(column=3, row=4)


window.mainloop()
