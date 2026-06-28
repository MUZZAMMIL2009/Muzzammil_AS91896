# LOAN REPAYMENT CALCULATOR - TRIAL 3: LOGIC AND FUNCTIONALITY
# ============================================================
# This final trial adds the working loan repayment calculation.
# It uses amount borrowed, interest rate, time period, and repayment
# frequency to calculate the payment required each repayment period.
#
# The result updates automatically when the user types, which is why
# the Entry boxes are connected to update_loan_result with KeyRelease.
# ============================================================


import tkinter as tk


# Fixed window size so screenshots stay consistent on school computers.
WIDTH = 900
HEIGHT = 600


# Same colour constants used across the Financial Toolkit.
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
    """Draw a rounded rectangle using a smooth Canvas polygon."""
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


def canvas_button(canvas, x, y, w, h, text):
    """Draw one reusable rounded navigation button."""
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


def make_entry(canvas, x, y, width=120):
    """Create a grey Entry box and place it exactly on the Canvas."""
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


def repayment_label(frequency):
    """Return a simple word for common repayment frequencies."""
    if frequency == 52:
        return "week"
    elif frequency == 26:
        return "fortnight"
    elif frequency == 12:
        return "month"
    elif frequency == 4:
        return "quarter"
    elif frequency == 2:
        return "six months"
    elif frequency == 1:
        return "year"
    else:
        return "repayment period"




def calculate_payment(principal, annual_rate, years, repayments_per_year):
    """Calculate the repayment each period using the standard loan formula."""
    total_payments = years * repayments_per_year


    if total_payments <= 0:
        raise ValueError


    if annual_rate == 0:
        return principal / total_payments


    periodic_rate = (annual_rate / 100) / repayments_per_year


    payment = (
        principal
        * periodic_rate
        * (1 + periodic_rate) ** total_payments
        / ((1 + periodic_rate) ** total_payments - 1)
    )


    return payment






canvas = make_canvas()


rounded_rect(canvas, 25, 50, 875, 550, 18, fill=CARD_BG)


canvas.create_text(
    60,
    115,
    text="Loan Repayment Calculator",
    fill=WHITE,
    font=("Arial Black", 26, "bold"),
    anchor="w"
)


rounded_rect(canvas, 745, 92, 855, 134, 18, fill=BUTTON_BG, outline=BLACK, width=2)
canvas.create_text(800, 113, text="Help", fill=WHITE, font=("Arial", 10, "bold"))


canvas.create_text(65, 205, text="Amount Borrowed", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
amount_entry = make_entry(canvas, 250, 195)


canvas.create_text(575, 205, text="Interest Rate", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
rate_entry = make_entry(canvas, 720, 195)


canvas.create_line(25, 245, 875, 245, fill=WHITE, width=2)


canvas.create_text(115, 275, text="Time Period", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
time_entry = make_entry(canvas, 250, 265)


canvas.create_text(480, 275, text="Repayment Frequency", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
frequency_entry = make_entry(canvas, 720, 265)


canvas.create_line(25, 315, 875, 315, fill=WHITE, width=2)


result_text = canvas.create_text(60, 360, text="Result: You pay back $000 every X time period", fill=WHITE, font=("Arial", 15, "bold"), anchor="w")


def update_loan_result(event=None):
    """Read the Entry boxes, calculate repayment amount, and update the result."""
    try:
        amount = float(amount_entry.get())
        rate = float(rate_entry.get())
        years = float(time_entry.get())
        frequency = float(frequency_entry.get())


        if amount <= 0 or rate < 0 or years <= 0 or frequency <= 0:
            raise ValueError


        payment = calculate_payment(amount, rate, years, frequency)
        frequency_display = repayment_label(frequency)


        canvas.itemconfig(
            result_text,
            text=f"Result: You pay back ${payment:.2f} every {frequency_display}"
        )


    except ValueError:
        canvas.itemconfig(result_text, text="Result: Please enter valid numbers")




amount_entry.bind("<KeyRelease>", update_loan_result)
rate_entry.bind("<KeyRelease>", update_loan_result)
time_entry.bind("<KeyRelease>", update_loan_result)
frequency_entry.bind("<KeyRelease>", update_loan_result)


canvas_button(canvas, 70, 485, 230, 45, "Home")
canvas_button(canvas, 340, 485, 230, 45, "Income Calculator")
canvas_button(canvas, 610, 485, 230, 45, "Savings Calculator")


root.mainloop()
