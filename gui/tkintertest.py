import tkinter

name = None

def main():
     
    window = tkinter.Tk()

    greeting = tkinter.Label(text= "What is your first name?")
    greeting.pack()

    entry = tkinter.Entry()
    entry.pack()
    
    name = entry.get()
    print(name)

    def buttfunc():
        print(name + ", cool") 

    button = tkinter.Button(text = "Done", height = 2, width = 5, command=buttfunc)
    
    button.pack()

    
    window.mainloop()

if __name__ == "__main__":
    main()

#The window x and y are not on the same terms
#height is width times 2
# h = w x 2

# fg = text


