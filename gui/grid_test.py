import tkinter



def main():
    window = tkinter.Tk()

    title = tkinter.Label(text = "Pick a color:")
    
    
    for i in range(3):
        for j in range(2):
            frame = tkinter.Frame(master=window, relief=tkinter.RAISED, borderwidth=3)
            frame.grid(row=i, column=j)
            label = tkinter.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack()
            
    title.pack()
    window.mainloop()
if __name__ == "__main__":
    main()