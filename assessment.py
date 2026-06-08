from tkinter import *

root = Tk()
root.title("Financial Toolkit")
root.geometry("900x600")
root.configure(bg="#1F0954")

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

# TEXT ELEMENTS

# main title, large, bold, high contrast for visibility
title_label = Label(main_frame, text="Financial Toolkit",
font=("Arial", 26, "bold"), #larger font for emphasis
fg="yellow", bg="#091F92") #high contrast colour
title_label.pack(pady=20) #vertical spacing from the top

subtitle_label = Label(main_frame, #subtitle - explains purpose of the system
text="Your all-in-one calculator system",
font=("Arial", 14),
fg="white", bg="#091F92")
subtitle_label.pack(pady=5)

#instruction text - guides the user on what to do next
instruction_label = Label(main_frame,
text="Choose your calculator:",
font=("Arial", 11),
fg="white", bg="#091F92")
instruction_label.pack(pady=10)

root.mainloop()
