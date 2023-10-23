import random
import string
from tkinter import*
from tkinter.messagebox import*

root = Tk()
root.title("Random Password Generator")
root.geometry('800x800+50+50')
f = ("Arial", 30, "bold")

password = StringVar()

def pas():
    try:
        pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        password1 = ""
        pass_len = int(len_ent.get())
        if pass_len < 0:
            showerror("Issue", "Number shoulde be postive")
        else:
            for x in range (int(pass_len)):
                password1 = password1 + random.choice(pass1)
            password.set(password1)
    except Exception as e:
        showerror("Issue", "Do no enter alphabets, enter number only")
    

    

len_lab = Label(root, text="Enter the length of password", font=f)
len_lab.pack(pady=5)

len_ent = Entry(root, font=f)
len_ent.pack(pady=5)

get_btn = Button(root, text="Generate the password", font=f, command=pas)
get_btn.pack(pady=5)

pas2 = Label(root, text= "Password:", font=f)
pas2.pack(pady=5)

pas_lab = Label(root, textvariable=password, font=f)
pas_lab.pack(pady=5)

root.mainloop()

