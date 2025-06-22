import keyboard
import psutil
import os
from tqdm import tqdm
from Pycho1 import *
from Psychonauts_1 import *
from Psychonauts_2 import *
from halo import *
from Metro import *
from Bioshock_infinite import *


def restart_program(self):
    os.startfile("Pycho1.exe")
    self.destroy()


pygame.init()
pygame.mixer_music.load("music/mod.mp3")
pygame.mixer_music.play(1)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fragging Terminal")
        photo = tk.PhotoImage(file="back/155.png")
        self.wm_iconphoto(False, photo)
        self.attributes("-topmost", True)
        self.geometry("340x550")

        self.options = ["Halo CE New", "Halo CE Old", "Psychonauts", "Psychonauts 2", "Bioshock infinite",
                        "The binding of isaac", "Spongebob CosmicShake", "Metro 2033", "DEV Page",
                        "Company of Heroes"]
        self.current_frame = None

        self.selected_option = tk.StringVar(value=self.options[0])
        dropdown = ttk.OptionMenu(self, self.selected_option, self.options[0], *self.options, command=self.switch_frame)
        dropdown.pack(pady=5)

        self.switch_frame(self.options[0])

    def restart_program(self):
        os.startfile("Pycho1.exe")
        self.destroy()

    def show(self):
        self.deiconify()

    def hide(self):
        self.withdraw()

    keyboard.add_hotkey("-", show)
    keyboard.add_hotkey("+", hide)
    keyboard.add_hotkey("k", restart_program)

    def switch_frame(self, selected_option):
        if self.current_frame is not None:
            self.current_frame.destroy()

        if selected_option == "Halo CE New":
            self.current_frame = Frame1(self)
        elif selected_option == "Halo CE Old":
            self.current_frame = Frame2(self)
        elif selected_option == "Psychonauts":
            self.current_frame = Frame3(self)
        elif selected_option == "Psychonauts 2":
            self.current_frame = Frame4(self)
        elif selected_option == "Bioshock infinite":
            self.current_frame = Frame5(self)
        elif selected_option == "The binding of isaac":
            self.current_frame = Frame6(self)
        elif selected_option == "Spongebob CosmicShake":
            self.current_frame = Frame7(self)
        elif selected_option == "Metro 2033":
            self.current_frame = Frame8(self)
        elif selected_option == "DEV Page":
            self.current_frame = Frame9(self)
        elif selected_option == "Company of Heroes":
            self.current_frame = Frame10(self)

        self.current_frame.pack(fill="both", expand=True)


class Frame1(tk.Frame):  # Halo new
    def __init__(self, parent):
        super().__init__(parent, background="black")

        button1 = tk.Button(self, text="Health", bg='black', fg='red', cursor="cross",
                            command=multi_run_new_health)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="UNSC Fire rate", bg='black', fg='red', cursor="cross",
                            command=multi_run_117)
        button2.pack(pady=10)

        button3 = tk.Button(self, text="Covenant Fire rate", bg='black', fg='red', cursor="cross",
                            command=multi_run_plasma)
        button3.pack(pady=10)

        button4 = tk.Button(self, text="Bullet Pierce", bg='black', fg='red', cursor="cross",
                            command=multi_run_wall_pierce)
        button4.pack(pady=10)

        button5 = tk.Button(self, text="No Spread", bg='black', fg='red', cursor="cross",
                            command=multi_run_nospread)
        button5.pack(pady=10)

        button6 = tk.Button(self, text="Shotgun", bg='black', fg='red', cursor="cross", command=multi_run_shotgun)
        button6.pack(pady=10)

        button7 = tk.Button(self, text="Throw Hands", bg='black', fg='red', cursor="cross",
                            command=multi_run_hands)
        button7.pack(pady=10)

        button8 = tk.Button(self, text="No Clip", bg='black', fg='red', cursor="cross", command=multi_run_clip)
        button8.pack(pady=10)

        button9 = tk.Button(self, text="Speed", bg='black', fg='red', cursor="cross", command=multi_run_speed)
        button9.pack(pady=10)

        button10 = tk.Button(self, text="Plasma Pistol", bg='black', fg='red', cursor="cross",
                             command=multi_run_plasma_pistol)
        button10.pack(pady=10)


class Frame2(tk.Frame):
    # Halo old
    def __init__(self, parent):
        super().__init__(parent, background="black")

        button1 = tk.Button(self, text="Health", bg='black', fg='red', cursor="cross",
                            command=multi_run_old_health)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="UNSC Fire rate", bg='black', fg='red', cursor="cross",
                            command=multi_run_0ld_117)
        button2.pack(pady=10)

        button3 = tk.Button(self, text="Speed", bg='black', fg='red', cursor="cross", command=multi_run_speed)
        button3.pack(pady=10)

        button4 = tk.Button(self, text="Confuse NPC", bg='black', fg='red', cursor="cross", command=multi_run_haha)
        button4.pack(pady=10)

        button5 = tk.Button(self, text="Pause", bg='black', fg='red', cursor="cross", command=multi_run_pause)
        button5.pack(pady=10)

        button5 = tk.Button(self, text="Stats", bg='black', fg='red', cursor="cross", command=multi_run_stats)
        button5.pack(pady=10)


class Frame3(tk.Frame):
    # Psychonauts
    def __init__(self, parent):
        super().__init__(parent, background="black")

        button1 = tk.Button(self, text="Health", bg='black', fg='red', cursor="cross", command=multi_run_god)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Fuck walking", bg='black', fg='red', cursor="cross",
                            command=multi_run_move)
        button2.pack(pady=10)

        button3 = tk.Button(self, text="Run", bg='black', fg='red', cursor="cross",
                            command=multi_run_move2)
        button3.pack(pady=10)

        button4 = tk.Button(self, text="Fuck gravity", bg='black', fg='red', cursor="cross",
                            command=multi_run_gravity)
        button4.pack(pady=10)

        button5 = tk.Button(self, text="Legendary Mode", bg='black', fg='red', cursor="cross",
                            command=multi_run_legendary)
        button5.pack(pady=10)

        button6 = tk.Button(self, text="Big Raz", bg='black', fg='red', cursor="cross",
                            command=multi_run_big)
        button6.pack(pady=10)

        button7 = tk.Button(self, text="Small Raz", bg='black', fg='red', cursor="cross",
                            command=multi_run_small)
        button7.pack(pady=10)

        button8 = tk.Button(self, text="Stats", bg='black', fg='red', cursor="cross",
                            command=multi_run_raz_stats)
        button8.pack(pady=10)

        button9 = tk.Button(self, text="Flip Gravity", bg='black', fg='red', cursor="cross",
                            command=multi_run_raz_flip)

        button9.pack(pady=10)

        button10 = tk.Button(self, text="Restart exe", bg='black', fg='red', cursor="cross",
                             command=restart_program)

        button10.pack(pady=10)


class Frame4(tk.Frame):
    def __init__(self, parent):  # Psychonauts 2
        super().__init__(parent, background="black")

        button1 = tk.Button(self, text="Health", bg='black', fg='red', cursor="cross", command=multi_run_god2)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Meth", bg='black', fg='red', cursor="cross", command=multi_run_meth)
        button2.pack(pady=10)

        button3 = tk.Button(self, text="Fuck Gravity", bg='black', fg='red', cursor="cross",
                            command=multi_run_fuck_gravity)
        button3.pack(pady=10)

        button4 = tk.Button(self, text="Speed up time", bg='black', fg='red', cursor="cross",
                            command=multi_run_fast)
        button4.pack(pady=10)

        button5 = tk.Button(self, text="Slow down time", bg='black', fg='red', cursor="cross",
                            command=multi_run_slow)
        button5.pack(pady=10)

        button6 = tk.Button(self, text="Flip Gravity", bg='black', fg='red', cursor="cross",
                            command=multi_run_flip)
        button6.pack(pady=10)

        button7 = tk.Button(self, text="Restart exe", bg='black', fg='red', cursor="cross",
                            command=restart_program)
        button7.pack(pady=10)


class Frame5(tk.Frame):
    def __init__(self, parent):  # Bioshock infinite
        super().__init__(parent, background="black")

        button1 = tk.Button(self, text="Pistol Ammo", bg='black', fg='red', cursor="cross",
                            command=multi_bio_pistol)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Money", bg='black', fg='red', cursor="cross", command=multi_bio_mon)
        button2.pack(pady=10)

        button3 = tk.Button(self, text="Fuck Gravity", bg='black', fg='red', cursor="cross",
                            command=multi_bio_fly)
        button3.pack(pady=10)


class Frame6(tk.Frame):
    def __init__(self, parent):  # The binding of isaac
        super().__init__(parent, background="black")

        button1 = tk.Button(self, text="Health", bg='black', fg='red', cursor="cross", command=self.destroy)
        button1.pack(pady=10)

        # button2 = tk.Button(tab7, text="Bombs", bg='black', fg='red', cursor="cross", command=multi_isaac_bomb)
        # button2.pack(pady=10)

        # button3 = tk.Button(tab7, text="Fire rate", bg='black', fg='red', cursor="cross", command=multi_isaac_fire)
        # button3.pack(pady=10)


class Frame7(tk.Frame):
    def __init__(self, parent):  # Spongebob CosmicShake
        super().__init__(parent, background="black")

        button1 = tk.Button(self, text="Fly", bg='black', fg='red', cursor="cross", command=self.destroy)  # I forget :(
        button1.pack(pady=10)


class Frame8(tk.Frame):   
    def __init__(self, parent):
        super().__init__(parent, background="black")
        label = tk.Label(self, text="Metro 2033", font=("Arial", 16))
        label.pack(pady=20)

        button1 = tk.Button(self, text="Bullet go brrr", bg='black', fg='red', cursor="cross",
                            command=multi_run_primary)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Cash", bg='black', fg='red', cursor="cross", command=multi_run_money)
        button2.pack(pady=10)

        button3 = tk.Button(self, text="FOV", bg='black', fg='red', cursor="cross", command=multi_run_fov)
        button3.pack(pady=10)

        button4 = tk.Button(self, text="FLY Tower", bg='black', fg='red', cursor="cross", command=multi_run_z)
        button4.pack(pady=10)

        button5 = tk.Button(self, text="FLY Dead city", bg='black', fg='red', cursor="cross",
                            command=multi_run_zd)
        button5.pack(pady=10)

        button6 = tk.Button(self, text="Restart exe", bg='black', fg='red', cursor="cross",
                            command=restart_program)
        button6.pack(pady=10)


class Frame9(tk.Frame):  # DEV
    def __init__(self, parent):
        super().__init__(parent, background="black")

        # Clock
        time_label = tk.Label(self, font=("Arial", 10), fg="Black", bg="Red")
        time_label.pack(pady=10)

        day_label = tk.Label(self, font=("Arial", 10), fg="Black", bg="Red")
        day_label.pack(pady=10)

        date_label = tk.Label(self, font=("Arial", 10), fg="Black", bg="Red")
        date_label.pack(pady=10)

        time_string = strftime("%I:%M:%S %p")
        time_label.config(text=time_string)

        day_string = strftime("%A")
        day_label.config(text=day_string)

        date_string = strftime("%B %d, %Y")
        date_label.config(text=date_string)

        label1 = tk.Label(self, bg="black", fg="red", text="Hello and thank you for using my software.")
        label1.pack(pady=10)

        self.after(1000, Frame9, parent)

        def callback(url):
            webbrowser.open_new(url)

        link1 = tk.Label(self, text="Your Sleep Paralysis Demon", bg="black", fg="red", cursor="cross")
        link1.bind("<Button-1>", lambda e: callback("https://steamcommunity.com/profiles/76561198259829950/"))
        link1.pack(pady=10)


class Frame10(tk.Frame):
    def __init__(self, parent):  # Company of Heroes
        super().__init__(parent, background="black")

        button1 = tk.Button(self, text="Money", bg='black', fg='red', cursor="cross",
                            command=self.destroy)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Gas", bg='black', fg='red', cursor="cross", command=self.destroy)
        button2.pack(pady=10)

        button3 = tk.Button(self, text="Ammo", bg='black', fg='red', cursor="cross", command=self.destroy)
        button3.pack(pady=10)

        button4 = tk.Button(self, text="Population Cap", bg='black', fg='red', cursor="cross",
                            command=self.destroy)
        button4.pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
