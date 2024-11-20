from tkinter import *
from PIL import ImageTk,Image
import customtkinter
from customtkinter import CTkFrame
import tkinter as tk
from tkinter import messagebox

# Simulated database
user_db = {}

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        # Welcome frame database
        self.data = []

        # Create frames
        self.image_frame = CTkFrame(self.root,border_color='black', fg_color='black', bg_color='black', border_width=2,corner_radius=20, width=850, height=450)
        self.login_frame = CTkFrame(self.root,border_color='black',fg_color='#f0f0f0',bg_color='black',border_width=2,corner_radius=20,width=450,height=450)
        self.signup_frame = CTkFrame(self.root,border_color='black',fg_color='#f0f0f0',bg_color='black',border_width=2,corner_radius=20,width=450,height=450)
        self.welcome_frame = CTkFrame(self.root, width=850, height=450,fg_color='black')
        # Create widgets for the login frame
        self.create_login_widgets()

        # Create widgets for the signup frame
        self.create_signup_widgets()

        # Create widgets for the welcome frame
        self.create_welcome_widgets()



        self.create_image_widgets()

        # Show the login frame by default
        self.login_frame.place(x=399.9, y=0)

        self.image_frame.place(x=0,y=0)


    def create_login_widgets(self):

        #Resize show and hide password icon
        self.show = Image.open('show.png')
        self.resize_image = self.show.resize((20, 20))
        self.show_image = ImageTk.PhotoImage(self.resize_image)

        self.hidepass = Image.open('hide.png')
        self.resize_image = self.hidepass.resize((20, 20))
        self.hide_image = ImageTk.PhotoImage(self.resize_image)

        label_username = Label(self.login_frame, text="Log in",font=('calibre', 20, 'normal', 'bold'))
        label_username.place(x=180,y=50)

        # Log in Username
        label_username = Label(self.login_frame, text="Username:")
        label_username.place(x=100, y=110)

        self.entry_username = customtkinter.CTkEntry(self.login_frame,border_color="black",border_width=0,corner_radius=5,fg_color='white',width=250,height=30,text_color='black',placeholder_text="Enter Username")
        self.entry_username.place(x=100,y=130)

        # Log in Password
        label_password = Label(self.login_frame, text="Password:")
        label_password.place(x=100,y=180)

        self.entry_password = customtkinter.CTkEntry(self.login_frame, show='*',border_color="black",border_width=0,corner_radius=5,fg_color='white',width=250,height=30,text_color='black',placeholder_text="Enter Password")
        self.entry_password.place(x=100,y=200)

        # Show and hide button
        self.show_button = Button(self.login_frame, image=self.show_image,text="", background="white",command=self.show_password,border=0,cursor="hand2")
        self.show_button.image = self.show_image
        self.show_button.place(x=320, y=204)

        # Log in button
        button_login = customtkinter.CTkButton(self.login_frame, text="Login",border_width=0,border_spacing=10,corner_radius=50,width=250,height=30, command=self.login)
        button_login.place(x=100,y=260)

        # Sign up link button
        button_signup = tk.Button(self.login_frame, text="Go to Signup", command=self.show_signup_frame,border=0,fg='blue',cursor="hand2")
        button_signup.place(x=190,y=320)

    def create_image_widgets(self):

        self.background = Image.open("download.jpg")
        self.Pic = ImageTk.PhotoImage(self.background)

        background_image = Label(self.image_frame, image=self.Pic,width=395,border=0,)
        background_image.place(x=0,y=0)

        background_image = Label(self.image_frame, image=self.Pic, width=445,border=0)
        background_image.place(x=399.9, y=0)

        label = Label(self.image_frame, text="Welcome Back!", font=('calibre', 25, 'normal', 'bold'), bg="black",border=0,
                      fg='white')
        label.place(x=100, y=200)

        label = Label(self.image_frame, text="Hi,\nWelcome!", font=('calibre', 25, 'normal', 'bold'), bg="black",border=0,
                      fg='white')
        label.place(x=550, y=170)
    def create_signup_widgets(self):

        # Resize show and hide icon
        show = Image.open('show.png')
        self.resize_image = show.resize((20, 20))
        self.show_image = ImageTk.PhotoImage(self.resize_image)

        hidepass = Image.open('hide.png')
        self.resize_image = hidepass.resize((20, 20))
        self.hide_image = ImageTk.PhotoImage(self.resize_image)

        label_username = Label(self.signup_frame, text="Sign up",font=('calibre', 20, 'normal', 'bold'))
        label_username.place(x=180,y=50)

        # sign up Username
        label_username = Label(self.signup_frame, text="Username:")
        label_username.place(x=100, y=110)

        self.entry_signup_username = customtkinter.CTkEntry(self.signup_frame,border_color="black",border_width=0,corner_radius=5,fg_color='white',width=250,height=30,text_color='black',placeholder_text="Enter Username")
        self.entry_signup_username.place(x=100,y=130)

        # Sign up Password
        label_password = Label(self.signup_frame, text="Password:")
        label_password.place(x=100,y=180)

        self.entry_signup_password = customtkinter.CTkEntry(self.signup_frame, show='*',border_color="black",border_width=0,corner_radius=5,fg_color='white',width=250,height=30,text_color='black',placeholder_text="Enter Password")
        self.entry_signup_password.place(x=100,y=200)

        # Show and hide button
        self.show_button = tk.Button(self.signup_frame,image=self.show_image,text="show", background="white",command=self.show_password,border=0)
        self.show_button.image = self.show_image
        self.show_button.place(x=300, y=204)

        # Sign up Button
        button_signup = customtkinter.CTkButton(self.signup_frame, text="Sign up", command=self.signup,border_width=0,border_spacing=10,corner_radius=50,width=250,height=30)
        button_signup.place(x=100,y=260)

        # Log in link Button
        button_login = tk.Button(self.signup_frame, text="Go to Log in", command=self.show_login_frame,border=0,fg='blue',cursor="hand2")
        button_login.place(x=190,y=320)

    def create_welcome_widgets(self):

        self.frame = CTkFrame(self.welcome_frame, fg_color='#f0f0f0', border_width=2, corner_radius=20, width=400, height=400)
        self.frame.place(x=260, y=20)

        self.entry = customtkinter.CTkEntry(self.welcome_frame, border_color="black", border_width=0, corner_radius=5,
                                            fg_color='white', width=250, height=30, text_color='black',bg_color='#f0f0f0',
                                            placeholder_text="Enter Item")
        self.entry.place(x=330, y=50)

        self.add_button = customtkinter.CTkButton(self.welcome_frame, text="Add", command=self.add, border_width=0,
                                                  border_spacing=0, corner_radius=50, width=5, border_color="white",bg_color='#E8E8E8' )
        self.add_button.place(x=355, y=100)

        self.update_button = customtkinter.CTkButton(self.welcome_frame, text="Update", command=self.update, border_width=0,
                                                     border_spacing=0, corner_radius=50, width=5,bg_color='#E8E8E8')
        self.update_button.place(x=415, y=100)

        self.delete_button = customtkinter.CTkButton(self.welcome_frame, text="Delete", command=self.delete, border_width=0,
                                                     border_spacing=0, corner_radius=50, width=5,bg_color='#E8E8E8')
        self.delete_button.place(x=490, y=100)

        self.listbox = tk.Listbox(self.welcome_frame, width=40, height=15)
        self.listbox.place(x=330, y=140)

    def signup(self):
        username = self.entry_signup_username.get()
        password = self.entry_signup_password.get()

        if username in user_db:
            messagebox.showerror("Error", "User already exists!")
        elif username == "" or password == "":
            messagebox.showerror("Error", "Please fill in all fields!")
        else:
            user_db[username] = password
            messagebox.showinfo("Success", "User created successfully!")
            self.entry_signup_username.delete(0, tk.END)
            self.entry_signup_password.delete(0, tk.END)
            self.signup_frame.place_forget()
            self.login_frame.place(x=399.9, y=0)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in user_db and user_db[username] == password:
            messagebox.showinfo("Success", "Login successful!")
            self.entry_username.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.login_frame.place_forget()
            self.welcome_frame.place(x=0, y=0)
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def show_signup_frame(self):
        self.login_frame.place_forget()
        self.signup_frame.place(x=0, y=0)

    def show_login_frame(self):
        self.signup_frame.place_forget()
        self.login_frame.place(x=399.9, y=0)

    def show_password(self):
        if self.entry_password.cget('show') == "*":
            self.entry_password.configure(show="")
            self.show_button.configure(image=self.hide_image)
        else:
            self.show_button.configure(image=self.show_image)
            self.entry_password.configure(show="*")

    def add(self):
        item = self.entry.get()
        if item:
            self.data.append(item)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an item.")

    def update(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            new_value = self.entry.get()
            if new_value:
                self.data[selected_index[0]] = new_value
                self.update_listbox()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a new value.")
        else:
            messagebox.showwarning("Warning", "Please select an item to edit.")

    def delete(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            del self.data[selected_index[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select an item to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.data:
            self.listbox.insert(tk.END, item)

# Create main window
root = tk.Tk()
app = App(root)
root.geometry("850x450")

# Run the application
root.mainloop()