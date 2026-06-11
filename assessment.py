from tkinter import *

root = Tk()
root.title("Income Calculator")
root.geometry("900x600")
root.configure(bg="#1F0954")

# Centering window
window_width = 900
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Main frame (same style)
main_frame = Frame(root, bg="#091F92", width=700, height=450)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# TITLE
title = Label(main_frame, text="Income Calculator",
font=("Arial", 22, "bold"),
fg="white", bg="#091F92")
title.pack(pady=20)

# INPUT FRAME (for alignment)
input_frame = Frame(main_frame, bg="#091F92")
input_frame.pack(pady=10)

# LEFT SIDE
Label(input_frame, text="Hourly Wage", fg="white", bg="#091F92").grid(row=0, column=0, padx=20, pady=10, sticky="w")
wage_entry = Entry(input_frame)
wage_entry.grid(row=0, column=1, padx=10)

Label(input_frame, text="Hours per Week", fg="white", bg="#091F92").grid(row=1, column=0, padx=20, pady=10, sticky="w")
hours_entry = Entry(input_frame)
hours_entry.grid(row=1, column=1, padx=10)

Label(input_frame, text="Number of Weeks", fg="white", bg="#091F92").grid(row=2, column=0, padx=20, pady=10, sticky="w")
weeks_entry = Entry(input_frame)
weeks_entry.grid(row=2, column=1, padx=10)

# RESULT
income_result = Label(main_frame,
text="Result: ",
font=("Arial", 11, "bold"),
fg="#ffca28",
bg="#091F92")
income_result.pack(pady=20)

# BUTTON FRAME (same as homepage)
button_frame = Frame(main_frame, bg="#091F92")
button_frame.pack(pady=20)

btn_style = {
"font": ("Arial", 11, "bold"),
"bg": "#6d28d9",
"fg": "white",
"width": 18,
"height": 2,
"bd": 0
}

home_btn = Button(button_frame, text="Home", **btn_style)
home_btn.pack(side="left", padx=10)

calc_btn = Button(button_frame, text="Calculate", **btn_style)
calc_btn.pack(side="left", padx=10)

loan_btn = Button(button_frame, text="Loans Calculator", **btn_style)
loan_btn.pack(side="left", padx=10)

root.mainloop()
