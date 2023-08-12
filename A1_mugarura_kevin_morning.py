import tkinter as tk
from tkinter import messagebox

class ReceiptPrintingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printing Program")

        self.items = []
        self.prices = []

        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()

        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()

        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.print_button = tk.Button(root, text="Print Receipt", command=self.print_receipt)
        self.print_button.pack()

    def add_item(self):
        item = self.item_entry.get()
        price = self.price_entry.get()

        if item and price:
            self.items.append(item)
            self.prices.append(price)
            messagebox.showinfo("Success", "Item added successfully.")
            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both item and price.")

    def print_receipt(self):
        if not self.items:
            messagebox.showerror("Error", "No items added to the receipt.")
            return

        receipt = "\n".join(f"{item} - ${price}" for item, price in zip(self.items, self.prices))
        total = sum(float(price) for price in self.prices)
        receipt += f"\nTotal: ${total:.2f}"

       
        messagebox.showinfo("Receipt", receipt)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiptPrintingApp(root)
    root.mainloop()

