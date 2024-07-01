### DOC LINK: https://docs.python.org/3/library/tkinter.html

from tkinter import *

window = Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

window.config(padx=100, pady=200)


#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

def button_clicked():
    
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#Button
botton = Button(text="Click Me", command=button_clicked)
botton.grid(column=1, row=1)

new_botton = Button(text="New Button", command=button_clicked)
new_botton.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=4, row=2)


window.mainloop()
