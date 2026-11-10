from tkinter import *

class Recipe_Organizer_System:
    def __init__(self):
        # Create the main window and set its title
        window = Tk()
        window.title("3A3D Recipe Organizer")

        logo_Image = PhotoImage(file = "3A-3D.png")
        self.canvas = Canvas(window, width=400, height=300, bg="white")
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=logo_Image)

        menubar = Menu(window)
        window.config(menu = menubar)

        operation_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operations", menu=operation_menu)
        operation_menu.add_command(label="Create Recipe", command=self.create_recipe)
        operation_menu.add_command(label="Edit Recipe", command=self.edit_recipe)
        operation_menu.add_command(label="Search Recipe", command=self.search_recipe)
        operation_menu.add_command(label="Exit", command=window.quit)

        # Create a frame to hold the widgets
        frame = Frame(window)
        frame.pack()
        self.label = Label(frame, text="Welcome to the 3A3D Recipe Organizer")
        self.label.pack()

        self.order_button = Button(frame, text="Create Recipe", command=self.create_recipe)
        self.order_button.pack()

        self.edit_button = Button(frame, text="Edit Recipe", command=self.edit_recipe)
        self.edit_button.pack()

        self.search_button = Button(frame, text="Search Recipe", command=self.search_recipe)
        self.search_button.pack()

        self.exit_button = Button(frame, text="Exit", command=window.quit)
        self.exit_button.pack()

        window.mainloop()

    def create_recipe(self):
        # Create a new window for recipe creation
        recipe_window = Toplevel()
        recipe_window.title("Create Recipe")

        # Create labels and entry fields for recipe details
        Label(recipe_window, text="Recipe Name:").grid(row=0, column=0)
        self.recipe_name_entry = Entry(recipe_window)
        self.recipe_name_entry.grid(row=0, column=1)

        Label(recipe_window, text="Ingredients:").grid(row=1, column=0)
        self.ingredients_entry = Entry(recipe_window)
        self.ingredients_entry.grid(row=1, column=1)

        Label(recipe_window, text="Instructions:").grid(row=2, column=0)
        self.instructions_entry = Entry(recipe_window)
        self.instructions_entry.grid(row=2, column=1)

        # Create a button to save the recipe
        save_button = Button(recipe_window, text="Save Recipe", command=self.save_recipe)
        save_button.grid(row=3, columnspan=2)

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
        # Create a new window for recipe editing
        edit_window = Toplevel()
        edit_window.title("Edit Recipe")

        # Create labels and entry fields for recipe details
        Label(edit_window, text="Recipe Name:").grid(row=0, column=0)
        self.edit_recipe_name_entry = Entry(edit_window)
        self.edit_recipe_name_entry.grid(row=0, column=1)

        Label(edit_window, text="Ingredients:").grid(row=1, column=0)
        self.edit_ingredients_entry = Entry(edit_window)
        self.edit_ingredients_entry.grid(row=1, column=1)

        Label(edit_window, text="Instructions:").grid(row=2, column=0)
        self.edit_instructions_entry = Entry(edit_window)
        self.edit_instructions_entry.grid(row=2, column=1)

        # Create a button to save the edited recipe
        save_button = Button(edit_window, text="Save Changes", command=self.save_edited_recipe)
        save_button.grid(row=3, columnspan=2)

    def search_recipe(self):
        # Create a new window for recipe searching
        search_window = Toplevel()
        search_window.title("Search Recipe")

        # Create a label and entry field for recipe name
        Label(search_window, text="Recipe Name:").grid(row=0, column=0)
        self.search_recipe_name_entry = Entry(search_window)
        self.search_recipe_name_entry.grid(row=0, column=1)

        # Create a button to search for the recipe
        search_button = Button(search_window, text="Search", command=self.perform_search)
        search_button.grid(row=1, columnspan=2)

Recipe_Organizer_System()

