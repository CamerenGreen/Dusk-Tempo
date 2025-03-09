import tkinter as tk
from datetime import timedelta

class IntervalTimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Interval Timer")

        # List of colors for intervals
        self.colors = ["#FF0000", "#00FF00"]

        self.intro_label = tk.Label(master, text="Welcome to The Interval Timer!", font=('Times', 24))
        self.intro_label.pack(pady=20)

        # Start and Exit buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_timers)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.master.destroy)
        self.exit_button.pack(side=tk.LEFT, padx=5)

        self.global_timer_value = tk.StringVar()
        self.interval_timer_value = tk.StringVar()

        self.global_timer_label = tk.Label(master, text="Global Timer:", font=('Times', 24))
        self.global_timer_label.pack(pady=10)
        self.global_timer_display = tk.Label(master, textvariable=self.global_timer_value, font=('Times', 36, 'bold'))
        self.global_timer_display.pack(pady=10)

        self.interval_timer_label = tk.Label(master, text="Interval Timer:", font=('Times', 24))
        self.interval_timer_label.pack(pady=10)
        self.interval_timer_display = tk.Label(master, textvariable=self.interval_timer_value, font=('Times', 36, 'bold'))
        self.interval_timer_display.pack(pady=10)

        self.message_label = tk.Label(master, text="", font=('Times', 14), fg='red')
        self.message_label.pack(pady=10)

        # Replace Total Time with Total Intervals
        self.total_intervals_label = tk.Label(master, text="Total Intervals:", font=('Times', 14))
        self.total_intervals_label.pack(pady=5)
        self.total_intervals_entry = tk.Entry(master, font=('Times', 14))
        self.total_intervals_entry.pack(pady=5)

        self.interval_time_label = tk.Label(master, text="Interval Times (seconds, comma separated):", font=('Times', 14))
        self.interval_time_label.pack(pady=5)
        self.interval_time_entry = tk.Entry(master, font=('Times', 14))
        self.interval_time_entry.pack(pady=5)

        self.confirm_button = tk.Button(master, text="Confirm", command=self.confirm_times)
        self.confirm_button.pack(pady=10)

        self.global_timer = timedelta()
        self.interval_timer = timedelta()
        self.is_running = False
        self.intervals = []
        self.current_interval_index = 0
        self.total_intervals = 0
        self.completed_intervals = 0

    def confirm_times(self):
        try:
            self.total_intervals = int(self.total_intervals_entry.get())
            interval_times = self.interval_time_entry.get().split(',')
            self.intervals = [int(time.strip()) for time in interval_times]
            self.interval_timer = timedelta(seconds=self.intervals[self.current_interval_index])
            self.global_timer_value.set(str(self.global_timer).split(".")[0])
            self.interval_timer_value.set(str(self.interval_timer).split(".")[0])
            self.message_label.config(text="Times set! Press Start to begin.")
        except ValueError:
            self.message_label.config(text="Please enter valid integers for intervals and times.")

    def start_timers(self):
        if not self.is_running:
            self.is_running = True
            self.intro_label.pack_forget()
            self.start_button.pack_forget()
            self.update_timers()

    def update_timers(self):
        if self.is_running:
            self.global_timer += timedelta(seconds=1)
            self.global_timer_value.set(str(self.global_timer).split(".")[0])

            self.interval_timer -= timedelta(seconds=1)
            self.interval_timer_value.set(str(self.interval_timer).split(".")[0])

            if self.interval_timer <= timedelta():
                self.completed_intervals += 1
                if self.completed_intervals >= self.total_intervals:
                    self.is_running = False
                    self.show_finish_options()
                    return

                self.current_interval_index = (self.current_interval_index + 1) % len(self.intervals)
                self.interval_timer = timedelta(seconds=self.intervals[self.current_interval_index])
                self.message_label.config(text="*Interval Changed!*")
                self.change_background_color()
                self.master.after(1000, self.clear_message)

            self.master.after(1000, self.update_timers)

    def change_background_color(self):
        # Change the background color based on the current interval index
        if self.current_interval_index == 0:
            color = self.colors[0]  # Red for the first interval
        else:
            color = self.colors[1]  # Green for subsequent intervals

        self.master.configure(bg=color)
        self.global_timer_label.configure(bg=color)
        self.global_timer_display.configure(bg=color)
        self.interval_timer_label.configure(bg=color)
        self.interval_timer_display.configure(bg=color)
        self.message_label.configure(bg=color)

    def clear_message(self):
        self.message_label.config(text="")

    def show_finish_options(self):
        # Show options to restart or exit after intervals are finished
        self.message_label.config(text="Intervals Finished! Restart or Exit?")

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_program)
        self.restart_button.pack(pady=10)

        self.exit_button_finish = tk.Button(self.master, text="Exit", command=self.master.destroy)
        self.exit_button_finish.pack(pady=10)

    def restart_program(self):
        # Reset the program to its initial state
        self.is_running = False
        self.global_timer = timedelta()
        self.interval_timer = timedelta()
        self.current_interval_index = 0
        self.completed_intervals = 0
        self.global_timer_value.set("00:00:00")
        self.interval_timer_value.set("00:00:00")
        self.message_label.config(text="")
        self.restart_button.pack_forget()
        self.exit_button_finish.pack_forget()
        self.intro_label.pack(pady=20)
        self.start_button.pack(pady=10)
        self.exit_button.pack(pady=10)
        self.master.configure(bg="SystemButtonFace")  # Reset background color

if __name__ == "__main__":
    root = tk.Tk()
    app = IntervalTimerApp(root)
    root.mainloop()
