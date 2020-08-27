import tkinter as tk
from tkinter import font as tkFont
import random
from tkinter import ttk


LARGEFONT = ("Arial", 20, "bold")

# characters that can be used to produce a strong password
# some characters such as "I" and "0" are avoided because of the possibility for confusion
possible_characters = "!#$%&'()*+,-./23456789:;<=>?@ABCDEFGHJKLMNOPRSTUVWXYZ[\]^_abcdefghijkmnopqrstuvwxyz{|}~"
list_char = []
for each_char in possible_characters:
    list_char.append(each_char)

# boiler-plate code for tkinter multiple frame window from https://www.geeksforgeeks.org/
class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}
        # iterating through  tuple consisting
        # of the different page layouts
        for F in (HomePage, RandomPage, CustomPage):
            frame = F(container, self)
            # set frame color
            frame.configure(bg = '#89cff0')
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



# Home Page frame
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, bg= '#89cff0', text="Welcome to PasswordGenerator!", font=("Arial",18, "bold")).place(x=300, y = 10)
        label2 = tk.Label(self, bg= '#89cff0',  text="Please select an option below...", font=("Arial",12, "italic")).place(x=370, y = 40)

        # button to lead to random password generator
        button1 = tk.Button(self, text="GENERATE RANDOM PASSSWORD", height = 3, width = 40,
                             command=lambda: controller.show_frame(RandomPage))
        button_font = tkFont.Font(family='Arial', size=14, weight='bold')
        button1['font'] =button_font
        button1.place(x=285, y=85)

        # button to lead to custom password generator
        button2 = tk.Button(self, text="GENERATE CUSTOMIZED PASSSWORD", height = 3, width = 40,
                             command=lambda: controller.show_frame(CustomPage))
        button2['font'] = button_font
        button2.place(x=285, y=150)



# Random Password Generator frame
class RandomPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, bg= '#89cff0',text="Random Password", font=LARGEFONT).place(x = 350, y = 10)

        # allows user to return back to home page
        button1 = tk.Button(self, text="Return to Home page",
                             command=lambda: controller.show_frame(HomePage)).place(x = 10, y = 210)


        # asks user for length of password
        label3 = tk.Label(self, text="Enter Length of Password:", font=("arial", 12, "bold")).place(x = 340, y = 70)
        length_of_password = tk.IntVar()
        entry = tk.Entry(self, textvariable=length_of_password, width=4).place(x = 500, y = 67)

        def action(length_of_password):
            password = ""
            if (length_of_password > 64):
                text = "INVALID ENTRY: Maximum allowed character length is 64. Please try again"
                generated_password["text"] = text
                generated_password.place(x= 225, y=100)
            else:
                for character in range(length_of_password):
                    password += random.choice(list_char)
                generated_password["text"] = password
                generated_password.pack(pady=100)

        # once clicked, the random password accounts for length parameter and generates a password
        generate_button = tk.Button(self, text="Generate Password", width=30,
                                  command=lambda: action(length_of_password.get())).place(x = 310, y = 150)
        generated_password = ttk.Label(self)
        generated_password.grid(row=5, column=2, padx=1, pady=10)



# Customized Password Generator frame
class CustomPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        special_characters = "!#$%&'()*+,-./23456789:;<=>[\]^"
        list_special_characters = []
        for each_char in special_characters:
            list_special_characters.append(each_char)
        label = tk.Label(self,bg= '#89cff0', text="Customized Password", font=LARGEFONT).place(x = 350, y = 10)

        # allows user to return to home page
        button2 = ttk.Button(self, text="Return to Home page",
                             command=lambda: controller.show_frame(HomePage)).place(x = 10, y = 210)


        label3 = tk.Label(self,bg= '#89cff0', text="Enter below 3 potential words you would like featured in your password.",
                           font=("arial", 12, "italic")).place(x = 275, y = 50)

        def produce_password(word1, word2, word3):
            list_words = []
            list_words.append(word1)
            list_words.append(word2)
            list_words.append(word3)
            approval1 = True
            approval2 = True

            # handles exceptions with user entry
            for each in list_words:
                if not each.isalpha():
                    approval1 = False
                if len(each) > 16:
                    approval2 = False

            # if all three blanks are NOT filled
            if "" in list_words:
                message["text"] = "INVALID ENTRY: MUST provide 3 words"
                message.place(x=342, y = 80)

            # if numbers and symbols included in words entered
            elif not approval1:
                message["text"] = "INVALID ENTRY: Words MUST NOT include numbers or symbols"
                message.place(x=260, y = 80)

            # if any entry exceeds 16 characters
            elif not approval2:
                message["text"] = "INVALID ENTRY: Word entries MUST NOT exceed 16 characters"
                message.place(x = 265, y = 80)

            # if valid entry of words
            else:
                final_password = random.sample(list_words,2)
                password = ""
                for i in range(4):
                    final_password.append(random.choice(list_special_characters))
                shuffled = random.shuffle(final_password)
                for word in final_password:
                    password+= word
                message["text"] = password
                message.pack(pady=80)

        # first word entry
        word1 = tk.StringVar()
        word1_label = ttk.Label(self, text="WORD 1:").place(x =350, y = 112)
        entry1 = ttk.Entry(self, textvariable=word1, width=15).place(x =425, y = 110)

        # second word entry
        word2 = tk.StringVar()
        word2_label = ttk.Label(self, text="WORD 2:").place(x =350, y = 138)
        entry2 = ttk.Entry(self, textvariable=word2, width=15).place(x =425, y = 135)

        # third word entry
        word3 = tk.StringVar()
        word3_label = ttk.Label(self, text="WORD 3:").place(x =350, y = 162)
        entry3 = ttk.Entry(self, textvariable=word3, width=15).place(x =425, y = 160)

        # once clicked, personalized password in generated
        generate_button = tk.Button(self, text="Generate Password",
                                    width=30, command=lambda: produce_password(word1.get(),
                                                                               word2.get(), word3.get())).place(x = 330, y = 200)

        message = ttk.Label(self)



# Driver Code
app = tkinterApp()
app.title("Password Generator")
app.minsize(width=900, height=250)
app.maxsize(width=900, height=250)
app.mainloop()
