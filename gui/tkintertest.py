import tkinter


def buttfunc(name):
    print(name + ", cool") 
    return name + ", cool"

def main():
    def do_buttfunc():
        name = entry.get()
        new = buttfunc(name)
        answer['text'] = new
        answer.pack()

    window = tkinter.Tk()

    greeting = tkinter.Label(text= "What is your first name?")
    greeting.pack()

    entry = tkinter.Entry()
    entry.pack()

    answer = tkinter.Label()
    answer.pack()
    
   

    

    button = tkinter.Button(text = "Done", height = 2, width = 5, command=do_buttfunc)
    
    button.pack()

    
    window.mainloop()

if __name__ == "__main__":
    main()

#The window x and y are not on the same terms
#height is width times 2
# h = w x 2

# fg = text


