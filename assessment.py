# HOME PAGE - TRIAL 1: BASIC LAYOUT ONLY
# ============================================================
# This is for the first screenshot of Component 1.
# It only shows the main window, the dark background, and the
# rounded central card/container from the design. Text and buttons
# are intentionally not included yet because they are added in
# later trials.
#
# Canvas is used instead of a normal Frame because Canvas lets me
# draw smoother rounded shapes, which matches my Canva design better
# while still staying inside normal Tkinter.
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


# HOME PAGE - TRIAL 1
# Basic layout only: background and centred rounded card.


canvas = make_canvas()


rounded_rect(canvas, 35, 140, 865, 410, 20, fill=CARD_BG)


root.mainloop()


