### DOC LINK: https://docs.python.org/3/library/tkinter.html

from tkinter import *

window = Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)


#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#Button
botton = Button(text="Click Me", command=button_clicked)
botton.pack()

# Entry
input = Entry(width=10)
input.pack()
print(input.get())


window.mainloop()
