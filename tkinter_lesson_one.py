import tkinter as tk
import time

count = 0
cps = 0
started = False

def bf_on_click(stringvar, window):
    if started:
        global count
        count += 1

        press_time = time.time()
        stringvar.set(f"Clicks: {str(count)}")
        
        while True:
            if (press_time - time.time() > 3):
                print("3 seconds passed")
            window.update()
            #window.update_idletasks()

def bf_start_timer(stringvar):
    start_time = time.time()
    while (time.time() - start_time <= 4.99):
        stringvar.set(f"Starting in: {round(5 - (time.time() - start_time), 1)}")
        window.update()
    global started
    started = True


# TKINTER WINDOW VARS
window = tk.Tk("My Window", None, "Tk", True, False, None)
window.geometry("500x300")
window.title("CPS Measurement")

str_count = tk.StringVar(window, "Clicks: 0", "count")
str_cps = tk.StringVar(window, "CPS: Not yet tested", "cps")
str_start_time = tk.StringVar(window, "Press to start the timer.", "start_time")

l_click = tk.Label(window, compound=tk.BOTTOM, textvariable=str_count).pack(side=tk.TOP)
l_cps = tk.Label(window, compound=tk.BOTTOM, textvariable=str_cps).pack()
l_start = tk.Label(window, compound=tk.BOTTOM, textvariable=str_start_time).pack(side=tk.TOP)

b_start = tk.Button(window, text="Start", width=15, height=3,
                    command=lambda: bf_start_timer(str_start_time)).pack()

b_click = tk.Button(window, text="Press to increase count", width=20, height=5,
                   command=lambda : bf_on_click(str_count, window)).pack(side=tk.BOTTOM)

tk.mainloop()