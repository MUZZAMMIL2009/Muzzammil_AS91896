# HOME PAGE - TRIAL 2: ADDING TEXT
# ============================================================
# This file builds on Trial 1 by adding the title and subtitles.
# The goal is to show visual hierarchy: a large yellow title, then
# smaller white supporting text underneath. Buttons are still not
# included at this stage because they are added in Trial 3.
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


# HOME PAGE - TRIAL 2
# Adds the title and subtitles from the design.


canvas = make_canvas()


rounded_rect(canvas, 35, 140, 865, 410, 20, fill=CARD_BG)


canvas.create_text(
    WIDTH / 2,
    210,
    text="The Ultimate Financial Toolkit",
    fill=YELLOW,
    font=("Arial Black", 31),
    anchor="center"
)


canvas.create_text(
    WIDTH / 2,
    270,
    text="Simple financial tools for students",
    fill=WHITE,
    font=("Arial", 20, "bold"),
    anchor="center"
)


canvas.create_text(
    WIDTH / 2,
    305,
    text="Choose your calculator",
    fill=WHITE,
    font=("Arial", 18, "bold"),
    anchor="center"
)


root.mainloop()
