import tkinter as tk
from datetime import timedelta

        master = master
        master.title("Interval Timer")

        # List of colors for intervals
        colors = ["#FF0000", "#00FF00"]

        intro_label = tk.Label(master, text="Welcome to The Interval Timer!", font=('Times', 24))
        intro_label.pack(pady=20)

        # Start and Exit buttons
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        start_button = tk.Button(button_frame, text="Start", command=start_timers)
        start_button.pack(side=tk.LEFT, padx=5)

        exit_button = tk.Button(button_frame, text="Exit", command=master.destroy)
        exit_button.pack(side=tk.LEFT, padx=5)

        global_timer_value = tk.StringVar()
        interval_timer_value = tk.StringVar()

        global_timer_label = tk.Label(master, text="Global Timer:", font=('Times', 24))
        global_timer_label.pack(pady=10)
        global_timer_display = tk.Label(master, textvariable=global_timer_value, font=('Times', 36, 'bold'))
        global_timer_display.pack(pady=10)

        interval_timer_label = tk.Label(master, text="Interval Timer:", font=('Times', 24))
        interval_timer_label.pack(pady=10)
        interval_timer_display = tk.Label(master, textvariable=interval_timer_value, font=('Times', 36, 'bold'))
        interval_timer_display.pack(pady=10)

        message_label = tk.Label(master, text="", font=('Times', 14), fg='red')
        message_label.pack(pady=10)

        # Replace Total Time with Total Intervals
        total_intervals_label = tk.Label(master, text="Total Intervals:", font=('Times', 14))
        total_intervals_label.pack(pady=5)
        total_intervals_entry = tk.Entry(master, font=('Times', 14))
        total_intervals_entry.pack(pady=5)

        interval_time_label = tk.Label(master, text="Interval Times (seconds, comma separated):", font=('Times', 14))
        interval_time_label.pack(pady=5)
        interval_time_entry = tk.Entry(master, font=('Times', 14))
        interval_time_entry.pack(pady=5)

        confirm_button = tk.Button(master, text="Confirm", command=confirm_times)
        confirm_button.pack(pady=10)

        global_timer = timedelta()
        interval_timer = timedelta()
        is_running = False
        intervals = []
        current_interval_index = 0
        total_intervals = 0
        completed_intervals = 0

    def confirm_times(self):
        try:
            total_intervals = int(total_intervals_entry.get())
            interval_times = interval_time_entry.get().split(',')
            intervals = [int(time.strip()) for time in interval_times]
            interval_timer = timedelta(seconds=intervals[current_interval_index])
            global_timer_value.set(str(global_timer).split(".")[0])
            interval_timer_value.set(str(interval_timer).split(".")[0])
            message_label.config(text="Times set! Press Start to begin.")
        except ValueError:
            message_label.config(text="Please enter valid integers for intervals and times.")

    def start_timers(self):
        if not is_running:
            is_running = True
            intro_label.pack_forget()
            start_button.pack_forget()
            update_timers()

    def update_timers(self):
        if is_running:
            global_timer += timedelta(seconds=1)
            global_timer_value.set(str(global_timer).split(".")[0])

            interval_timer -= timedelta(seconds=1)
            interval_timer_value.set(str(interval_timer).split(".")[0])

            if interval_timer <= timedelta():
                completed_intervals += 1
                if completed_intervals >= total_intervals:
                    is_running = False
                    show_finish_options()
                    return

                current_interval_index = (current_interval_index + 1) % len(intervals)
                interval_timer = timedelta(seconds=intervals[current_interval_index])
                message_label.config(text="*Interval Changed!*")
                change_background_color()
                master.after(1000, clear_message)

            master.after(1000, update_timers)

    def change_background_color(self):
        # Change the background color based on the current interval index
        if current_interval_index == 0:
            color = colors[0]  # Red for the first interval
        else:
            color = colors[1]  # Green for subsequent intervals

        master.configure(bg=color)
        global_timer_label.configure(bg=color)
        global_timer_display.configure(bg=color)
        interval_timer_label.configure(bg=color)
        interval_timer_display.configure(bg=color)
        message_label.configure(bg=color)

    def clear_message(self):
        message_label.config(text="")

    def show_finish_options(self):
        # Show options to restart or exit after intervals are finished
        message_label.config(text="Intervals Finished! Restart or Exit?")

        restart_button = tk.Button(master, text="Restart", command=restart_program)
        restart_button.pack(pady=10)

        exit_button_finish = tk.Button(master, text="Exit", command=master.destroy)
        exit_button_finish.pack(pady=10)

    def restart_program(self):
        # Reset the program to its initial state
        is_running = False
        global_timer = timedelta()
        interval_timer = timedelta()
        current_interval_index = 0
        completed_intervals = 0
        global_timer_value.set("00:00:00")
        interval_timer_value.set("00:00:00")
        message_label.config(text="")
        restart_button.pack_forget()
        exit_button_finish.pack_forget()
        intro_label.pack(pady=20)
        start_button.pack(pady=10)
        exit_button.pack(pady=10)
        master.configure(bg="SystemButtonFace")  # Reset background color

if __name__ == "__main__":
    root = tk.Tk()
    app = IntervalTimerApp(root)
    root.mainloop()
