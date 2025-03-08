import keyboard
import os
import sys
import tkinter as tk
import pygame
import time
import pymem.exception
import webbrowser
import colorama
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from time import sleep
from time import *
from tkinter import ttk
from colorama import Fore, Back, Style
from offsets import *
from gui import *
from Psychonauts_1 import *
from Psychonauts_2 import *
from Halo_CE import *
from Bioshock_infinite import *

colorama.init()

while True:
    password = input(Fore.RED + Back.BLACK + Style.BRIGHT + "Enter password ")
    if password == "115":
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "Welcome")
        break
    else:
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "Try again retard")

game_list = ["Games Available",
             "● Psychonauts",
             "● Psychonauts 2",
             "● Halo 1",
             "● Bioshock infinite",
             "● The binding of isaac",
             "● Spongebob CosmicShake"]
for game_list in game_list:
    print(game_list)

while True:

    game = input(Fore.RED + Back.BLACK + Style.BRIGHT + "\nEnter game title: ")
    if game == "Psychonauts":
        mem = Pymem("Psychonauts")
        module1 = module_from_name(mem.process_handle, "Psychonauts.exe").lpBaseOfDll
        print("Game Found!")
        break

    elif game == "Psychonauts 2":
        mem = Pymem("Psychonauts2-Win64-Shipping")
        module_pycho2 = module_from_name(mem.process_handle, "Psychonauts2-Win64-Shipping.exe").lpBaseOfDll
        print("Game Found!")
        break

    elif game == "Halo 1":
        mem = Pymem("MCC-Win64-Shipping")
        module_halo = module_from_name(mem.process_handle, "halo1.dll").lpBaseOfDll
        print("Game Found!")
        break

    elif game == "Bioshock infinite":
        mem = Pymem("BioShockInfinite.exe")
        module_bio = module_from_name(mem.process_handle, "BioShockInfinite.exe").lpBaseOfDll
        print("Game Found!")
        break

    elif game == "The binding of isaac":
        mem = Pymem("isaac-ng")
        module_isaac = module_from_name(mem.process_handle, "isaac-ng.exe").lpBaseOfDll
        print("Game Found!")
        break

    elif game == "Spongebob CosmicShake":
        mem = Pymem("CosmicShake-Win64-Shipping.exe")
        module_sponge = module_from_name(mem.process_handle, "CosmicShake-Win64-Shipping.exe").lpBaseOfDll
        print("Game Found!")
        break

    else:
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "How fucking stupid are you???")

print("""
██╗░░██╗░█████╗░██╗░░░██╗███████╗  ███████╗██╗░░░██╗███╗░░██╗
██║░░██║██╔══██╗██║░░░██║██╔════╝  ██╔════╝██║░░░██║████╗░██║
███████║███████║╚██╗░██╔╝█████╗░░  █████╗░░██║░░░██║██╔██╗██║
██╔══██║██╔══██║░╚████╔╝░██╔══╝░░  ██╔══╝░░██║░░░██║██║╚████║
██║░░██║██║░░██║░░╚██╔╝░░███████╗  ██║░░░░░╚██████╔╝██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝""")
