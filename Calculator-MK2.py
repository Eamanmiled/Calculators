import tkinter


def button_click(value):
    entry_display.insert(tkinter.END, value)


def clear_display():
    entry_display.delete(0, tkinter.END)


root = tkinter.Tk()
root.title("Basic 2 number Calculator")
entry_display = tkinter.Entry(root, width=16, font=('Arial', 24), borderwidth=2,)
entry_display.grid(row=0, column=0, columnspan=4)
tkinter.Button(root, text="1", height=5, width=10, command=lambda: button_click("1")).grid(row=1, column=0, columnspan=1)
tkinter.Button(root, text="2", height=5, width=10, command=lambda: button_click("2")).grid(row=1, column=1, columnspan=1)
tkinter.Button(root, text="3", height=5, width=10, command=lambda: button_click("3")).grid(row=1, column=2, columnspan=1)
tkinter.Button(root, text="4", height=5, width=10, command=lambda: button_click("4")).grid(row=2, column=0, columnspan=1)
tkinter.Button(root, text="5", height=5, width=10, command=lambda: button_click("5")).grid(row=2, column=1, columnspan=1)
tkinter.Button(root, text="6", height=5, width=10, command=lambda: button_click("6")).grid(row=2, column=2, columnspan=1)
tkinter.Button(root, text="7", height=5, width=10, command=lambda: button_click("7")).grid(row=3, column=0, columnspan=1)
tkinter.Button(root, text="8", height=5, width=10, command=lambda: button_click("8")).grid(row=3, column=1, columnspan=1)
tkinter.Button(root, text="9", height=5, width=10, command=lambda: button_click("9")).grid(row=3, column=2, columnspan=1)
tkinter.Button(root, text="0", height=5, width=10, command=lambda: button_click("0")).grid(row=4, column=1, columnspan=1)
tkinter.Button(root, text="calc", height=5, width=10).grid(row=4, column=2, columnspan=1)
tkinter.Button(root, text="clear", height=5, width=10, command=clear_display).grid(row=4, column=0, columnspan=1)
tkinter.Button(root, text="+", height=5, width=10, command=lambda: button_click("+")).grid(row=1, column=3, columnspan=1)
tkinter.Button(root, text="-", height=5, width=10, command=lambda: button_click("-")).grid(row=2, column=3, columnspan=1)
tkinter.Button(root, text="÷", height=5, width=10, command=lambda: button_click("÷")).grid(row=3, column=3, columnspan=1)

root.mainloop()