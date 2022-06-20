from tkinter import *

class Sign_Up_Form():
    def __init__(self, window):
        self.window = window
        window.title("Login")
        window.configure(bg='#040229')
        window.resizable(FALSE,FALSE)
        
        Elist = []
        Plist = []

              
        self.label1 = Label(text='Log in', bg='#040229', fg="#72f542")
        self.label1.config(font=("Amiri", 20))
        self.label1.place(x=162,y=40)


        
        self.label2 = Label(text='E-mail    ', bg='#040229', fg="#ffffff")
        self.label2.config(font=("Amiri", 10))
        self.label2.place(x=50,y=130)


        self.label3 = Label(text='Password ', bg='#040229', fg="#ffffff")
        self.label3.config(font=("Amiri", 10))
        self.label3.place(x=50,y=180)

      
        self.text1 = Entry()
        self.text1.place(x=140,y=133)
        
        self.text2 = Entry()
        self.text2.place(x=140, y=180)
        

        self.button_forget = Button(text='forget password ?', bg='#040229', fg='white',activebackground='#040229',activeforeground='green', font="timesnewroman 7 bold")
        self.button_forget.place(x=180, y=205)
        

        self.quit_button = Button(text='X', bg='#040229',fg='red',command=self.window_quit,activebackground='red')
        self.quit_button.config(font=("Amiri", 15))
        self.quit_button.place(x=365,y=5)
                              


        self.login_button = Button(text='Log in',command=self.print_email, bg='#b32400', fg='black', height=1, width=25,activebackground='#801a00', activeforeground='green')
                        
        self.login_button.config(font=("Amiri", 10))
        self.login_button.place(x=90,y=244)
        
    def print_email(self):
        print('You have clicked the log in button')
    def window_quit(self):
        root.destroy()
        

root = Tk()
my_gui = Sign_Up_Form(root)
root.geometry('400x400+300+150')
root.mainloop()
