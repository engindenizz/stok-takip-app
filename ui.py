import customtkinter as ctk
import buttons


class StokTakipApp:
    def __init__(self):
        self.screen = ctk.CTk()
        ctk.set_appearance_mode("light")
        self.screen.geometry("1200x800")
        self.screen.title("Stok Takip Programı v1.0")


app = StokTakipApp()

app.screen.mainloop()
