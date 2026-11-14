from pathlib import Path
from tkinter import*
from tkinter import messagebox
from recipe import recipes
from tkinter import PhotoImage
from tkinter import Canvas, Scrollbar
    
class Recipe_Organizer_System:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        # Set the window size
        self.window.geometry("1200x744")

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
    
# For click back to home page
    def homePage(self):
        
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.config(menu=Menu(self.window))
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        operation_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operations", menu=operation_menu)
        operation_menu.add_command(label="Exit", command=self.window.quit)

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
    
    def register(self):
        # New page
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Registration Center")
        self.window.geometry("1200x744")


        Label(self.window, text="Welcome!",font=("Times New Roman", 20, "bold", "italic")).pack(pady=20)
        Label(self.window, text="Username").pack()
        self.username_entry = Entry(self.window)
        self.username_entry.pack()

        Label(self.window, text="Password").pack(pady=(20, 0))
        self.password_entry = Entry(self.window)
        self.password_entry.pack()
        Label(self.window, text="Password at least 5 characters", fg="grey", font=("Times New Roman", 8, "italic")).pack()

        # Frame to hold the confirm and back button
        self.register_frame = Frame(self.window)
        self.register_frame.pack()

        button_frame = Frame(self.register_frame)
        button_frame.pack(pady=10)
       
        Button(button_frame, text="Back", width=10, height=2, command=self.homePage).pack(side="left", padx=5, pady=(20, 0))
        Button(button_frame, text="Confirm", width=10, height=2, command=self.confirm_registration).pack(side="left", padx=5, pady=(20, 0))

    def login(self):
        # New page
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Login Center")
        self.window.geometry("1200x744")


        Label(self.window, text="Welcome back!", font=("Times New Roman", 20, "bold", "italic")).pack(pady=20)
        Label(self.window, text="Username").pack()
        self.username_entry = Entry(self.window)
        self.username_entry.pack()

        Label(self.window, text="Password").pack(pady=(20, 0))
        self.password_entry = Entry(self.window)
        self.password_entry.pack()

         # Frame to hold the confirm and back button
        self.login_frame = Frame(self.window)
        self.login_frame.pack()
        
        button_frame = Frame(self.login_frame)
        button_frame.pack(pady=10)
        
        Button(button_frame, text="Back", width=10, height=2, command=self.homePage).pack(side="left", padx=5, pady=(20, 0))
        Button(button_frame, text="Confirm", width=10, height=2, command=self.confirm_login).pack(side="left", padx=5, pady=(20, 0))

    def confirm_login(self):
        
        self.Recipe_Page()

    ##############################################################################################################################
    ##############################################################################################################################
    def Recipe_Page(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Kiyo Recipe Organizer")

        Label(self.window, text="Kiyo Recipe", font=("Times New Roman", 50, "bold", "italic")).pack(pady=10)

        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        operation_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operations", menu=operation_menu)
        operation_menu.add_command(label="Log out", command=self.homePage)
        operation_menu.add_command(label="Create Recipe", command=self.create_recipe)
        operation_menu.add_command(label="Edit Recipe", command=self.edit_recipe)
        operation_menu.add_command(label="Search Recipe", command=self.search_recipe)

        Label(self.window, text="Let's Taste!", font=("Times New Roman", 25, "bold"), fg="blue").pack(pady=10)
        # Create a canvas and scrollbar for scrolling through recipe cards
        canvas = Canvas(self.window)
        vbar = Scrollbar(self.window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vbar.set)

        vbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Create a frame to hold the recipe cards
        card_frame = Frame(canvas)
        canvas_window = canvas.create_window((0, 0), window=card_frame, anchor="nw")

        canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width))

        card_frame.columnconfigure(0, weight=1)

        card_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        self.window.bind_all(
            "<MouseWheel>",
            lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        )
        self.project_folder = Path(__file__).resolve().parent
        self.card_frame = card_frame
        self.display_Recipes(recipes)

    # IMPORTANT loop to search and display
    def display_Recipes(self, recipe_list):
        self.recipe_images = []

        for i, recipe in enumerate(recipe_list):
            row, col = divmod(i, 3)

            card = Frame(self.card_frame)
            card.grid(row=row, column=col + 1, padx=10, pady=10)

            image_path = self.project_folder / recipe["image"]
            photo = PhotoImage(file=str(image_path))
            self.recipe_images.append(photo)

            Button(
                card,
                image=photo,
                text=recipe["name"],
                font=("Arial", 15, "bold"),
                compound="top",
                command=lambda r=recipe: self.show_details(r)
            ).pack()

    def show_details(self, recipe):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title(recipe["name"])
        Button(self.window, text="Back", width=10, height=2, command=self.Recipe_Page).pack(anchor="nw", padx=10, pady=10)

        # Scroll(frame1)
        canvas = Canvas(self.window)
        vbar = Scrollbar(self.window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vbar.set)

        vbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Create a frame to hold the recipe details
        self.page_frame = Frame(canvas)
        canvas_window = canvas.create_window((0, 0), window=self.page_frame, anchor="nw")

        canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width))

        self.page_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.bind_all(
            "<MouseWheel>",
            lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        )

        ### frame2
        self.Title_frame = Frame(self.page_frame)
        self.Title_frame.pack()
        title_frame = Frame(self.Title_frame)
        title_frame.pack()

        Label(title_frame, text=recipe['name'], font=("Times New Roman", 35, "bold", "italic")).pack(pady=15)
        # photo
        self.project_folder = Path(__file__).resolve().parent
        image_path = self.project_folder / recipe["image"]
        self.photo = PhotoImage(file=str(image_path))
        Label(title_frame, image=self.photo).pack(pady=5)
        Label(title_frame, text='Category: ' + recipe['category'], fg="purple", font=("Times New Roman", 13, "italic")).pack(pady=10)

        # frame3
        self.details_frame = Frame(self.page_frame)
        self.details_frame.pack()
        ing_frame = Frame(self.details_frame)
        ing_frame.pack(anchor="w", pady=20)
        #show ingredients
        Label(ing_frame, text="Ingredients:", font=("CourierNew", 20, "bold", "italic")).pack(anchor="w")
        Button(self.details_frame, text="Customize", bg="yellow", font=("Arial", 10, "bold"), width=10, height=2, command=lambda: self.customize(recipe)).pack(anchor="center")

        for item in recipe["ingredients"]:
            ingredient_text = (
            f'{item["name"]} ：'
            f'{item["amount"] if item["amount"] is not None else ""} '
            f'{item["unit"]}'
        )
            Label(ing_frame, text=ingredient_text, font=("Arial", 13)).pack(side="top", anchor="w", pady=2)

        ins_frame = Frame(self.details_frame)
        ins_frame.pack(pady=25)
        #show instructions
        Label(ins_frame, text="Instructions:", font=("CourierNew", 20, "bold", "italic")).pack()
        # for loop
        for i, step in enumerate(recipe["steps"], start=1):
            Label(ins_frame, text=f"{i}. {step}", wraplength=3000, font=("Arial", 13)).pack(anchor="w", pady=5)

    def customize(self, recipe):
        c_window = Toplevel()
        c_window.title("Customize Recipe")
        c_window.geometry("500x500")
        c_window.config(menu=Menu(c_window))   

        Label(c_window, text=f"Customize: {recipe['name']}",
            font=("Times New Roman", 16, "bold")).pack(pady=10)

        for item in recipe["ingredients"]:
            row = Frame(c_window); row.pack(fill="x", padx=10, pady=2)
            Label(row, text=item["name"], width=20, anchor="w").pack(side="left")
            Label(row, text=f"({item['unit']})", width=20, anchor="w").pack(side="left")
            var = DoubleVar(value=item.get("amount") or 1)
            Spinbox(row, from_=0, to=100, increment=0.1,
                    textvariable=var, width=8).pack(side="left")

        Button(c_window, text="Save to My Recipes", font=("Arial", 10, "bold"), width=15, height=5, command=lambda: self.save_customized_recipe(recipe)).pack(anchor="center", pady=10)
        


    def search_recipe(self):
            # Create a new window for recipe searching
            search_window = Toplevel()
            search_window.title("Search Recipe")
        
            # Create a label and entry field for recipe name
            Label(search_window, text="Recipe Name:").grid(row=0, column=0)
            self.search_recipe_name_entry = Entry(search_window)
            self.search_recipe_name_entry.grid(row=0, column=1)
        
            # Create a button to search for the recipe
            search_button = Button(search_window, text="Search",width=10, height=2, command=self.perform_search)
            search_button.grid(row=1, columnspan=2)

    def create_recipe(self):
            for widget in self.window.winfo_children():
                widget.destroy()
            # Create a new window for recipe creation
            self.window.title("Create Recipe")
        
            # Create labels and entry fields for recipe details
            Label(self.window, text="Recipe Name:").grid(row=1, column=0)
            self.recipe_name_entry = Text(self.window, width=100, height=1)
            self.recipe_name_entry.grid(row=1, column=1, pady=5)
        
            Label(self.window, text="Ingredients:").grid(row=2, column=0)
            self.ingredients_entry = Text(self.window, width=100, height=8)
            self.ingredients_entry.grid(row=2, column=1, pady=5)
        
            Label(self.window, text="Instructions:").grid(row=3, column=0)
            self.instructions_entry = Text(self.window, width=100, height=8)
            self.instructions_entry.grid(row=3, column=1, pady=5)
        
            # Create a frame to hold the save button
            self.save_frame = Frame(self.window)
            self.save_frame.grid(row=4, column=1, pady=10)
            
            button_frame = Frame(self.save_frame)
            button_frame.pack()
        
            back_button = Button(button_frame, text="Back", width=10, height=2, command=self.Recipe_Page)
            back_button.pack(side="left", padx=5)
            save_button = Button(button_frame, text="Save Recipe", width=10, height=2, command=self.save_recipe)
            save_button.pack(side="left", padx=5)

    def save_recipe(self):
            # Get the recipe details from the entry fields
            recipe_name = self.recipe_name_entry.get()
            ingredients = self.ingredients_entry.get()
            instructions = self.instructions_entry.get()
        
            # Here you can add code to save the recipe details to a file or database
            print(f"Recipe Name: {recipe_name}")
            print(f"Ingredients: {ingredients}")
            print(f"Instructions: {instructions}")
        
    def edit_recipe(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        # Create a new window for recipe editing
        self.window.title("Edit Recipe")

        Label(self.window, text="Recipe Name:").grid(row=1, column=0)
        self.recipe_name_entry = Text(self.window, width=100, height=1)
        self.recipe_name_entry.grid(row=1, column=1, pady=5)
            
        Label(self.window, text="Ingredients:").grid(row=2, column=0)
        self.ingredients_entry = Text(self.window, width=100, height=8)
        self.ingredients_entry.grid(row=2, column=1, pady=5)
            
        Label(self.window, text="Instructions:").grid(row=3, column=0)
        self.instructions_entry = Text(self.window, width=100, height=8)
        self.instructions_entry.grid(row=3, column=1, pady=5)
            
        # Create a frame to hold the save button
        self.edit_frame = Frame(self.window)
        self.edit_frame.grid(row=4, column=1, pady=10)
                
        button_frame = Frame(self.edit_frame)
        button_frame.pack(pady=10)
            
        back_button = Button(button_frame, text="Back", width=10, height=2, command=self.Recipe_Page)
        back_button.pack(side="left", padx=5)
        save_button = Button(button_frame, text="Save Changes", width=10, height=2, command=self.save_edited_recipe)
        save_button.pack(side="left", padx=5)   
          

    def save_edited_recipe(self):
            # Get the edited recipe details from the entry fields
            recipe_name = self.recipe_name_entry.get()
            ingredients = self.ingredients_entry.get()
            instructions = self.instructions_entry.get()
        
            # Here you can add code to save the edited recipe details to a file or database
            print(f"Edited Recipe Name: {recipe_name}")
            print(f"Edited Ingredients: {ingredients}")
            print(f"Edited Instructions: {instructions}")   

    def save_customized_recipe(self, recipe):
        # Here you can add code to save the customized recipe to a file or database
        messagebox.showinfo("Save Recipe", f"Customized recipe '{recipe['name']}' saved to My Recipes!")

    


Recipe_Organizer_System()