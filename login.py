from customtkinter import*
from PIL import Image   #this image class will help in importing image in our code
from customtkinter import CTkImage
from tkinter import messagebox

def login():
    if usernameEntry.get()=="" or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='dharshan' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems

    else:
        messagebox.showerror('Error','wrong credentials')



root=CTk()    #creating object to CTK class
root.geometry('930x478')    #width and height of window
root.resizable(0,0)   #to fix the window size
root.title('login page')
image=CTkImage(Image.open('cover.jpg'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employee Management System',bg_color='#EFEFEF',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headinglabel.place(x=150,y=100)

usernameEntry=CTkEntry(root,placeholder_text='Entry Your Username',width=180)
usernameEntry.place(x=180,y=150)

passwordEntry=CTkEntry(root,placeholder_text='Entry Your Password',width=180,show='*')
passwordEntry.place(x=180,y=200)

loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=200,y=250)
root.mainloop()        #to see the window on screen