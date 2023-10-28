import tkinter as tk
import main

class AutomateMontavueGoGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Automate MontavueGo")

        self.button = tk.Button(self, text="Run Automation", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        main.run_automation()

if __name__ == "__main__":
    gui = AutomateMontavueGoGUI()
    gui.mainloop()
