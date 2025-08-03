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
from ReadWriteMemory import ReadWriteMemory
from time import sleep
from time import *
from tkinter import ttk
from colorama import Fore, Back, Style
from offsets import *

colorama.init()
game_list = [Fore.RED + Back.BLACK + Style.BRIGHT + "Games Available",
             "● Psychonauts",
             "● Psychonauts 2",
             "● Halo 1",
             "● Bioshock infinite",
             "● The binding of isaac",
             "● Spongebob CosmicShake",
             "● Metro 2033",
             "● Company of Heroes"]

for game_list in game_list:
    print(game_list)

while True:
    game = input(Fore.RED + Back.BLACK + Style.BRIGHT + "\nEnter game title: ")
    if game == "Psychonauts".casefold():
        mem = Pymem("Psychonauts")
        module1 = module_from_name(mem.process_handle, "Psychonauts.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Psychonauts 2".casefold():
        mem = Pymem("Psychonauts2-Win64-Shipping")
        module_pycho2 = module_from_name(mem.process_handle, "Psychonauts2-Win64-Shipping.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Halo 1".casefold():
        mem = Pymem("MCC-Win64-Shipping")
        module_halo = module_from_name(mem.process_handle, "halo1.dll").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Bioshock infinite".casefold():
        mem = Pymem("BioShockInfinite.exe")
        module_bio = module_from_name(mem.process_handle, "BioShockInfinite.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "The binding of isaac".casefold():
        mem = Pymem("isaac-ng")
        module_isaac = module_from_name(mem.process_handle, "isaac-ng.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "TF2".casefold():  # Do not attach to a VAC secured server retard. Only run this code in -insecure mode.
        mem = Pymem("tf_win64")
        module_tf2 = module_from_name(mem.process_handle, "engine.dll").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Spongebob CosmicShake".casefold():
        mem = Pymem("CosmicShake-Win64-Shipping.exe")
        module_sponge = module_from_name(mem.process_handle, "CosmicShake-Win64-Shipping.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Metro 2033".casefold():
        mem = Pymem("metro")
        module_sponge = module_from_name(mem.process_handle, "metro.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Fallout 3".casefold():
        mem = Pymem("Fallout3")
        module_fallout = module_from_name(mem.process_handle, "Fallout3.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Company of Heroes".casefold():
        mem = Pymem("RelicCOH")
        module = module_from_name(mem.process_handle, "WW2Mod.dll").lpBaseOfDll
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


def readpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer + offset)
        else:
            return remote_pointer.value + offset


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset
