# HELP PAGE - TRIAL 3: ADDING NAVIGATION BUTTONS
# ============================================================
# This trial completes the Help page by adding navigation buttons.
# The buttons match the same style and layout used in the other pages.
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
    """Create the main drawing area for the page."""
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


# Title for the Help page.
canvas.create_text(
    75,
    105,
    text="Help - How to use this calculator",
    fill=WHITE,
    font=("Arial Black", 24, "bold"),
    anchor="w"
)


# The help text is kept in one list so I can edit or add sections later.
# Each section has a heading and paragraph. To add more help text,
# copy one tuple and change the title/text.
HELP_SECTIONS = [
    (
        "Income Tax Calculator",
        "Hourly Wage is how much money you earn for one hour of work. "
        "Hours worked per week is the number of hours you usually work in a week. "
        "Time Period is the number of weeks you want to calculate for. "
        "This calculator matters because students often think about gross pay, "
        "but the amount you actually take home is lower after tax and ACC. "
        "Understanding take-home pay helps with budgeting, saving, transport costs, "
        "phone bills, and planning how much work is actually worth."
    ),
    (
        "Savings Return Calculator",
        "Initial Investment is the amount of money you start with. Interest Rate is "
        "the yearly percentage return. Time Period is how many years the money is saved "
        "or invested for. Compound Frequency means how often interest is added: "
        "1 = yearly, 4 = quarterly, 12 = monthly, 52 = weekly. Monthly Contribution "
        "is extra money added each month. Interest Range lets you test a lower and higher "
        "rate. This matters because compound interest can help build wealth over time, "
        "especially when someone starts young and adds money regularly."
    ),
    (
        "Loan Repayment Calculator",
        "Amount Borrowed is the total loan amount. Interest Rate is the cost of borrowing "
        "money, shown as a yearly percentage. Time Period is how many years the loan will "
        "take to repay. Repayment Frequency means how often payments are made, such as "
        "12 for monthly or 52 for weekly. This calculator matters because loans can help "
        "people buy expensive things, but interest makes the total cost higher. Understanding "
        "repayments helps teenagers avoid debt problems later and make smarter choices."
    )
]


# Scrollable area inside the central card.
# The title and bottom buttons stay still while this middle section scrolls.
scroll_canvas = tk.Canvas(
    root,
    width=740,
    height=300,
    bg=CARD_BG,
    highlightthickness=0
)


scrollbar = tk.Scrollbar(
    root,
    orient="vertical",
    command=scroll_canvas.yview
)


scroll_canvas.configure(yscrollcommand=scrollbar.set)


# Place the scrolling canvas and scrollbar inside the large purple card.
canvas.create_window(75, 150, window=scroll_canvas, anchor="nw")
canvas.create_window(835, 150, window=scrollbar, width=16, height=300, anchor="nw")


# Draw the help sections inside the scrollable canvas.
y = 10


for heading, paragraph in HELP_SECTIONS:
    scroll_canvas.create_text(
        0,
        y,
        text=heading,
        fill=WHITE,
        font=("Arial", 17, "bold"),
        anchor="nw",
        width=720
    )


    y += 35


    scroll_canvas.create_text(
        0,
        y,
        text=paragraph,
        fill=WHITE,
        font=("Arial", 11, "bold"),
        anchor="nw",
        width=720
    )


    y += 125


# Tell Tkinter how far the scrollable area goes.
scroll_canvas.configure(scrollregion=(0, 0, 740, y))


# Allows the mouse wheel to scroll the help text.
def mouse_scroll(event):
    scroll_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


scroll_canvas.bind("<Enter>", lambda event: scroll_canvas.bind_all("<MouseWheel>", mouse_scroll))
scroll_canvas.bind("<Leave>", lambda event: scroll_canvas.unbind_all("<MouseWheel>"))


def canvas_button(canvas, x, y, w, h, text):
    """Draw one rounded navigation button.


    I reused this button function so the Help page buttons match
    the same style as the other pages.
    """
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




# Bottom navigation buttons.
canvas_button(canvas, 70, 485, 230, 45, "Home")
canvas_button(canvas, 340, 485, 230, 45, "Income Calculator")
canvas_button(canvas, 610, 485, 230, 45, "Savings Calculator")




root.mainloop()



