# HELP PAGE - TRIAL 1: BASIC FRAME / CARD
# This trial only creates the Help page background and main rounded
# container. Text and buttons are added in later trials.
# ============================================================


import tkinter as tk


# Fixed window size so screenshots stay consistent on school computers.
WIDTH = 900
HEIGHT = 600


# Same colours as the rest of my Financial Toolkit pages.
ROOT_BG = "#241b4a"
CARD_BG = "#2821a3"
BUTTON_BG = "#6d20f6"
WHITE = "#ffffff"
BLACK = "#000000"


# Create the main Tkinter window.
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




def rounded_rect(canvas, x1, y1, x2, y2, radius, fill, outline=None, width=1, tags=None):
    """Draw a rounded rectangle using Canvas.


    I used this instead of a normal Frame because my design has rounded
    purple sections, while standard Tkinter frames are very square.
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




def make_canvas():
    """Create the drawing area for the page."""
    canvas = tk.Canvas(
        root,
        width=WIDTH,
        height=HEIGHT,
        bg=ROOT_BG,
        highlightthickness=0
    )
    canvas.pack(fill="both", expand=True)
    return canvas




canvas = make_canvas()


# Main rounded card used to hold all Help page content.
rounded_rect(canvas, 25, 50, 875, 550, 18, fill=CARD_BG)


root.mainloop()


