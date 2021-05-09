import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_column_names()
        #self.create_items_and_predictions()

    #list of names of people passed as parameter
    def create_column_names(self, names = ["Leon", "Jason", "Wesley"]):
        row = 0
        col = 0
        self.items_column = tk.Label(text="").grid(row=row,column=col)
        col += 1
        self.items_column = tk.Label(text="Items").grid(row=row,column=col)

        #total quantity
        col += 1
        self.items_quantity = tk.Label(text="Quantity", relief=tk.GROOVE).grid(row=row,column=col)

        for name in names:
            col += 1
            tk.Label(text=name, relief=tk.RIDGE).grid(row=row,column=col)

    def create_items_and_predictions(self, items = ["Leon", "Jason", "Wesley"], predictions_for_items = [["Leon", "Jason", "Wesley"], ["Leon", "Jason", "Wesley"], ["Leon", "Jason", "Wesley"]]):
        #add items
        row = 1

        for item in items:
            # #image
            col = 0
            # tk.Label(image=items.image).grid(row=row,column=col)

            #description
            col += 1
            #tk.Label(text=items.name, justify=tk.CENTER, relief=tk.RIDGE).grid(row=row,column=col)
            tk.Label(text=items[1], justify=tk.CENTER, relief=tk.RIDGE).grid(row=row,column=col)

            #quantity
            col += 1
            #tk.Label(text=items.quantity, relief=tk.RIDGE).grid(row=row,column=col)
            tk.Label(text=items[2], relief=tk.RIDGE).grid(row=row,column=col)
            row += 1

        #add predictions
        row = 1
        col = 2
        for predictions in predictions_for_items:
            for prediction in predictions:
                prediction_box = tk.Entry(relief=tk.RIDGE).grid(row=row,column=col)
                prediction_box = tk.insert(0, prediction)
                col += 1
            row += 1

root = tk.Tk()
app = GUI(master=root)
app.mainloop()