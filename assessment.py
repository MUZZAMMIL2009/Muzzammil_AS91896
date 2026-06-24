# SAVINGS RETURN CALCULATOR - TRIAL 1: LAYOUT AND TEXT
# This first trial creates the visual structure of the Savings page.
# It includes the card, title, labels, divider lines, Help button,
# and result placeholder. Entry boxes and bottom buttons are added later.


import tkinter as tk


# Fixed window size so screenshots stay consistent on school computers.
WIDTH = 900
HEIGHT = 600


# Same colour constants used in the Home and Income pages.
# Keeping them together makes the page consistent and easier to edit.
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




def rounded_rect(canvas, x1, y1, x2, y2, radius, fill, outline=None, width=1, tags=None):
    """Draw a rounded rectangle using a smooth Canvas polygon.


    Normal Tkinter Frames and Buttons are very square. This function
    lets me create the rounded card and rounded buttons from my design.
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


canvas = make_canvas()


# Main calculator card.
rounded_rect(canvas, 25, 50, 875, 550, 18, fill=CARD_BG)


# Page title: same font family/weight as the Income page.
canvas.create_text(
    60,
    115,
    text="Savings Return Calculator",
    fill=WHITE,
    font=("Arial Black", 26),
    anchor="w"
)


# Help button at top right, matching the Income page.
rounded_rect(canvas, 745, 92, 855, 134, 18, fill=BUTTON_BG, outline=BLACK, width=2)
canvas.create_text(800, 113, text="Help", fill=WHITE, font=("Arial", 10, "bold"))


# First input row.
canvas.create_text(65, 195, text="Initial Investment", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")


canvas.create_text(575, 195, text="Interest Rate", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")


canvas.create_line(25, 235, 875, 235, fill=WHITE, width=2)


# Second input row.
canvas.create_text(115, 265, text="Time Period", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")


canvas.create_text(445, 265, text="Compound Frequency", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")


canvas.create_line(25, 305, 875, 305, fill=WHITE, width=2)


# Third input row.
canvas.create_text(95, 335, text="Interest Range", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")


canvas.create_text(455, 335, text="Monthly Contribution", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")


canvas.create_line(25, 375, 875, 375, fill=WHITE, width=2)


# Result placeholder, same wording as the design.
canvas.create_text(60, 415, text="Result: Your Return on investment would be $000", fill=WHITE, font=("Arial", 15, "bold"), anchor="w")


root.mainloop()
