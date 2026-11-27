import time
from pathlib import Path
from tkinter import *
from tkinter import Canvas, PhotoImage, Scrollbar, filedialog, messagebox, ttk

from recipe import recipes

BG_COLOR = "#fef2d8"
FG_COLOR = "#2e3444"
BTN_COLOR = "#de774c"


class Recipe_Organizer_System:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        # Set the window size
        self.window.geometry("1500x844")
        self.window.config(bg=BG_COLOR)

        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        operation_menu = Menu(
            menubar,
            tearoff=0,
            bg=BG_COLOR,
            fg=FG_COLOR,
            bd=0,
            activebackground=BTN_COLOR,
            activeforeground=FG_COLOR,
        )
        menubar.add_cascade(
            label="Operations",
            menu=operation_menu,
        )
        operation_menu.add_command(label="Exit", command=self.window.quit)

        ### Load user data from a file
        self.USER_FILE = Path(__file__).resolve().parent / "user.txt"
        self.users = self.load_users()
        self.current_user = None

        ### Load custom recipes from a file
        self.MY_RECIPE_FILE = Path(__file__).resolve().parent / "my_recipe.txt"
        self.my_recipes = self.load_my_recipes()

        self.recipe_photo_images = []

        self.window.title("Home")
        title = Label(
            self.window,
            text="Kiyo Recipe Organizer",
            font=("CourierNew", 25, "bold", "italic"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        )
        bR = Button(
            self.window,
            width=10,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            text="Register",
            font=("Arial", 10, "bold"),
            command=self.register,
        )
        bS = Button(
            self.window,
            width=10,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            text="Sign in",
            font=("Arial", 10, "bold"),
            command=self.login,
        )
        title.pack(pady=(100, 20))

        self.logo_image = PhotoImage(file=r"assets\Kiyo.png")
        canvas = Canvas(self.window, bg=BG_COLOR, highlightthickness=0)
        canvas.create_image(180, 140, anchor="center", image=self.logo_image)
        canvas.pack()
        bR.pack(pady=2)
        bS.pack(pady=10)

        self.window.mainloop()

    # For click back to home page
    def homePage(self):

        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Home")
        title = Label(
            self.window,
            text="Kiyo Recipe Organizer",
            font=("CourierNew", 25, "bold", "italic"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        )
        bR = Button(
            self.window,
            width=10,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            text="Register",
            font=("Arial", 10, "bold"),
            command=self.register,
        )
        bS = Button(
            self.window,
            width=10,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            text="Sign in",
            font=("Arial", 10, "bold"),
            command=self.login,
        )
        title.pack(pady=(100, 20))

        canvas = Canvas(self.window, bg=BG_COLOR, highlightthickness=0)
        canvas.create_image(180, 140, anchor="center", image=self.logo_image)
        canvas.pack()
        bR.pack(pady=2)
        bS.pack(pady=10)

    ### Save user data to a file
    def save_users(self, users):
        lines = [f"{username}:{password}" for username, password in users.items()]
        ### Save the user data to the file with UTF-8 encoding
        self.USER_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    ### Load user data from a file
    def load_users(self):
        users = {}
        if self.USER_FILE.exists():
            lines = self.USER_FILE.read_text(encoding="utf-8").splitlines()
            for line in lines:
                ### Split the line into username and password
                username, password = line.split(":", 1)
                users[username] = password
        return users

    ### Confirm by register
    def confirm_registration(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Password validation
        if len(username) == 0:
            messagebox.showerror("Registration Failed", "Username cannot be empty.")
            return False
        ### To avoid file corruption that may contain (:)
        elif not username.isalnum():
            messagebox.showerror(
                "Registration Failed", "Username can only contain letters and numbers."
            )
            return False
        elif len(password) < 5:
            messagebox.showerror(
                "Registration Failed", "Password must be at least 5 characters long."
            )
            return False
        ### Check if the password contain only letters and numbers
        elif not password.isalnum():
            messagebox.showerror(
                "Registration Failed", "Password can only contain letters and numbers."
            )
            return False
        elif username in self.users:
            messagebox.showerror("Registration Failed", "Username already exists.")
            return False
        else:
            self.users[username] = password
            ### Save the updated user data to the file
            self.save_users(self.users)
            messagebox.showinfo(
                "Registration Successful", "Account created for {}!".format(username)
            )
            self.homePage()

    def register(self):
        # New page
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Registration Center")
        self.window.geometry("1500x844")

        Label(
            self.window,
            text="Welcome!",
            font=("Times New Roman", 60, "bold", "italic"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack(pady=(80, 50))
        Label(self.window, text="Username", font=20, bg=BG_COLOR, fg=FG_COLOR).pack()
        self.username_entry = Entry(self.window, font=20)
        self.username_entry.pack()

        Label(self.window, text="Password", font=20, bg=BG_COLOR, fg=FG_COLOR).pack(
            pady=(20, 0)
        )
        self.password_entry = Entry(self.window, font=20)
        self.password_entry.pack()
        Label(
            self.window,
            text="Password at least 5 characters",
            fg="grey",
            font=("Times New Roman", 10, "italic"),
            bg=BG_COLOR,
        ).pack()

        # Frame to hold the confirm and back button
        self.register_frame = Frame(self.window, bg=BG_COLOR, highlightthickness=0)
        self.register_frame.pack()

        button_frame = Frame(self.register_frame, bg=BG_COLOR, highlightthickness=0)
        button_frame.pack(pady=10)

        Button(
            button_frame,
            text="Back",
            width=10,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            command=self.homePage,
        ).pack(side="left", padx=5, pady=(20, 0))
        Button(
            button_frame,
            text="Confirm",
            width=10,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            command=self.confirm_registration,
        ).pack(side="left", padx=5, pady=(20, 0))

    ### Confirm by sign in
    def confirm_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username in self.users and self.users[username] == password:
            self.current_user = username
            messagebox.showinfo(
                "Login Successful", "Welcome back, {}!".format(username)
            )
            self.Recipe_Page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def login(self):
        # New page
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Login Center")
        self.window.geometry("1500x844")

        Label(
            self.window,
            text="Welcome back!",
            font=("Times New Roman", 60, "bold", "italic"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack(pady=(80, 50))
        Label(self.window, text="Username", font=20, bg=BG_COLOR, fg=FG_COLOR).pack()
        self.username_entry = Entry(self.window, font=20)
        self.username_entry.pack()

        Label(self.window, text="Password", font=20, bg=BG_COLOR, fg=FG_COLOR).pack(
            pady=(20, 0)
        )
        self.password_entry = Entry(self.window, font=20)
        self.password_entry.pack()

        # Frame to hold the confirm and back button
        self.login_frame = Frame(self.window, bg=BG_COLOR, highlightthickness=0)
        self.login_frame.pack()

        button_frame = Frame(self.login_frame, bg=BG_COLOR, highlightthickness=0)
        button_frame.pack(pady=10)

        Button(
            button_frame,
            text="Back",
            width=10,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            command=self.homePage,
        ).pack(side="left", padx=5, pady=(20, 0))
        Button(
            button_frame,
            text="Confirm",
            width=10,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            command=self.confirm_login,
        ).pack(side="left", padx=5, pady=(20, 0))

    ##############################################################################################################################
    ##############################################################################################################################
    def Recipe_Page(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.title("Kiyo Recipe Organizer")

        # Create a top bar with logo and title
        top_bar = Frame(self.window, bg=BG_COLOR, highlightthickness=0)
        top_bar.pack(side="top", fill="x")

        self.small_logo_image = PhotoImage(file=r"assets\small_Kiyo.png")
        canvas = Canvas(
            top_bar,
            bg=BG_COLOR,
            highlightthickness=0,
            width=self.small_logo_image.width(),
            height=self.small_logo_image.height(),
        )
        canvas.create_image(0, 0, anchor="nw", image=self.small_logo_image)
        canvas.pack(side="left", padx=20, pady=20)

        Label(
            top_bar,
            text="Kiyo Recipe",
            font=("Times New Roman", 50, "bold", "italic"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).place(relx=0.5, rely=0.5, anchor="center")

        Label(
            self.window,
            text="Let's Taste!",
            font=("Times New Roman", 25, "bold"),
            fg="#d56942",
            bg=BG_COLOR,
        ).pack(side="top", pady=(0, 10))

        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        operation_menu = Menu(
            menubar,
            tearoff=0,
            bg=BG_COLOR,
            fg=FG_COLOR,
            bd=0,
            activebackground=BTN_COLOR,
            activeforeground=FG_COLOR,
        )
        menubar.add_cascade(label="Operations", menu=operation_menu)
        operation_menu.add_command(label="Log out", command=self.homePage)
        operation_menu.add_command(label="Create Recipe", command=self.create_recipe)
        operation_menu.add_command(label="Edit Recipe", command=self.edit_recipe)
        operation_menu.add_command(label="Profile", command=self.profile)

        ### Search frame
        content = Frame(self.window, bg=BG_COLOR, highlightthickness=0)
        content.pack(fill="both", expand=True)

        search_frame = Frame(content, bg=BG_COLOR, highlightthickness=0)
        search_frame.pack(side="left", anchor="n", padx=10, pady=10)
        Label(
            search_frame,
            text="Search",
            font=("Arial", 12, "bold"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack(side="left", anchor="n", padx=(0, 4))

        input_frame = Frame(search_frame, bg=BG_COLOR, highlightthickness=0)
        input_frame.pack(side="left", anchor="n", padx=10)

        self.search_entry = Entry(input_frame, width=30, font=("Arial", 12))
        self.search_entry.pack(anchor="w")

        Label(
            input_frame,
            text="Search name/category/tags",
            fg="gray",
            font=("Arial", 10, "italic"),
            bg=BG_COLOR,
        ).pack(anchor="w", pady=(5, 0))

        # Get all unique categories from the recipes
        all_categories = sorted({r["category"] for r in recipes if r.get("category")})

        # Create a combobox for category selection
        categories_box = ttk.Combobox(
            input_frame, values=all_categories, state="readonly", font=("Arial", 10)
        )
        categories_box.pack(anchor="w", pady=(0, 10))

        # Define a function to handle category selection
        def category_select(event=None):
            value = categories_box.get()
            self.search_entry.delete(0, END)
            self.search_entry.insert(0, value)
            self.search_recipe()

        categories_box.bind("<<ComboboxSelected>>", category_select)

        self.search_icon = PhotoImage(file=r"assets\search.png")

        Button(
            search_frame,
            text="Get",
            image=self.search_icon,
            font=("Arial", 10),
            command=self.search_recipe,
        ).pack(side="left", anchor="n")

        Button(
            input_frame,
            text="Profile",
            width=15,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            font=("Arial", 13),
            command=self.profile,
        ).pack(anchor="w", padx=10, pady=10)

        # Create a canvas and scrollbar for scrolling through recipe cards
        recipe_area = Frame(content, bg=BG_COLOR, highlightthickness=0)
        recipe_area.pack(side="right", fill="both", expand=True)

        canvas = Canvas(recipe_area, bg=BG_COLOR, highlightthickness=0)
        vbar = Scrollbar(recipe_area, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vbar.set)

        vbar.pack(side="right", fill="y")
        canvas.pack(side="right", fill="both", expand=True)

        # Create a frame to hold the recipe cards
        card_frame = Frame(canvas, bg=BG_COLOR, highlightthickness=0)
        canvas_window = canvas.create_window((0, 0), window=card_frame, anchor="nw")

        canvas.bind(
            "<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width)
        )

        # size between card
        for column in range(5):
            card_frame.grid_columnconfigure(column, uniform="recipe")

        # clear the empty space when too little recipe
        card_frame.grid_columnconfigure(5, weight=1)

        card_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        self.window.bind_all(
            "<MouseWheel>",
            lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"),
        )
        self.project_folder = Path(__file__).resolve().parent
        self.card_frame = card_frame
        self.display_Recipes(recipes)

    # IMPORTANT loop to search and display
    def display_Recipes(self, recipe_list):
        for widget in self.card_frame.winfo_children():
            widget.destroy()

        self.recipe_images = []

        for i, recipe in enumerate(recipe_list):
            row, col = divmod(i, 5)

            card = Frame(self.card_frame)
            card.grid(row=row, column=col, padx=(0, 5), pady=10, sticky="nw")

            image_path = self.project_folder / recipe["image"]
            photo = PhotoImage(file=str(image_path))
            self.recipe_images.append(photo)

            Button(
                card,
                image=photo,
                bg=BTN_COLOR,
                fg=FG_COLOR,
                command=lambda r=recipe: self.show_details(r),
            ).pack()

            name = recipe["name"]
            if len(name) > 19:
                name = name[:18] + "..."
            else:
                name = name.strip()

            Label(
                card,
                text=name,
                font=("Arial", 13, "bold"),
                compound="top",
                justify="center",
                anchor="center",
                bg=BTN_COLOR,
                fg=FG_COLOR,
            ).pack(fill="both", expand=True)

    def show_details(self, recipe):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title(recipe["name"])
        Button(
            self.window,
            text="Back",
            width=10,
            height=2,
            bg=BTN_COLOR,
            fg=FG_COLOR,
            command=self.Recipe_Page,
        ).pack(anchor="nw", padx=10, pady=10)

        # Scroll(frame1)
        canvas = Canvas(self.window, bg=BG_COLOR, highlightthickness=0)
        vbar = Scrollbar(self.window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vbar.set)

        vbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Create a frame to hold the recipe details
        self.page_frame = Frame(canvas, bg=BG_COLOR, highlightthickness=0)
        canvas_window = canvas.create_window(
            (0, 0), window=self.page_frame, anchor="nw"
        )

        canvas.bind(
            "<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width)
        )

        self.page_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.bind_all(
            "<MouseWheel>",
            lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"),
        )

        ### frame2
        self.Title_frame = Frame(self.page_frame, bg=BG_COLOR, highlightthickness=0)
        self.Title_frame.pack()
        title_frame = Frame(self.Title_frame, bg=BG_COLOR, highlightthickness=0)
        title_frame.pack()

        Label(
            title_frame,
            text=recipe["name"],
            font=("Times New Roman", 35, "bold", "italic"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack(pady=15)

        # photo
        self.project_folder = Path(__file__).resolve().parent
        image_path = self.project_folder / recipe["image"]
        self.photo = PhotoImage(file=str(image_path))
        Label(title_frame, image=self.photo).pack(pady=5)
        Label(
            title_frame,
            text="Category: " + recipe["category"],
            bg=BG_COLOR,
            fg="#d56942",
            font=("Times New Roman", 13, "bold"),
        ).pack(pady=10)
        Button(
            title_frame,
            text="Customize",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            font=("Arial", 10, "bold"),
            width=10,
            height=2,
            command=lambda: self.customize(recipe),
        ).pack(pady=5)

        # frame3
        self.details_frame = Frame(self.page_frame, bg=BG_COLOR, highlightthickness=0)
        self.details_frame.pack()
        ing_frame = Frame(self.details_frame, bg=BG_COLOR, highlightthickness=0)
        ing_frame.pack(anchor="w", pady=20)
        # show ingredients
        Label(
            ing_frame,
            text="Ingredients:",
            font=("CourierNew", 20, "bold", "italic"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack(anchor="w")

        for item in recipe["ingredients"]:
            ingredient_text = (
                f"{item['name']} ："
                f"{item['amount'] if item['amount'] is not None else ''} "
                f"{item['unit']}"
            )
            Label(
                ing_frame,
                text=ingredient_text,
                font=("Arial", 13),
                bg=BG_COLOR,
                fg=FG_COLOR,
            ).pack(side="top", anchor="w", pady=2)

        ins_frame = Frame(self.details_frame, bg=BG_COLOR, highlightthickness=0)
        ins_frame.pack(pady=25)
        # show instructions
        Label(
            ins_frame,
            text="Instructions:",
            font=("CourierNew", 20, "bold", "italic"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack()
        # for loop
        for i, step in enumerate(recipe["steps"], start=1):
            Label(
                ins_frame,
                text=f"{i}. {step}",
                wraplength=1000,
                font=("Arial", 13),
                bg=BG_COLOR,
                fg=FG_COLOR,
            ).pack(anchor="w", pady=5)

    def customize(self, recipe):
        self.c_window = Toplevel()
        self.c_window.title("Customize Recipe")
        self.c_window.geometry("550x500")
        self.c_window.config(menu=Menu(self.c_window), bg=BG_COLOR)

        Label(
            self.c_window,
            text=f"Customize: {recipe['name']}",
            bg=BG_COLOR,
            fg=FG_COLOR,
            font=("Times New Roman", 20, "bold"),
        ).pack(pady=10)

        Label(
            self.c_window,
            text="Select an ingredient:",
            font=("Arial", 10),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack(pady=(15, 0))

        ingredient_text = [
            item["name"]
            for item in recipe["ingredients"]
            if item["amount"] is not None and item["amount"] > 0
        ]

        ingredient_box = ttk.Combobox(
            self.c_window, values=ingredient_text, state="readonly", font=("Arial", 10)
        )
        ingredient_box.pack()

        Label(
            self.c_window,
            text="Enter amount you have:",
            font=("Arial", 10),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack(pady=(25, 0))
        amount_entry = Entry(self.c_window, font=("Arial", 10))
        amount_entry.pack()

        self.result_frame = Frame(self.c_window, bg=BG_COLOR, highlightthickness=0)
        self.result_frame.pack()

        Button(
            self.c_window,
            text="Calculate",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            width=8,
            height=2,
            command=lambda: self.calculate_cuztomize(
                recipe, ingredient_box, amount_entry, self.result_frame
            ),
        ).pack(pady=35)

    def calculate_cuztomize(self, recipe, ingredient_box, amount_entry, result_frame):
        selected = ingredient_box.get()
        user_entry = amount_entry.get()

        if not selected:
            messagebox.showerror("Error", "Please select an ingredient.")
            return
        if not user_entry.strip():
            messagebox.showerror("Errror", "Please enter a number.")
            return
        try:
            user_entry = float(user_entry)
            if user_entry <= 0:
                messagebox.showerror("Error", "Amount must be greater than 0.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        for item in recipe["ingredients"]:
            if item["name"] == selected:
                original_amount = item["amount"]
                break

        # Formula to calculate
        ratio = user_entry / original_amount

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        Label(
            self.result_frame,
            text="Customized Ingredients:",
            bg=BG_COLOR,
            fg="#d56942",
            font=("CourierNew", 14, "bold", "italic"),
        ).pack(pady=(30, 5))
        for item in recipe["ingredients"]:
            if item["amount"] is not None:
                new_amount = item["amount"] * ratio

                Label(
                    result_frame,
                    bg=BG_COLOR,
                    fg=FG_COLOR,
                    text=f"{item['name']}: {new_amount:.2f} {item['unit']}",
                    font=("Arial", 12),
                ).pack(anchor="w")

    def search_recipe(self):
        search_text = self.search_entry.get().strip().lower()

        search_results = [
            recipe
            for recipe in recipes
            if search_text in recipe["name"].lower()
            or search_text in recipe.get("category", "").lower()
            or any(search_text in tag.lower() for tag in recipe.get("tags", []))
        ]

        self.display_Recipes(search_results)

    #######################################################################################################################################
    def profile(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title("User Center")

        Button(
            self.window,
            text="Back",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            width=10,
            height=2,
            command=self.Recipe_Page,
        ).pack(anchor="nw", padx=10, pady=10)

        Label(
            self.window,
            text="My Profile",
            bg=BG_COLOR,
            fg=FG_COLOR,
            font=("CourierNew", 30, "bold", "italic"),
        ).pack(pady=15)

        self.profile_image = PhotoImage(file="pfp.png")
        canvas = Canvas(
            self.window,
            width=self.profile_image.width(),
            height=self.profile_image.height(),
            bg=BG_COLOR,
            highlightthickness=0,
        )
        canvas.create_image(0, 0, anchor="nw", image=self.profile_image)
        canvas.pack()

        # show user details
        user_text = f"Username: {self.current_user}"
        Label(
            self.window,
            text=user_text,
            font=("Arial", 14, "bold"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack(pady=(10, 5))

        Button(
            self.window,
            text="View My Recipes",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            width=20,
            height=2,
            font=("Arial", 10, "bold"),
            command=self.my_Recipe,
        ).pack(padx=15, pady=30)

    def save_my_recipes(self):
        lines = []
        for my_recipe in self.my_recipes:
            # Replace '|' to protect delimiter and escape newlines so each recipe stays on 1 line
            user = my_recipe["user"].replace("|", "/")
            name = my_recipe["name"].replace("|", "/").replace("\n", "\\n")
            ingredients = (
                my_recipe["ingredients"].replace("|", "/").replace("\n", "\\n")
            )
            instructions = (
                my_recipe["instructions"].replace("|", "/").replace("\n", "\\n")
            )
            image = my_recipe["image"].replace("|", "/")
            lines.append(f"{user}|{name}|{ingredients}|{instructions}|{image}")

        content = "\n".join(lines) + ("\n" if lines else "")
        self.MY_RECIPE_FILE.write_text(content, encoding="utf-8")

    def load_my_recipes(self):
        loaded = []
        if self.MY_RECIPE_FILE.exists():
            lines = self.MY_RECIPE_FILE.read_text(encoding="utf-8").splitlines()
            for line in lines:
                parts = line.split("|")
                if len(parts) == 5:
                    loaded.append(
                        {
                            "user": parts[0],
                            "name": parts[1].replace("\\n", "\n"),
                            "ingredients": parts[2].replace("\\n", "\n"),
                            "instructions": parts[3].replace("\\n", "\n"),
                            "image": parts[4],
                        }
                    )
        return loaded

    def my_Recipe(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title("My Recipe")

        Button(
            self.window,
            text="Back",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            width=10,
            height=2,
            command=self.profile,
        ).pack(anchor="nw", padx=10, pady=10)

        Button(
            self.window,
            text="Create Recipe",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            width=13,
            height=2,
            font=("Arial", 10, "bold"),
            command=self.create_recipe,
        ).pack(padx=10, pady=10)

        # Filter recipes belonging to the logged-in user
        user_recipes = [
            user for user in self.my_recipes if user["user"] == self.current_user
        ]
        if not user_recipes:
            Label(
                self.window,
                text="0 recipes — Please create one :)",
                bg=BG_COLOR,
                fg=FG_COLOR,
                font=("Arial", 16, "bold"),
            ).pack(pady=30)

        self.recipe_photo_images = []

        # Show recipe in user profile
        for my_recipe in user_recipes:
            card = LabelFrame(
                self.window,
                text=my_recipe["name"],
                bg=BG_COLOR,
                fg=FG_COLOR,
                padx=10,
                pady=8,
            )
            card.pack(fill="x", padx=20, pady=8)

            Label(
                card,
                text="Ingredients: " + my_recipe["ingredients"],
                bg=BG_COLOR,
                fg=FG_COLOR,
                wraplength=1000,
                justify="left",
            ).pack(anchor="w")

            Label(
                card,
                text="Instructions: " + my_recipe["instructions"],
                bg=BG_COLOR,
                fg=FG_COLOR,
                wraplength=1000,
                justify="left",
            ).pack(anchor="w", pady=5)

            if my_recipe["image"]:
                try:
                    image_path = Path(__file__).resolve().parent / my_recipe["image"]
                    image = PhotoImage(file=str(image_path))
                    self.recipe_photo_images.append(image)
                    Label(card, image=image, bg=BG_COLOR).pack(anchor="w", pady=5)
                except Exception:
                    Label(
                        card,
                        text="Photo: " + Path(my_recipe["image"]).name,
                        bg=BG_COLOR,
                        fg=FG_COLOR,
                    ).pack(anchor="w")

            action_frame = Frame(card, bg=BG_COLOR)
            action_frame.pack(anchor="e", pady=(5, 0))

            Button(
                action_frame,
                text="Edit",
                bg=BTN_COLOR,
                fg=FG_COLOR,
                width=8,
                command=lambda r=my_recipe: self.edit_recipe(r),
            ).pack(side="left", padx=5)

            Button(
                action_frame,
                text="Delete",
                bg="#d9534f",
                fg="white",
                width=8,
                command=lambda r=my_recipe: self.delete_recipe(r),
            ).pack(side="left")

    # Save Button
    def save_recipe(self):
        name = self.recipe_name_entry.get("1.0", "end").strip()
        ingredients = self.ingredients_entry.get("1.0", "end").strip()
        instructions = self.instructions_entry.get("1.0", "end").strip()

        if not name or not ingredients or not instructions:
            messagebox.showerror("Missing details", "Details cannot be blank.")
            return

        self.my_recipes.append(
            {
                "user": self.current_user,
                "name": name,
                "ingredients": ingredients,
                "instructions": instructions,
                "image": self.recipe_photo_path,
            }
        )
        self.save_my_recipes()

        messagebox.showinfo("Saved", "You can view My Recipe to edit or delete.")
        self.my_Recipe()

    def choose_recipe_photo(self):
        path = filedialog.askopenfilename(
            title="Choose a recipe photo",
            filetypes=[("PNG or GIF images", "*.png *.gif")],
        )
        if path:
            image = PhotoImage(file=path)

            # Change the file size
            max_height = 200
            if image.height() > max_height:
                scale = max(1, image.height() // max_height)
                image = image.subsample(scale, scale)

            # Validate images folder
            project_dir = Path(__file__).resolve().parent
            images_dir = project_dir / "images"
            images_dir.mkdir(exist_ok=True)

            # Make sure the file name wont conflict & Store the file
            new_filename = f"{int(time.time())}_{Path(path).stem}.png"
            save_path = images_dir / new_filename
            image.write(str(save_path), format="png")

            # Store variable
            self.recipe_photo_path = f"images/{new_filename}"
            self.photo_name_label.config(text=new_filename)
            self.upload_photo = image
            self.photo_preview_label.config(image=self.upload_photo)

    def create_recipe(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        # Create a new window for recipe creation
        self.window.title("Create Recipe")

        ######Upload Photo
        Label(
            self.window,
            text="Recipe Photo:",
            font=("Arial", 10, "bold"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).grid(row=1, column=0, sticky="w", padx=10, pady=5)

        photo_frame = Frame(self.window, bg=BG_COLOR)
        photo_frame.grid(row=1, column=1, columnspan=2, sticky="w", padx=5, pady=5)

        self.recipe_photo_path = ""
        self.upload_photo = None

        self.photo_preview_label = Label(photo_frame, bg=BG_COLOR)
        self.photo_preview_label.pack(side="left", padx=(0, 10))

        self.photo_name_label = Label(
            photo_frame,
            text="No photo selected",
            font=("Arial", 10, "bold"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        )
        self.photo_name_label.pack(side="left", padx=(0, 10))

        Button(
            photo_frame,
            text="Choose Photo",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            command=self.choose_recipe_photo,
        ).pack(side="left")

        # Create labels and entry fields for recipe details
        Label(
            self.window,
            text="Recipe Name:",
            font=("Arial", 10, "bold"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.recipe_name_entry = Text(self.window, width=150, height=2)
        self.recipe_name_entry.grid(row=2, column=1, sticky="w", pady=5)

        Label(
            self.window,
            text="Ingredients:",
            font=("Arial", 10, "bold"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).grid(row=3, column=0, sticky="nw", padx=10, pady=5)
        self.ingredients_entry = Text(self.window, width=150, height=12)
        self.ingredients_entry.grid(row=3, column=1, sticky="w", pady=5)

        Label(
            self.window,
            text="Instructions:",
            font=("Arial", 10, "bold"),
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).grid(row=4, column=0, sticky="nw", padx=10, pady=5)
        self.instructions_entry = Text(self.window, width=150, height=12)
        self.instructions_entry.grid(row=4, column=1, sticky="w", pady=5)

        # Create a frame to hold the save button
        self.save_frame = Frame(self.window, bg=BG_COLOR, highlightthickness=0)
        self.save_frame.grid(row=5, column=1, columnspan=2, sticky="e", pady=10)

        button_frame = Frame(self.save_frame, bg=BG_COLOR, highlightthickness=0)
        button_frame.grid(row=0, column=0, sticky="w")

        Button(
            button_frame,
            text="Back",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            width=10,
            height=2,
            command=lambda: self.my_Recipe(),
        ).pack(side="left", padx=5)

        Button(
            button_frame,
            text="Save Recipe",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            width=10,
            height=2,
            command=lambda: self.save_recipe(),
        ).pack(side="left", padx=5)

    def edit_recipe(self, target_recipe=None):
        user_recipes = [
            user for user in self.my_recipes if user["user"] == self.current_user
        ]
        if target_recipe is None:
            if not user_recipes:
                messagebox.showinfo(
                    "No Recipes", "You don't have any recipes to edit yet."
                )
                self.my_Recipe()
                return
            target_recipe = user_recipes[0]

        self.editing_recipe = target_recipe

        for widget in self.window.winfo_children():
            widget.destroy()
        # Create a new window for recipe editing
        self.window.title("Edit Recipe")

        Label(self.window, text="Recipe Name:", bg=BG_COLOR, fg=FG_COLOR).grid(
            row=1, column=0
        )
        self.recipe_name_entry = Text(self.window, width=100, height=1)
        self.recipe_name_entry.grid(row=1, column=1, pady=5)

        Label(self.window, text="Ingredients:", bg=BG_COLOR, fg=FG_COLOR).grid(
            row=2, column=0
        )
        self.ingredients_entry = Text(self.window, width=100, height=8)
        self.ingredients_entry.grid(row=2, column=1, pady=5)

        Label(self.window, text="Instructions:", bg=BG_COLOR, fg=FG_COLOR).grid(
            row=3, column=0
        )
        self.instructions_entry = Text(self.window, width=100, height=8)
        self.instructions_entry.grid(row=3, column=1, pady=5)

        # Create a frame to hold the save button
        self.save_frame = Frame(self.window, bg=BG_COLOR, highlightthickness=0)
        self.save_frame.grid(row=4, column=1, pady=10)

        button_frame = Frame(self.save_frame, bg=BG_COLOR, highlightthickness=0)
        button_frame.pack(pady=10)

        back_button = Button(
            button_frame,
            text="Back",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            width=10,
            height=2,
            command=self.Recipe_Page,
        )
        back_button.pack(side="left", padx=5)
        save_button = Button(
            button_frame,
            text="Save Changes",
            bg=BTN_COLOR,
            fg=FG_COLOR,
            width=10,
            height=2,
            command=self.save_edited_recipe,
        )
        save_button.pack(side="left", padx=5)

        # Here you can add code to save the recipe details to a file or database
        print(f"Recipe Name: {recipe_name}")
        print(f"Ingredients: {ingredients}")
        print(f"Instructions: {instructions}")

    def delete_recipe(self, target_recipe):
        if messagebox.askyesno("Confirm Delete", f"Delete '{target_recipe['name']}'?"):
            self.my_recipes.remove(target_recipe)
            self.save_my_recipes()
            self.my_Recipe()

    def save_edited_recipe(self):
        # Get the edited recipe details from the entry fields
        recipe_name = self.recipe_name_entry.get().strip()
        ingredients = self.ingredients_entry.get().strip()
        instructions = self.instructions_entry.get().strip()

        # Here you can add code to save the edited recipe details to a file or database
        print(f"Edited Recipe Name: {recipe_name}")
        print(f"Edited Ingredients: {ingredients}")
        print(f"Edited Instructions: {instructions}")


Recipe_Organizer_System()
