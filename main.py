from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(TIMER) # Stops timer
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    check_label.config(text='')
    global REPS
    REPS = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global REPS
    REPS += 1
    
    if REPS % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif REPS % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
	    count_sec = f'0{count_sec}'
    # Update the canvas text with the current count
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    # If the count is greater than 0, call the count_down function again after 1000 milliseconds (1 second) with count-1
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ''
        work_sessions = math.floor(REPS/2)
        for i in range(work_sessions):
            marks += '✅'
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text='Timer', font=(FONT_NAME, 70), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2,row=1)

check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=2,row=4)

start_button = Button(text='Start', highlightthickness=0, command=start)
start_button.grid(column=1,row=3)

reset_button = Button(text='Reset', highlightthickness=0, command=reset)
reset_button.grid(column=3,row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file='/Users/macintosh/Downloads/pomodoro-start/tomato.png')
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(103, 112, text='00:00', fill='white', font=('Arial', 35, 'bold'))
canvas.grid(column=2,row=2)



window.mainloop()
