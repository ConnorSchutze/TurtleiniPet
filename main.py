import random
import tkinter as tk
import pyautogui

x = 1400
cycle = 0
check = 1
idle_num = [1, 2, 3 , 4]
sleep_num = [10, 11, 12, 13, 15]
move_left = [6, 7]
move_right = [8, 9]
event_number = random.randrange(1, 3, 1)
# impath = "C:\\your\\path\\to\\file"

def gif_working(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) -1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num+1, 1)
    
    return cycle, event_number

def update(cycle, check, event_number, x):
    if check == 0:
        pass
        # frame = idle[cycle]

window = tk.Tk()

# idle = [tk.PhotoImage]
# idle_to_sleep
# sleep
# sleep_to_idle
# walk_left
# walk_right

window.config(highlightbackground="black")
window.overrideredirect(True)
window.wm_attributes("-transparentcolor", "black")

label = tk.Label(window, bd=0, bg="black")
label.pack()

window.mainloop()

