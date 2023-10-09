### DOC LINK: https://docs.python.org/3/library/tkinter.html

from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km:.4f}")


window = Tk()

window.title("Mile to Km Converter")

window.minsize(width=500, height=300)

window.config(padx=20, pady=20)


# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


#Label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.config(padx=10, pady=5)
miles_label.grid(column=2, row=0)


equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.config(text="is equal to")
equal_label.grid(column=0, row=2)


kilometer_result_label = Label(text="0", font=("Arial", 12, "bold"))
kilometer_result_label.config(padx=10, pady=5)
kilometer_result_label.grid(column=1, row=2)


km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.config(text="Km")
km_label.grid(column=2, row=2)


#Button
botton_calculate = Button(text="Calculate", command=miles_to_km)
botton_calculate.grid(column=1, row=4)


window.mainloop()
