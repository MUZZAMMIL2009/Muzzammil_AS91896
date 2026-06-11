from tkinter import *

root = Tk()
root.title("Income Calculator")
root.geometry("900x600")
root.configure(bg="#1F0954")

# Centering window (same as homepage)
window_width = 900
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Main card (same style as homepage)
main_frame = Frame(root, bg="#091F92", width=700, height=450)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# TITLE
title = Label(main_frame,
              text="Income Calculator",
              font=("Arial", 22, "bold"),
              fg="white",
              bg="#091F92")
title.pack(pady=20)

# SUBTEXT (matches style consistency)
subtitle = Label(main_frame,
                 text="Enter your income details below",
                 font=("Arial", 12),
                 fg="white",
                 bg="#091F92")
subtitle.pack(pady=5)

# Placeholder layout rows (no inputs yet)
row1 = Label(main_frame, text="Hourly Wage", fg="white", bg="#091F92")
row1.pack(pady=10)

row2 = Label(main_frame, text="Hours per Week", fg="white", bg="#091F92")
row2.pack(pady=10)

row3 = Label(main_frame, text="Number of Weeks", fg="white", bg="#091F92")
row3.pack(pady=10)

# Result placeholder
result_label = Label(main_frame,
                     text="Result: ",
                     font=("Arial", 11, "bold"),
                     fg="#FFCA28",
                     bg="#091F92")
result_label.pack(pady=20)

root.mainloop()
