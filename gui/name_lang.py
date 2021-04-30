import tkinter

#possible lang
## hexidecimal
## arabic (dont know how i would get those characters)
## galactic alphabet ('')
## phone number keyboard
## nato phonetic alphabet (whiskey, tango, foxtrot)

def binary_trans(letter):
    letter = letter.lower()
    if letter == "a":
        letter = "01000001"
    elif letter == "b":
        letter = "01000010"
    elif letter == "c":
        letter = "01000011"
    elif letter == "d":
        letter = "01000100"
    elif letter == "e":
        letter = "01000101"
    elif letter == "f":
        letter = "01000110"
    elif letter == "g":
        letter = "01000111"
    elif letter == "h":
        letter = "01001000"
    elif letter == "i":
        letter = "01001001"
    elif letter == "j":
        letter = "01001010"
    elif letter == "k":
        letter = "01001011"
    elif letter == "l":
        letter = "01001100"
    elif letter == "m":
        letter = "01001101"
    elif letter == "n":
        letter = "01001110"
    elif letter == "o":
        letter = "01001111"
    elif letter == "p":
        letter = "01010000"
    elif letter == "q":
        letter = "01010001"
    elif letter == "r":
        letter = "01010010"
    elif letter == "s":
        letter = "01010011"
    elif letter == "t":
        letter = "01010100"
    elif letter == "u":
        letter = "01010101"
    elif letter == "v":
        letter = "01010110"
    elif letter == "w":
        letter = "01010111"
    elif letter == "x":
        letter = "01011000"
    elif letter == "y":
        letter = "01011001"
    elif letter == "z":
        letter = "01011010"
    return letter + " "


def pig_latin(name):
    print(name + ", cool") 
    piglatin = name[1:] + name[0] + "ay"
    return piglatin

def binary(name):
    print(name + ", cool") 
    new_binary = ""
    for let in name:
        new_binary += binary_trans(let)
    return new_binary
    #this will return a list, figure out how to make it string

def main():
    def do_pig_latin():
        name = entry.get()
        new = pig_latin(name)
        answer['text'] = new
        answer.pack()

    def do_binary():
        name = entry.get()
        new = binary(name)
        answer['text'] = new
        answer.pack()
        print(new)

    window = tkinter.Tk()

    title = tkinter.Label(text = "Name Translator")
    title.pack()
    greeting = tkinter.Label(text= "What is your first name?")
    greeting.pack()

    entry = tkinter.Entry()
    entry.pack()

    answer = tkinter.Label()
    answer.pack()
    
   

    pig_latin_button = tkinter.Button(text = "Pig Latin", height = 2, width = 5, command=do_pig_latin)
    pig_latin_button.pack()

    binary_button = tkinter.Button(text = "Binary", height = 2, width = 5, command=do_binary)
    binary_button.pack()
    
    window.mainloop()

if __name__ == "__main__":
    main()

#The window x and y are not on the same terms
#height is width times 2
# h = w x 2

# fg = text


