from Pycho1 import *

# GUI
pygame.init()
pygame.mixer_music.load("music/mod.mp3")
pygame.mixer_music.play(1)

root = tk.Tk()
photo = tk.PhotoImage(file="back/155.png")
root.wm_iconphoto(False, photo)
root.attributes("-topmost", True)
root.title("Fragging Terminal")
root.geometry("340x450")


def callback(url):
    webbrowser.open_new(url)


def show():
    root.deiconify()


def hide():
    root.withdraw()


# Create a style object
style = ttk.Style()
style.theme_use("classic")
style.configure("TNotebook.Tab", background="black", foreground="red")
style.map("TNotebook.Tab",
          background=[("pressed", "black"), ("disabled", "red")],
          foreground=[("pressed", "red"), ("disabled", "white")])

# notebook (tab control)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# frames for each
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab6 = ttk.Frame(notebook)
tab7 = ttk.Frame(notebook)

# tabs to the notebook
notebook.add(tab1, text='Psychonauts 1')
notebook.add(tab2, text='Psychonauts 2')
notebook.add(tab3, text='Dev/Info')
notebook.add(tab4, text='BioShock Infinite')
notebook.add(tab5, text='Halo 1 new')
notebook.add(tab6, text='Halo 1 old')
notebook.add(tab7, text='The Binding of Isaac')

# first tab pycho 1
button1_tab1 = tk.Button(tab1, text="Health", bg='black', fg='white', cursor="cross", command=multi_run_god)
button1_tab1.pack(pady=10)

button2_tab1 = tk.Button(tab1, text="Fuck walking", bg='black', fg='white', cursor="cross", command=multi_run_move)
button2_tab1.pack(pady=10)

button3_tab1 = tk.Button(tab1, text="Run", bg='black', fg='white', cursor="cross",
                         command=multi_run_move2)
button3_tab1.pack(pady=10)

button4_tab1 = tk.Button(tab1, text="Fuck gravity", bg='black', fg='white', cursor="cross",
                         command=multi_run_gravity)
button4_tab1.pack(pady=10)

button5_tab1 = tk.Button(tab1, text="Legendary Mode", bg='black', fg='white', cursor="cross",
                         command=multi_run_legendary)
button5_tab1.pack(pady=10)

button6_tab1 = tk.Button(tab1, text="Exit", bg='black', fg='white', cursor="cross", command=root.destroy)
button6_tab1.pack(pady=10)

# second tab pycho 2
button1_tab2 = tk.Button(tab2, text="Health", bg='black', fg='white', cursor="cross", command=multi_run_god2)
button1_tab2.pack(pady=10)

button2_tab2 = tk.Button(tab2, text="Meth", bg='black', fg='white', cursor="cross", command=multi_run_meth)
button2_tab2.pack(pady=10)

button3_tab2 = tk.Button(tab2, text="Fuck Gravity", bg='black', fg='white', cursor="cross",
                         command=multi_run_fuck_gravity)
button3_tab2.pack(pady=10)

button4_tab2 = tk.Button(tab2, text="Speed up time", bg='black', fg='white', cursor="cross", command=multi_run_fast)
button4_tab2.pack(pady=10)

button5_tab2 = tk.Button(tab2, text="Slow down time", bg='black', fg='white', cursor="cross", command=multi_run_slow)
button5_tab2.pack(pady=10)

button6_tab2 = tk.Button(tab2, text="Flip Gravity", bg='black', fg='white', cursor="cross", command=multi_run_flip)
button6_tab2.pack(pady=10)

button7_tab2 = tk.Button(tab2, text="Exit", bg='black', fg='white', cursor="cross", command=root.destroy)
button7_tab2.pack(pady=10)

# three tab dev/info
label1_tab4 = tk.Label(tab3, text="Hello and thank you for using my software.")
label1_tab4.pack(pady=10)

# tab four bioshock
button1_tab4 = tk.Button(tab4, text="Pistol Ammo", bg='black', fg='white', cursor="cross", command=multi_bio_pistol)
button1_tab4.pack(pady=10)

button2_tab4 = tk.Button(tab4, text="Money", bg='black', fg='white', cursor="cross", command=multi_bio_mon)
button2_tab4.pack(pady=10)

button3_tab4 = tk.Button(tab4, text="Fuck Gravity", bg='black', fg='white', cursor="cross",
                         command=multi_bio_fly)
button3_tab4.pack(pady=10)

# tabs for halo 1

button1_tab5 = tk.Button(tab5, text="Health", bg='black', fg='white', cursor="cross", command=multi_run_new_health)
button1_tab5.pack(pady=10)

button2_tab5 = tk.Button(tab5, text="UNSC Fire rate", bg='black', fg='white', cursor="cross", command=multi_run_117)
button2_tab5.pack(pady=10)

button3_tab5 = tk.Button(tab5, text="Covenant Fire rate", bg='black', fg='white', cursor="cross",
                         command=multi_run_plasma)
button3_tab5.pack(pady=10)

button4_tab5 = tk.Button(tab5, text="Bullet Pierce", bg='black', fg='white', cursor="cross",
                         command=multi_run_wall_pierce)
button4_tab5.pack(pady=10)

button5_tab5 = tk.Button(tab5, text="No Spread", bg='black', fg='white', cursor="cross", command=multi_run_nospread)
button5_tab5.pack(pady=10)

button6_tab5 = tk.Button(tab5, text="Shotgun", bg='black', fg='white', cursor="cross", command=multi_run_shotgun)
button6_tab5.pack(pady=10)

button7_tab5 = tk.Button(tab5, text="Throw Hands", bg='black', fg='white', cursor="cross", command=multi_run_hands)
button7_tab5.pack(pady=10)

button8_tab5 = tk.Button(tab5, text="No Clip", bg='black', fg='white', cursor="cross", command=multi_run_clip)
button8_tab5.pack(pady=10)

button9_tab5 = tk.Button(tab5, text="Speed", bg='black', fg='white', cursor="cross", command=multi_run_speed)
button9_tab5.pack(pady=10)

button10_tab5 = tk.Button(tab5, text="Plasma Pistol", bg='black', fg='white', cursor="cross",
                          command=multi_run_plasma_pistol)
button10_tab5.pack(pady=10)

# second tab
button1_tab6 = tk.Button(tab6, text="Health", bg='black', fg='white', cursor="cross", command=multi_run_old_health)
button1_tab6.pack(pady=10)

button2_tab6 = tk.Button(tab6, text="UNSC Fire rate", bg='black', fg='white', cursor="cross", command=multi_run_0ld_117)
button2_tab6.pack(pady=10)

button3_tab6 = tk.Button(tab6, text="Speed", bg='black', fg='white', cursor="cross", command=multi_run_speed)
button3_tab6.pack(pady=10)

button4_tab6 = tk.Button(tab6, text="Confuse NPC", bg='black', fg='white', cursor="cross", command=multi_run_haha)
button4_tab6.pack(pady=10)

button5_tab6 = tk.Button(tab6, text="Pause", bg='black', fg='white', cursor="cross", command=multi_run_pause)
button5_tab6.pack(pady=10)

button5_tab6 = tk.Button(tab6, text="Stats", bg='black', fg='white', cursor="cross", command=multi_run_stats)
button5_tab6.pack(pady=10)

# isaac tab
button1_tab7 = tk.Button(tab7, text="Health", bg='black', fg='white', cursor="cross", command=multi_isaac_health)
button1_tab7.pack(pady=10)

button2_tab7 = tk.Button(tab7, text="Bombs", bg='black', fg='white', cursor="cross", command=multi_isaac_bomb)
button2_tab7.pack(pady=10)

button3_tab7 = tk.Button(tab7, text="Fire rate", bg='black', fg='white', cursor="cross", command=multi_isaac_fire)
button3_tab7.pack(pady=10)

# Clock
time_label = tk.Label(tab3, font=("Arial", 10), fg="Black", bg="Red")
time_label.pack(pady=10)

day_label = tk.Label(tab3, font=("Arial", 10), fg="Black", bg="Red")
day_label.pack(pady=10)

date_label = tk.Label(tab3, font=("Arial", 10), fg="Black", bg="Red")
date_label.pack(pady=10)


def clock():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    root.after(1000, clock)


link1 = tab4 = tk.Label(tab3, text="Your Sleep Paralysis Demon", bg="black", fg="red", cursor="cross")
link1.bind("<Button-1>", lambda e: callback("https://steamcommunity.com/profiles/76561198259829950/"))
link1.pack(pady=10)

keyboard.add_hotkey("c", show)
keyboard.add_hotkey("v", hide)
keyboard.add_hotkey("F", multi_run_gravity)
keyboard.add_hotkey("G", multi_run_walls)
keyboard.add_hotkey("1", tele_main_lodge)
keyboard.add_hotkey("k", root.destroy)
keyboard.add_hotkey("l", multi_run_spam)
keyboard.add_hotkey("F", multi_run_fuck_gravity)
keyboard.add_hotkey("F", multi_bio_fly)
keyboard.add_hotkey("Z", multi_run_flip)
keyboard.add_hotkey("-", multi_run_slow)
keyboard.add_hotkey("+", multi_run_fast)
keyboard.add_hotkey("9", multi_run_stop)
clock()
root.mainloop()
