# HOME PAGE - TRIAL 3: ADDING NAVIGATION BUTTONS
# ============================================================
# This file completes the visual home page by adding the three
# calculator buttons. The custom canvas_button function is used so
# every button has the same rounded shape, purple colour, white text,
# and spacing.
#
# In this trial file, the buttons are mainly for the screenshot and
# visual development. The connected app version links buttons to pages.

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


# Draws one reusable rounded button style so all buttons remain consistent.


def canvas_button(canvas, x, y, w, h, text):
    """Draws a rounded button shape for the design stage."""
    tag = f"button_{text}"


    rounded_rect(
        canvas,
        x,
        y,
        x + w,
        y + h,
        18,
        fill=BUTTON_BG,
        outline=BLACK,
        width=2,
        tags=tag
    )


    canvas.create_text(
        x + w / 2,
        y + h / 2,
        text=text,
        fill=WHITE,
        font=("Arial", 10, "bold"),
        tags=tag
    )


    canvas.tag_bind(tag, "<Enter>", lambda event: canvas.config(cursor="hand2"))
    canvas.tag_bind(tag, "<Leave>", lambda event: canvas.config(cursor=""))


# HOME PAGE - TRIAL 3
# Adds the three horizontal calculator buttons.


canvas = make_canvas()


rounded_rect(canvas, 35, 140, 865, 410, 20, fill=CARD_BG)


canvas.create_text(WIDTH / 2, 210, text="The Ultimate Financial Toolkit",
                   fill=YELLOW, font=("Arial Black", 31), anchor="center")


canvas.create_text(WIDTH / 2, 270, text="Simple financial tools for students",
                   fill=WHITE, font=("Arial", 20, "bold"), anchor="center")


canvas.create_text(WIDTH / 2, 305, text="Choose your calculator",
                   fill=WHITE, font=("Arial", 18, "bold"), anchor="center")


canvas_button(canvas, 85, 340, 230, 42, "Income Calculator")
canvas_button(canvas, 335, 340, 230, 42, "Savings Calculator")
canvas_button(canvas, 585, 340, 230, 42, "Loans Calculator")


root.mainloop()
