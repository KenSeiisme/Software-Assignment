from tkinter import *

class Recipe_Organizer_System:
    def __init__(self):
        # Create the main window and set its title
        window = Tk()
        window.title("3A3D Recipe Organizer")

        self.canvas = Canvas(window, width=400, height=300, bg="lightblue")
        self.canvas.pack()

        menubar = Menu(window)
        window.config(menu = menubar)

        operaion_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operations", menu=operaion_menu)
        operaion_menu.add_command(label="Create Recipe", command=self.create_recipe)
        operaion_menu.add_command(label="Exit", command=window.quit)

        # Create a frame to hold the widgets
        frame = Frame(window)
        frame.pack()
        self.label = Label(frame, text="Welcome to the 3A3D Recipe Organizer")
        self.label.pack()

        self.order_button = Button(frame, text="Create Recipe", command=self.create_recipe)
        self.order_button.pack()

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

Recipe_Organizer_System()

