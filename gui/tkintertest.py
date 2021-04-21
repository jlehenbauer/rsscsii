import tkinter

def main():

    window = tkinter.Tk()
    greeting = tkinter.Label(text= "Hello, World!")
    greeting.pack()
    button = tkinter.Button(text = "Click Me!", height = 5, width = 5, bg = "red", fg = "yellow")
    button.pack()
    window.mainloop()
if __name__ == "__main__":
    main()