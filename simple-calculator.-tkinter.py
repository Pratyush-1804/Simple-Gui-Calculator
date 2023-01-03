from tkinter import *

# Creating the window
window = Tk()

# title
window.title("A Simple Calculator")


# Creating Input field to put the values
e = Entry(width=40, borderwidth=5)
e.insert(0, " ")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Creating the function of the buttons
def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Creating the function to clear the screen
def clear_everything():
    e.delete(0, END)


# Creating the functionality for the button  +

def button_addition():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


# Subtraction
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

# Multiplication


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

# Division


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

# Creating the qual button functionality


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))

    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))

    elif math == "division":
        e.insert(0, f_num / int(second_number))


# Creating the button
button_1 = Button(text="1",
                  command=lambda: button_add(1), padx=40, pady=20)
button_2 = Button(text="2",
                  command=lambda: button_add(2), padx=40, pady=20)
button_3 = Button(text="3",
                  command=lambda: button_add(3), padx=40, pady=20)
button_4 = Button(text="4",
                  command=lambda: button_add(4), padx=40, pady=20)
button_5 = Button(text="5",
                  command=lambda: button_add(5), padx=40, pady=20)
button_6 = Button(text="6",
                  command=lambda: button_add(6), padx=40, pady=20)
button_7 = Button(text="7",
                  command=lambda: button_add(7), padx=40, pady=20)
button_8 = Button(text="8",
                  command=lambda: button_add(8), padx=40, pady=20)
button_9 = Button(text="9",
                  command=lambda: button_add(9), padx=40, pady=20)
button_0 = Button(text="0",
                  command=lambda: button_add(0), padx=40, pady=20)
button_sum = Button(text="+",
                    command=button_addition, padx=39, pady=20)
button_clear = Button(text="Clear",
                      command=clear_everything, padx=79, pady=20)
button_equal = Button(text="=",
                      command=button_equal, padx=91, pady=20)
button_subtraction = Button(text="-",
                            command=button_subtract, padx=40, pady=20)
button_multiplication = Button(text="*",
                               command=button_multiply, padx=40, pady=20)
button_division = Button(text="/",
                         command=button_divide, padx=40, pady=20)


# Putting the buttons in their place
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_sum.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=3)
button_clear.grid(row=4, column=1, columnspan=2)


button_subtraction.grid(row=6, column=0)
button_multiplication.grid(row=6, column=1)
button_division.grid(row=6, column=2)

# Looping the window
window.mainloop()
