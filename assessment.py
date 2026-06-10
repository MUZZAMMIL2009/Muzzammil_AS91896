from tkinter import *

root = Tk()
root.title("Financial Toolkit")
root.geometry("900x600")
root.configure(bg="#1c0333")

# center window
window_width = 900
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# main frame
main_frame = Frame(root, bg="#091F92", width=600, height=400)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# TEXT
title_label = Label(main_frame, text="Financial Toolkit",
                   font=("Arial", 26, "bold"),
                   fg="#FFCA28", bg="#091F92")
title_label.pack(pady=20)

subtitle_label = Label(main_frame,
                      text="Your all-in-one calculator system",
                      font=("Arial", 14),
                      fg="white", bg="#091F92")
subtitle_label.pack(pady=5)

instruction_label = Label(main_frame,
                         text="Choose your calculator:",
                         font=("Arial", 11),
                         fg="white", bg="#091F92")
instruction_label.pack(pady=10)

# BUTTONS

# create a separate frame to hold buttons in a row
# this keeps layout organised and easy to control

button_frame = Frame(main_frame, bg="#091F92")
button_frame.pack(pady=20)

# Define a reusable style dictionary for all buttons
# This ensures consistent appearance and avoids repeating code

btn_style = {
   "font": ("Arial", 11, "bold"),
   "bg": "#6d28d9",
   "fg": "white",
   "width": 18,
   "height": 2,
   "bd": 0
}

#income calculator button

income_btn = Button(button_frame, text="Income Calculator", **btn_style)
income_btn.pack(side="left", padx=10)

#savings calculator button

savings_btn = Button(button_frame, text="Savings Calculator", **btn_style)
savings_btn.pack(side="left", padx=10)

#loan calculator button

loan_btn = Button(button_frame, text="Loan Calculator", **btn_style)
loan_btn.pack(side="left", padx=10)

#run the completed application

root.mainloop()
