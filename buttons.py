import customtkinter as ctk


class CreateButton:
    def __init__(self, master):
        self.master = master
        self.button = {}

    def add_button(self, name, text, x, y, command):
        button = ctk.CTkButton(
            self.master,
            text=text,
            command=command,
            corner_radius=60,
            fg_color="transparent",
            border_width=1,
            text_color="black",
            hover_color="white",
            border_color="white",
            width=100,
            height=40,
            font=("Arial", 14, "bold"),
        )
        button.place(x=x, y=y)

        self.button[name] = button

        if name == "save_button":
            self.button["save_button"].configure(
                hover_color="blue", border_color="blue"
            )

    def get_button(self, name):
        return self.button.get(name)

    def delete_button(self, name):
        if name in self.button:
            self.button[name].destroy()
            del self.button[name]


# screen = ctk.CTk()
# ctk.set_appearance_mode("dark")
# screen.geometry("400x300")


# btn = CreateButton(screen)
# btn.add_button("save_button", "Click Me", 100, 0, lambda: print("Button Clicked!"))
# btn.add_button("button2", "Click Me", 100, 60, lambda: print("Button Clicked!"))
# btn.add_button("button3", "Click Me", 100, 120, lambda: print("Button Clicked!"))
# btn.add_button("button4", "Click Me", 100, 180, lambda: print("Button Clicked!"))


# screen.mainloop()
