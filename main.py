import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
timer = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer.grid(column=2, row=0)
start_button = tk.Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=3)
reset_button = tk.Button(text="Reset", highlightthickness=0)
reset_button.grid(column=4, row=3)
emoji = tk.Label(text="✓", bg=YELLOW, fg=GREEN,)
emoji.grid(column=2, row=4)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas.create_text(100, 130, text="00-00", fill="white", font=(FONT_NAME, 35))
canvas.grid(column=2, row=1)
window.config(padx=100, pady=50, bg=YELLOW)
window.mainloop()
