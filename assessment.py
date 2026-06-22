# INCOME TAX CALCULATOR - TRIAL 3: LOGIC AND FUNCTIONALITY
# ============================================================
# This file adds the working income calculation. It uses hourly wage,
# hours worked per week, and time period in weeks to calculate gross
# income, progressive tax, ACC levy, and final take-home pay.

# The result updates automatically when the user types, which is why
# the Entry boxes are connected to update_income_result with KeyRelease.

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


# Places a real Entry input box onto the Canvas at exact coordinates.


def make_entry(canvas, x, y, width=120):
    """Create an entry box and place it exactly on the canvas."""
    entry = tk.Entry(
        canvas,
        bg=ENTRY_BG,
        fg=BLACK,
        font=("Arial", 11),
        bd=2,
        relief="sunken"
    )


    canvas.create_window(
        x,
        y,
        window=entry,
        width=width,
        height=24,
        anchor="nw"
    )


    return entry


# INCOME TAX PAGE - TRIAL 3
# Adds progressive tax, ACC levy and automatic result updating.

ACC_LEVY = 0.0175

TAX_BRACKETS = [
    (14000, 0.105),
    (48000, 0.175),
    (70000, 0.30),
    (180000, 0.33),
    (float("inf"), 0.39)
]
# Calculates progressive tax separately from the interface code.

def progressive_tax(amount):
    """Calculate tax by filling each bracket before moving to the next."""
    tax = 0
    previous_limit = 0

    for limit, rate in TAX_BRACKETS:
        taxable_amount = min(amount, limit) - previous_limit

        if taxable_amount > 0:
            tax += taxable_amount * rate

        if amount <= limit:
            break

        previous_limit = limit

    return tax

canvas = make_canvas()


rounded_rect(canvas, 25, 50, 875, 550, 18, fill=CARD_BG)


canvas.create_text(60, 115, text="Income Tax Calculator",
                   fill=WHITE, font=("Arial Black", 26), anchor="w")


rounded_rect(canvas, 745, 92, 855, 134, 18, fill=BUTTON_BG, outline=BLACK, width=2)
canvas.create_text(800, 113, text="Help", fill=WHITE, font=("Arial", 10, "bold"))


canvas.create_text(105, 205, text="Hourly Wage", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
wage_entry = make_entry(canvas, 245, 195)


canvas.create_text(465, 205, text="Hours worked per week", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
hours_entry = make_entry(canvas, 720, 195)


canvas.create_line(25, 245, 875, 245, fill=WHITE, width=2)


canvas.create_text(45, 275, text="Time Period (Weeks)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
weeks_entry = make_entry(canvas, 245, 265)


canvas.create_line(25, 315, 875, 315, fill=WHITE, width=2)


result_text = canvas.create_text(
    60,
    360,
    text="Result: In X weeks, you will take home $000",
    fill=WHITE,
    font=("Arial", 15, "bold"),
    anchor="w"
)




# Updates the result whenever the user types into one of the input boxes.




def update_income_result(event=None):
    try:
        wage = float(wage_entry.get())
        hours = float(hours_entry.get())
        weeks = float(weeks_entry.get())


        if wage < 0 or hours < 0 or weeks < 0:
            raise ValueError


        gross_income = wage * hours * weeks
        tax = progressive_tax(gross_income)
        acc = gross_income * ACC_LEVY
        take_home = gross_income - tax - acc


        if weeks.is_integer():
            weeks_display = str(int(weeks))
        else:
            weeks_display = f"{weeks:g}"


        canvas.itemconfig(
            result_text,
            text=f"Result: In {weeks_display} weeks, you will take home ${take_home:.2f}"
        )


    except ValueError:
        canvas.itemconfig(result_text, text="Result: Please enter valid numbers")




wage_entry.bind("<KeyRelease>", update_income_result)
hours_entry.bind("<KeyRelease>", update_income_result)
weeks_entry.bind("<KeyRelease>", update_income_result)


canvas_button(canvas, 70, 485, 230, 45, "Home")
canvas_button(canvas, 340, 485, 230, 45, "Savings Calculator")
canvas_button(canvas, 610, 485, 230, 45, "Loans Calculator")


root.mainloop()
