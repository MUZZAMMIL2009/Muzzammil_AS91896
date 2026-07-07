import tkinter as tk


# FINANCIAL TOOLKIT - FINAL CONNECTED SYSTEM (POST FEEDBACK)
# This file connects the Home Page, Income Tax Calculator,
# Savings Return Calculator, Loan Repayment Calculator, and Help Page.


# The visual layout is kept the same as the separate trial pages.
# The only major change is that the Canvas buttons now take a command,
# so clicking them opens the correct page.


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


# Income calculator constants.
ACC_LEVY = 0.0175




TAX_BRACKETS = [
   (14000, 0.105),
   (48000, 0.175),
   (70000, 0.30),
   (180000, 0.33),
   (float("inf"), 0.39)
]


# Create the one main Tkinter window for the full connected program.
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


def clear_window():
   """Clear the current page before drawing the next page."""
   for widget in root.winfo_children():
       widget.destroy()




def rounded_rect(canvas, x1, y1, x2, y2, radius, fill, outline=None, width=1, tags=None):
   """Draw a rounded rectangle using a smooth Canvas polygon.


   This keeps the same rounded purple card and button style from the trial pages.
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


def canvas_button(canvas, x, y, w, h, text, command=None):
   """Draw one reusable rounded Canvas button.




   The trial pages used Canvas shapes for buttons. In the final system,
   this function keeps the same visual style but also connects the button
   to a page using command.
   """
   # Use only numbers in the tag so spaces in names like "Income Calculator"
   # do not interfere with Canvas bindings.
   tag = f"nav_button_{x}_{y}_{w}_{h}"


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
       tags=(tag,)
   )


   canvas.create_text(
       x + w / 2,
       y + h / 2,
       text=text,
       fill=WHITE,
       font=("Arial", 10, "bold"),
       tags=(tag,)
   )


   canvas.tag_bind(tag, "<Enter>", lambda event: canvas.config(cursor="hand2"))
   canvas.tag_bind(tag, "<Leave>", lambda event: canvas.config(cursor=""))


   if command is not None:
       canvas.tag_bind(tag, "<Button-1>", lambda event, chosen_command=command: chosen_command())




def make_entry(canvas, x, y, width=120):
   """Create a grey Entry box and place it onto the Canvas.




   This is copied from the individual calculator pages so the Entry boxes
   keep the same position, colour, size, font, and anchor point.
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


def calculate_savings(initial, annual_rate, years, compound_frequency, monthly_contribution):
   """Calculate the future savings value using compound interest."""
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


def calculate_payment(principal, annual_rate, years, repayment_frequency):
   """Calculate the loan repayment amount for each repayment period."""
   repayments_per_year = repayment_frequency
   total_payments = years * repayments_per_year


   if total_payments <= 0:
       raise ValueError


   # If interest is 0%, the loan is split evenly across all repayments.
   if annual_rate == 0:
       return principal / total_payments


   periodic_rate = (annual_rate / 100) / repayments_per_year


   payment = principal * (periodic_rate * (1 + periodic_rate) ** total_payments) / (
       ((1 + periodic_rate) ** total_payments) - 1
   )


   return payment




def repayment_label(frequency):
   """Convert common repayment frequency numbers into words."""
   if frequency == 52:
       return "week"
   if frequency == 26:
       return "fortnight"
   if frequency == 12:
       return "month"
   if frequency == 4:
       return "quarter"
   if frequency == 2:
       return "six months"
   if frequency == 1:
       return "year"
   return "repayment period"




def draw_help_button(canvas):
   """Draw the top-right Help button used on calculator pages."""
   canvas_button(canvas, 745, 92, 110, 42, "Help", show_help_page)




def show_home_page():
   """Display the Home Page."""
   clear_window()
   canvas = make_canvas()


   rounded_rect(canvas, 35, 140, 865, 410, 20, fill=CARD_BG)


   canvas.create_text(WIDTH / 2, 210, text="The Ultimate Financial Toolkit",
                      fill=YELLOW, font=("Arial Black", 31), anchor="center")


   canvas.create_text(WIDTH / 2, 270, text="Simple financial tools for students",
                      fill=WHITE, font=("Arial", 20, "bold"), anchor="center")


   canvas.create_text(WIDTH / 2, 305, text="Choose your calculator",
                      fill=WHITE, font=("Arial", 18, "bold"), anchor="center")


   canvas_button(canvas, 85, 340, 230, 42, "Income Calculator", show_income_page)
   canvas_button(canvas, 335, 340, 230, 42, "Savings Calculator", show_savings_page)
   canvas_button(canvas, 585, 340, 230, 42, "Loans Calculator", show_loan_page)


def show_income_page():
   """Display the Income Tax Calculator page."""
   clear_window()
   canvas = make_canvas()


   rounded_rect(canvas, 25, 50, 875, 550, 18, fill=CARD_BG)


   canvas.create_text(60, 115, text="NZ Income Tax Calculator",
                      fill=WHITE, font=("Arial Black", 26), anchor="w")


   draw_help_button(canvas)


   canvas.create_text(105, 205, text="Hourly Wage", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   wage_entry = make_entry(canvas, 245, 195)


   canvas.create_text(465, 205, text="Hours worked per week", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   hours_entry = make_entry(canvas, 720, 195)


   canvas.create_line(25, 245, 875, 245, fill=WHITE, width=2)




   canvas.create_text(45, 275, text="Time Period(weeks)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
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




   canvas_button(canvas, 70, 485, 230, 45, "Home", show_home_page)
   canvas_button(canvas, 340, 485, 230, 45, "Savings Calculator", show_savings_page)
   canvas_button(canvas, 610, 485, 230, 45, "Loans Calculator", show_loan_page)








def show_savings_page():
   """Display the Savings Return Calculator page."""
   clear_window()
   canvas = make_canvas()




   rounded_rect(canvas, 25, 50, 875, 550, 18, fill=CARD_BG)




   canvas.create_text(
       60,
       115,
       text="Savings Return Calculator",
       fill=WHITE,
       font=("Arial Black", 26),
       anchor="w"
   )




   draw_help_button(canvas)




   canvas.create_text(65, 195, text="Initial Investment", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   initial_entry = make_entry(canvas, 250, 185)




   canvas.create_text(575, 195, text="Interest Rate(%)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   rate_entry = make_entry(canvas, 720, 185)




   canvas.create_line(25, 235, 875, 235, fill=WHITE, width=2)




   canvas.create_text(100, 265, text="Time Period(years)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   time_entry = make_entry(canvas, 250, 255)




   canvas.create_text(445, 265, text="Compound Frequency(n/year)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   frequency_entry = make_entry(canvas, 720, 255)




   canvas.create_line(25, 305, 875, 305, fill=WHITE, width=2)




   canvas.create_text(35, 335, text="Interest Range(%) - optional", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   range_entry = make_entry(canvas, 250, 325)




   canvas.create_text(455, 335, text="Monthly Contribution(optional)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   monthly_entry = make_entry(canvas, 720, 325)




   canvas.create_line(25, 375, 875, 375, fill=WHITE, width=2)




   result_text = canvas.create_text(
       60,
       415,
       text="Result: Your Return on investment would be $000",
       fill=WHITE,
       font=("Arial", 15, "bold"),
       anchor="w"
   )




   def update_savings_result(event=None):
       """Read the Entry boxes, calculate the savings return, and update the result."""
       try:
           initial = float(initial_entry.get())
           rate = float(rate_entry.get())
           years = float(time_entry.get())
           frequency = float(frequency_entry.get())




           # Interest Range and Monthly Contribution are optional.
           interest_range_text = range_entry.get().strip()
           monthly_text = monthly_entry.get().strip()




           interest_range = float(interest_range_text) if interest_range_text != "" else 0
           monthly = float(monthly_text) if monthly_text != "" else 0




           if initial < 0 or rate < 0 or years < 0 or frequency <= 0 or interest_range < 0 or monthly < 0:
               raise ValueError




           final_amount = calculate_savings(initial, rate, years, frequency, monthly)




           if interest_range > 0:
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




   initial_entry.bind("<KeyRelease>", update_savings_result)
   rate_entry.bind("<KeyRelease>", update_savings_result)
   time_entry.bind("<KeyRelease>", update_savings_result)
   frequency_entry.bind("<KeyRelease>", update_savings_result)
   range_entry.bind("<KeyRelease>", update_savings_result)
   monthly_entry.bind("<KeyRelease>", update_savings_result)




   canvas_button(canvas, 70, 485, 230, 45, "Home", show_home_page)
   canvas_button(canvas, 340, 485, 230, 45, "Income Calculator", show_income_page)
   canvas_button(canvas, 610, 485, 230, 45, "Loans Calculator", show_loan_page)


def show_loan_page():
   """Display the Loan Repayment Calculator page."""
   clear_window()
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




   draw_help_button(canvas)




   canvas.create_text(65, 205, text="Amount Borrowed", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   amount_entry = make_entry(canvas, 250, 195)




   canvas.create_text(575, 205, text="Interest Rate(%)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   rate_entry = make_entry(canvas, 720, 195)




   canvas.create_line(25, 245, 875, 245, fill=WHITE, width=2)




   canvas.create_text(100, 275, text="Time Period(years)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   time_entry = make_entry(canvas, 250, 265)




   canvas.create_text(480, 275, text="Repayment Frequency(n/year)", fill=WHITE, font=("Arial", 12, "bold"), anchor="w")
   frequency_entry = make_entry(canvas, 720, 265)




   canvas.create_line(25, 315, 875, 315, fill=WHITE, width=2)




   result_text = canvas.create_text(
       60,
       360,
       text="Result: You pay back $000 every X time period",
       fill=WHITE,
       font=("Arial", 15, "bold"),
       anchor="w"
   )




   def update_loan_result(event=None):
       try:
           amount = float(amount_entry.get())
           rate = float(rate_entry.get())
           years = float(time_entry.get())
           frequency = float(frequency_entry.get())




           if amount <= 0 or rate < 0 or years <= 0 or frequency <= 0:
               raise ValueError




           payment = calculate_payment(amount, rate, years, frequency)
           label = repayment_label(frequency)




           canvas.itemconfig(
               result_text,
               text=f"Result: You pay back ${payment:.2f} every {label}"
           )




       except ValueError:
           canvas.itemconfig(result_text, text="Result: Please enter valid numbers")




   amount_entry.bind("<KeyRelease>", update_loan_result)
   rate_entry.bind("<KeyRelease>", update_loan_result)
   time_entry.bind("<KeyRelease>", update_loan_result)
   frequency_entry.bind("<KeyRelease>", update_loan_result)




   canvas_button(canvas, 70, 485, 230, 45, "Home", show_home_page)
   canvas_button(canvas, 340, 485, 230, 45, "Income Calculator", show_income_page)
   canvas_button(canvas, 610, 485, 230, 45, "Savings Calculator", show_savings_page)




def show_help_page():
   """Display the Help Page."""
   clear_window()
   canvas = make_canvas()


   rounded_rect(canvas, 25, 50, 875, 550, 18, fill=CARD_BG)


   canvas.create_text(
       75,
       105,
       text="Help - How to use this calculator",
       fill=WHITE,
       font=("Arial Black", 24, "bold"),
       anchor="w"
   )


   HELP_SECTIONS = [
       (
           "Income Tax Calculator",
           "Enter numbers only. Do not type $, %, or words. Hourly Wage is how much you earn per hour. Hours Worked per Week is the average number of hours you work each week. Time Period (Weeks) is how many weeks you want to calculate. Fill in all 3 boxes before expecting a result."
       ),
       (
           "Savings Return Calculator",
           "Enter numbers only. Do not type $, %, or words. Initial Investment is the amount you are starting with. Interest Rate is the annual rate of return (eg. enter 8, not 8%). Time Period is entered in years. Compound Frequency is the number of times interest is added each year (1 = yearly, 2 = semiannually, 4 = quarterly, 12 = monthly). Interest Range and Monthly Contribution are optional, so they can be left blank."
       ),
       (
           "Loan Repayment Calculator",
           "Enter numbers only. Do not type $, %, or words. Amount Borrowed is the size of the loan. Interest Rate is the annual rate (eg. enter 8, not 8%). Time Period is entered in years. Repayment Frequency is the number of repayments each year (1 = yearly, 2 = semiannually, 4 = quarterly, 12 = monthly). Complete all of the boxes before calculating."
       )
   ]


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




   canvas.create_window(75, 150, window=scroll_canvas, anchor="nw")
   canvas.create_window(835, 150, window=scrollbar, width=16, height=300, anchor="nw")




   y_position = 10




   for heading, paragraph in HELP_SECTIONS:
       scroll_canvas.create_text(
           0,
           y_position,
           text=heading,
           fill=WHITE,
           font=("Arial", 17, "bold"),
           anchor="nw",
           width=720
       )




       y_position += 35




       scroll_canvas.create_text(
           0,
           y_position,
           text=paragraph,
           fill=WHITE,
           font=("Arial", 11, "bold"),
           anchor="nw",
           width=720
       )




       y_position += 180




   scroll_canvas.configure(scrollregion=(0, 0, 740, y_position))


   def mouse_scroll(event):
       scroll_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


   scroll_canvas.bind("<MouseWheel>", mouse_scroll)


   canvas_button(canvas, 70, 485, 230, 45, "Home", show_home_page)
   canvas_button(canvas, 340, 485, 230, 45, "Income Calculator", show_income_page)
   canvas_button(canvas, 610, 485, 230, 45, "Savings Calculator", show_savings_page)


# Start the program on the Home Page.
show_home_page()
root.mainloop()
