# INCOME TAX CALCULATOR - TRIAL 1: LAYOUT AND TEXT
# ============================================================
# This file creates the first visual stage of the Income Tax page.
# It shows the card, page title, input labels, divider lines, and
# result placeholder. It does not include working Entry boxes yet.
# ============================================================


import tkinter as tk


# Fixed window size so screenshots stay consistent on school computers.
WIDTH = 900
HEIGHT = 600


# Colour constants for the interface. Using constants avoids repeating hex codes everywhere.
ROOT_BG = "#241b4a"
CARD_BG = "#2821a3"
BUTTON_BG = "#6d20f6"
WHITE = "#ffffff"
YELLOW = "#ffe83d"
BLACK = "#000000"
ENTRY_BG = "#d9d9d9"


# Create the one main Tkinter window for this trial.
root = tk.Tk()
root.title("Financial Toolkit")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg=ROOT_BG)
root.resizable(False, False)


# Centre the window on the school monitor.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (WIDTH / 2))
y = int((screen_height / 2) - (HEIGHT / 2))
root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")




# Draws rounded rectangles for cards/buttons, because default Tkinter widgets are too square.




def rounded_rect(canvas, x1, y1, x2, y2, radius, fill, outline=None, width=1, tags=None):
    """Draw a rounded rectangle using a smooth Canvas polygon.


    I am using this because normal Tkinter Frames and Buttons are too square,
    while my design uses rounded purple cards and buttons.
    """
    if outline is None:
        outline = fill


    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]


    return canvas.create_polygon(
        points,
        smooth=True,
        fill=fill,
        outline=outline,
        width=width,
        tags=tags
    )




# Creates the Canvas, which works like the drawing surface for the page.




def make_canvas():
    """Create the main drawing area for the current page."""
    canvas = tk.Canvas(
        root,
        width=WIDTH,
        height=HEIGHT,
        bg=ROOT_BG,
        highlightthickness=0
    )
    canvas.pack(fill="both", expand=True)
    return canvas


# INCOME TAX PAGE - TRIAL 1
# Layout and text only. No entries or working logic yet.


canvas = make_canvas()


rounded_rect(canvas, 25, 50, 875, 550, 18, fill=CARD_BG)


canvas.create_text(
    60,
    115,
    text="Income Tax Calculator",
    fill=WHITE,
    font=("Arial Black", 26),
    anchor="w"
)


rounded_rect(canvas, 745, 92, 855, 134, 18, fill=BUTTON_BG, outline=BLACK, width=2)
canvas.create_text(800, 113, text="Help", fill=WHITE, font=("Arial", 10, "bold"))


canvas.create_text(105, 205, text="Hourly Wage", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
canvas.create_text(465, 205, text="Hours worked per week", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
canvas.create_line(25, 245, 875, 245, fill=WHITE, width=2)


canvas.create_text(45, 275, text="Time Period (Weeks)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
canvas.create_line(25, 315, 875, 315, fill=WHITE, width=2)


canvas.create_text(
    60,
    360,
    text="Result: In X weeks, you will take home $000",
    fill=WHITE,
    font=("Arial", 15, "bold"),
    anchor="w"
)


root.mainloop()
