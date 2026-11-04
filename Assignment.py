from tkinter import *

class Restaurant_Ordering_System:
    def __init__(self):
        # Create the main window and set its title
        window = Tk()
        window.title("3A3D Restaurant")

        self.canvas = Canvas(window, width=400, height=300, bg="lightblue")
        self.canvas.pack()

        # Create a frame to hold the widgets
        frame = Frame(window)
        frame.pack()
        self.label = Label(frame, text="Welcome to the 3A3D Restaurant")
        self.label.pack()

        self.order_button = Button(frame, text="Place Order", command=self.place_order)
        self.order_button.pack()

        self.exit_button = Button(frame, text="Exit", command=window.quit)
        self.exit_button.pack()

        window.mainloop()

    # Create a method to handle placing an order
    def place_order(self):
        self.order_window = Toplevel()
        self.order_window.title("Place Order")

        self.menu_label = Label(self.order_window, text="Menu")
        self.menu_label.pack()

        self.menu_items = ["Pizza", "Burger", "Pasta", "Salad"]
        self.menu_var = StringVar(value=self.menu_items)

        self.menu_listbox = Listbox(self.order_window, listvariable=self.menu_var, selectmode=SINGLE)
        self.menu_listbox.pack()

        self.quantity_label = Label(self.order_window, text="Quantity")
        self.quantity_label.pack()

        self.quantity_entry = Entry(self.order_window)
        self.quantity_entry.pack()

        self.submit_button = Button(self.order_window, text="Submit Order", command=self.submit_order)
        self.submit_button.pack()

Restaurant_Ordering_System()
