from tkinter import *

# Create the main application window
root = Tk()

# set the title shown at the top of the window
root.title("Financial Toolkit")

# set the fixed window size (width x height)
root.geometry("900x600")

# Apply a dark navy background to match the design theme
root.configure(bg="#1F0954")

# centering the window on screen

#defining the window size again for positioning calculations
window_width = 900
window_height = 600

#get the users screen width and height for responsiveness
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#calculate the x and y position so the window appears centered
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

#apply the calculated position to the window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# main frame

# create a frame to hold all content (as as the main layout container)
main_frame = Frame(root, bg="#091F92", width=600, height=400)

#place the frame in the exact center of the window
#relx/rely = 0.5 means 50% across and 50% down
main_frame.place(relx=0.5, rely=0.5, anchor="center")

#Start the application loop(keeps the window open and responsive)
root.mainloop()
