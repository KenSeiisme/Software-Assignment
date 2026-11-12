from tkinter import*
from tkinter import messagebox

class Recipe_Organizer_System:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        # Set the window size
        self.window.geometry("400x500")

        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        operation_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operations", menu=operation_menu)
        operation_menu.add_command(label="Exit", command=self.window.quit)

        # username and password
        self.users = {
        "user01": "Kiyo2026",
        "user02": "Mango123",
        "user03": "Rice888",
        "user04": "Soup000",
        "user05": "Noodle111",
        "user06": "Burger999",
        "user07": "Cookie321",
        "user08": "Peach321",
        "user09": "Tofu000",
        "user10": "Curry777",
    }
        self.window.title("Home")
        title = Label(self.window, text="Kiyo Recipe Organizer", font=("CourierNew", 20, "bold", "italic"))
        bR = Button(self.window, width=10, height=2, text="Register", command=self.register)
        bS = Button(self.window, width=10, height=2, text="Sign in", command=self.login)
        title.pack(pady=(45, 5))

        logo_image = PhotoImage(file = "Kiyo.png")
        canvas = Canvas(self.window)
        canvas.create_image(180, 140, anchor="center", image=logo_image)
        canvas.pack()
        bR.pack(pady=2)
        bS.pack(pady=10)

        self.window.mainloop()
    
    def register(self):
        # New page
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Registration Center")
        self.window.geometry("400x500")


        Label(self.window, text="Welcome!",font=("Times New Roman", 20, "bold", "italic")).pack(pady=20)
        Label(self.window, text="Username").pack()
        self.username_entry = Entry(self.window)
        self.username_entry.pack()

        Label(self.window, text="Password").pack()
        self.password_entry = Entry(self.window)
        self.password_entry.pack()

        # Frame to hold the confirm and back button
        self.register_frame = Frame(self.window)
        self.register_frame.pack()

        button_frame = Frame(self.register_frame)
        button_frame.pack(pady=10)
       
        Button(button_frame, text="Back", command=self.homePage).pack(side="left", padx=5, pady=(20, 0))
        Button(button_frame, text="Confirm", command=self.confirm_registration).pack(side="left", padx=5, pady=(20, 0))

    def login(self):
        # New page
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Login Center")
        self.window.geometry("400x500")


        Label(self.window, text="Welcome back!", font=("Times New Roman", 20, "bold", "italic")).pack(pady=10)
        Label(self.window, text="Username").pack()
        self.username_entry = Entry(self.window)
        self.username_entry.pack()

        Label(self.window, text="Password").pack()
        self.password_entry = Entry(self.window)
        self.password_entry.pack()
        

         # Frame to hold the confirm and back button
        self.login_frame = Frame(self.window)
        self.login_frame.pack()
        
        button_frame = Frame(self.login_frame)
        button_frame.pack(pady=10)
        
        Button(button_frame, text="Back", command=self.homePage).pack(side="left", padx=5, pady=(20, 0))
        Button(button_frame, text="Confirm", command=self.confirm_login).pack(side="left", padx=5, pady=(20, 0))

    # For click back to home page
    def homePage(self):
        
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.config(menu=Menu(self.window))

        self.window.title("Home")
        title = Label(self.window, text="Kiyo Recipe Organizer", font=("CourierNew", 20, "bold", "italic"))
        bR = Button(self.window, width=10, height=2, text="Register", command=self.register)
        bS = Button(self.window, width=10, height=2, text="Sign in", command=self.login)
        title.pack(pady=(45, 5))
                
        self.logo_image = PhotoImage(file = "Kiyo.png")
        canvas = Canvas(self.window)
        canvas.create_image(180, 140, anchor="center", image=self.logo_image)
        canvas.pack()
        bR.pack(pady=2)
        bS.pack(pady=10)

    ### Confirm by sign in
    def confirm_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login Successful", "Welcome, {}!".format(username))
            self.Recipe_Page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    ### Confirm by register
    def confirm_registration(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        symb = any(c in password for c in '!@#$%^&')

        # Password validation
        if len(password) <5:
            messagebox.showerror("Registration Failed", "Password must be at least 5 characters long.")
            return False
        elif symb == True:
            messagebox.showerror("Registration Failed", "Password can only contain letters and numbers.")
            return False
        elif username in self.users:
            messagebox.showerror("Registration Failed", "Username already exists.")
            return False
        else:
            self.users[username] = password
            messagebox.showinfo("Registration Successful", "Account created for {}!".format(username))
            self.homePage()

    def Recipe_Page(self):

        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Kiyo Recipe Organizer")
        Label(self.window, text="Kiyo Recipe", font=("Times New Roman", 20, "bold", "italic")).pack(pady=10)
        ### not complete yet
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)

        operation_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Operations", menu=operation_menu)
        operation_menu.add_command(label="Create Recipe", command=self.create_recipe)
        operation_menu.add_command(label="Edit Recipe", command=self.edit_recipe)
        operation_menu.add_command(label="Search Recipe", command=self.search_recipe)
        operation_menu.add_separator()
        operation_menu.add_command(label="Back to Home",  command=self.homePage)   
        operation_menu.add_command(label="Exit", command=self.window.destroy)
        
        # Create a frame to hold the widgets
        self.recipe_frame = Frame(self.window)
        self.recipe_frame.pack()
        self.label = Label(self.recipe_frame, text="Welcome to the 3A3D Recipe Organizer")
        self.label.pack()
        
        self.order_button = Button(self.recipe_frame, text="Create Recipe", command=self.create_recipe)
        self.order_button.pack()
        
        self.edit_button = Button(self.recipe_frame, text="Edit Recipe", command=self.edit_recipe)
        self.edit_button.pack()
        
        self.search_button = Button(self.recipe_frame, text="Search Recipe", command=self.search_recipe)
        self.search_button.pack()
        
        self.exit_button = Button(self.recipe_frame, text="Exit", command=self.window.quit)
        self.exit_button.pack()
        
        
         
          
Recipe_Organizer_System()