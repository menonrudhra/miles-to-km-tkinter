from tkinter import *

# 1 mile = 1.609344 kilometres or 1.61 km
FONT_STYLE = ("Arial", 16)


# Function

def calculate_km():
    miles = float(input_entry.get())
    km = round(miles * 1.61)
    km_value_label.config(text=km)


# Window

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(pady=50, padx=50)

# Labels
null_label = Label()
null_label.grid(row=0, column=0)

miles_label = Label(text="Miles", font=FONT_STYLE)
miles_label.grid(row=0, column=2)

km_label = Label(text="Km", font=FONT_STYLE)
km_label.grid(row=1, column=2)

equals_label = Label(text="is equal to", font=FONT_STYLE)
equals_label.grid(row=1, column=0)

km_value_label = Label(text="0", font=FONT_STYLE)
km_value_label.grid(row=1, column=1)

# Text Entry

input_entry = Entry(width=10)
input_entry.insert(END, string="0")
print(input_entry.get())
input_entry.grid(column=1, row=0)

# Button

calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
