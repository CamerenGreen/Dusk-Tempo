
import tkinter as tk this source is already completed
from datetime import timedelta

class DualStopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome to the FNAF 1 Interval Timer")

        self.intro_label = tk.Label(master, text="Welcome to The FNAF 1 Interval Timer!", font=('Helvetica', 24))
        self.intro_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_timers)
        self.start_button.pack(pady=10)

        self.global_timer_value = tk.StringVar()
        self.interval_timer_value = tk.StringVar()

        self.global_timer_label = tk.Label(master, text="Global Timer:", font=('Helvetica', 24))
        self.global_timer_label.pack(pady=10)
        self.global_timer_display = tk.Label(master, textvariable=self.global_timer_value, font=('Helvetica', 36, 'bold'))
        self.global_timer_display.pack(pady=10)

        self.interval_timer_label = tk.Label(master, text="Interval Timer:", font=('Helvetica', 24))
        self.interval_timer_label.pack(pady=10)
        self.interval_timer_display = tk.Label(master, textvariable=self.interval_timer_value, font=('Helvetica', 36, 'bold'))
        self.interval_timer_display.pack(pady=10)

        self.message_label = tk.Label(master, text="", font=('Helvetica', 14), fg='red')
        self.message_label.pack(pady=10)

        self.global_timer = timedelta()
        self.interval_timer = timedelta(seconds=5)  # Initial interval: 5 seconds
        self.is_running = False

    def start_timers(self):
        if not self.is_running:
            self.is_running = True
            self.intro_label.pack_forget()
            self.start_button.pack_forget()
            self.update_timers()

    def update_timers(self):
        if self.is_running:
            self.global_timer += timedelta(seconds=1)
            self.global_timer_value.set(str(self.global_timer).split(".")[0])  # Display without milliseconds

            self.interval_timer -= timedelta(seconds=1)
            self.interval_timer_value.set(str(self.interval_timer).split(".")[0])  # Display without milliseconds

            if self.interval_timer == timedelta():
                self.reset_interval_timer()
                self.show_move_message()

            self.master.after(1000, self.update_timers)  # Update every 1000 milliseconds (1 second)

    def reset_interval_timer(self):
        if 0 <= self.global_timer.seconds < 535:
            self.interval_timer = timedelta(seconds=5)
        else:
            self.is_running = False

    def show_move_message(self):
        self.message_label.config(text="All animatronics have a movement opprotunity")
        self.master.after(1000, self.clear_message)  # Clear message after 1000 milliseconds (1 second)

    def clear_message(self):
        self.message_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = DualStopwatchApp(root)
    root.mainloop()
