# SAVINGS RETURN CALCULATOR - TRIAL 3: LOGIC AND FUNCTIONALITY
#
# This final trial adds the working savings calculation.
# It uses the starting investment, interest rate, time period, compound
# frequency, optional interest range, and optional monthly contribution.
#
# The result updates automatically when the user types, which is why
# the Entry boxes are connected to update_savings_result with KeyRelease.


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


def canvas_button(canvas, x, y, w, h, text):
    """Draw one reusable rounded button.


    I use the same function for every bottom button so their sizing,
    colour, outline, and font stay consistent across the whole page.
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


def make_entry(canvas, x, y, width=120):
    """Create a grey Entry box and place it onto the Canvas.


    Entry boxes are real Tkinter widgets, but create_window() lets
    me position them accurately inside the Canvas design.
    """
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


def calculate_savings(initial, annual_rate, years, compound_frequency, monthly_contribution):
    """Calculate the future savings value.


    The initial investment uses the standard compound interest formula:
    A = P(1 + r/n)^(nt)


    Monthly contributions are added at the end of each month using an
    equivalent monthly growth rate. This keeps the result realistic
    while still allowing the user to choose the compounding frequency.
    """
    r = annual_rate / 100
    n = compound_frequency
    t = years


    # Future value of the starting investment.
    future_initial = initial * (1 + r / n) ** (n * t)


    # Number of monthly contributions across the time period.
    total_months = int(round(t * 12))


    if total_months <= 0:
        return future_initial


    # Convert the selected compounding frequency into an equivalent monthly rate.
    effective_annual_factor = (1 + r / n) ** n
    monthly_rate = effective_annual_factor ** (1 / 12) - 1


    if monthly_rate == 0:
        future_contributions = monthly_contribution * total_months
    else:
        future_contributions = monthly_contribution * (((1 + monthly_rate) ** total_months - 1) / monthly_rate)


    return future_initial + future_contributions






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
initial_entry = make_entry(canvas, 250, 185)


canvas.create_text(575, 195, text="Interest Rate", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
rate_entry = make_entry(canvas, 720, 185)


canvas.create_line(25, 235, 875, 235, fill=WHITE, width=2)


# Second input row.
canvas.create_text(115, 265, text="Time Period", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
time_entry = make_entry(canvas, 250, 255)


canvas.create_text(445, 265, text="Compound Frequency", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
frequency_entry = make_entry(canvas, 720, 255)


canvas.create_line(25, 305, 875, 305, fill=WHITE, width=2)


# Third input row.
canvas.create_text(95, 335, text="Interest Range", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
range_entry = make_entry(canvas, 250, 325)


canvas.create_text(455, 335, text="Monthly Contribution", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
monthly_entry = make_entry(canvas, 720, 325)


canvas.create_line(25, 375, 875, 375, fill=WHITE, width=2)


# Result placeholder, same wording as the design.
result_text = canvas.create_text(60, 415, text="Result: Your Return on investment would be $000", fill=WHITE, font=("Arial", 15, "bold"), anchor="w")


def update_savings_result(event=None):
    """Read the Entry boxes, calculate the savings return, and update the result."""
    try:
        initial = float(initial_entry.get())
        rate = float(rate_entry.get())
        years = float(time_entry.get())
        frequency = float(frequency_entry.get())


        # Interest Range and Monthly Contribution are optional.
        # If the user leaves them blank, the program treats them as zero.
        interest_range_text = range_entry.get().strip()
        monthly_text = monthly_entry.get().strip()


        interest_range = float(interest_range_text) if interest_range_text != "" else 0
        monthly = float(monthly_text) if monthly_text != "" else 0


        # Negative values do not make sense for this calculator.
        # Compound frequency must also be above zero to avoid division errors.
        if initial < 0 or rate < 0 or years < 0 or frequency <= 0 or interest_range < 0 or monthly < 0:
            raise ValueError


        final_amount = calculate_savings(initial, rate, years, frequency, monthly)


        if interest_range > 0:
            # If an interest range is entered, show a low and high estimate as well.
            low_rate = max(rate - interest_range, 0)
            high_rate = rate + interest_range


            low_amount = calculate_savings(initial, low_rate, years, frequency, monthly)
            high_amount = calculate_savings(initial, high_rate, years, frequency, monthly)


            canvas.itemconfig(
                result_text,
                text=f"Result: Your Return on investment would be ${final_amount:.2f} (Range: ${low_amount:.2f} - ${high_amount:.2f})"
            )
        else:
            canvas.itemconfig(
                result_text,
                text=f"Result: Your Return on investment would be ${final_amount:.2f}"
            )


    except ValueError:
        canvas.itemconfig(result_text, text="Result: Please enter valid numbers")




# Update the result whenever the user changes any input box.
initial_entry.bind("<KeyRelease>", update_savings_result)
rate_entry.bind("<KeyRelease>", update_savings_result)
time_entry.bind("<KeyRelease>", update_savings_result)
frequency_entry.bind("<KeyRelease>", update_savings_result)
range_entry.bind("<KeyRelease>", update_savings_result)
monthly_entry.bind("<KeyRelease>", update_savings_result)


# Bottom navigation buttons, positioned the same way as the Income page.
canvas_button(canvas, 70, 485, 230, 45, "Home")
canvas_button(canvas, 340, 485, 230, 45, "Income Calculator")
canvas_button(canvas, 610, 485, 230, 45, "Loans Calculator")


root.mainloop()
