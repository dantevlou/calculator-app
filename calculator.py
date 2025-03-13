import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("415x500")

# Display screen
entry = tk.Entry(root, width=21, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=14, pady=14)

# Button layout
buttons = [
    '7', '8', '9', '÷',
    '4', '5', '6', '×',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
]

row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 18)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Runs the application
root.mainloop()