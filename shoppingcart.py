import tkinter as tk

# Product list with prices
product_prices = {
    "Toy": 10,
    "Book": 15,
    "Stationary": 5,
    "Chips": 2
}

# Calculate total cost
def calculate_total():
    total = 0
    for item, var in cart_vars.items():
        if var.get():
            total += product_prices[item]
    result_label.config(text=f"Total Cost: ${total}")

# GUI Setup
root = tk.Tk()
root.title("Shopping Cart Calculator")
root.geometry("300x300")

tk.Label(root, text="Pick items to buy and add to your cart:", font=("Arial", 12)).pack(pady=10)

# Checkbox dictionary
cart_vars = {}
for item, price in product_prices.items():
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=f"{item} (${price})", variable=var)
    cb.pack(anchor='w', padx=20)
    cart_vars[item] = var

# Calculate button
tk.Button(root, text="Calculate Total Cost", command=calculate_total).pack(pady=15)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()