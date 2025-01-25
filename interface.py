from customtkinter import *
import time


class MainApp(CTk):
    def __init__(self):
        super().__init__()

        self.title("Meu App")
        self.geometry("200x50")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.timer_label = CTkLabel(self, font=("Arial", 20), text="00:00:00")
        self.timer_label.grid(row=0, column=0, padx=10, pady=10)

        self.update_timer()

    def update_timer(self):
        current_time = time.localtime()
        formatted_time = time.strftime("%H:%M:%S", current_time)

        self.timer_label.configure(text=formatted_time)

        self.after(1000, self.update_timer)


app = MainApp()

app.mainloop()
