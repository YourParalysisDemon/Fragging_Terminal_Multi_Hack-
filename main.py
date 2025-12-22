import os
import sys
import time
import pymem.exception
import colorama
import keyboard
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from ReadWriteMemory import ReadWriteMemory
from time import sleep
from time import *
from colorama import Fore, Back, Style

colorama.init()
game_list = [Fore.RED + Back.BLACK + Style.BRIGHT + "Games Available",
             "● Psychonauts",
             "● Psychonauts 2",
             "● Halo 1",
             "● Bioshock infinite",
             "● The binding of isaac",
             "● Spongebob CosmicShake",
             "● Metro 2033",
             "● Company of Heroes",
             "● Deep Rock Galactic",
             "● Garfield Kart",
             "● L4D2",
             "● Fallout 3"]

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
        module_isaac2 = module_from_name(mem.process_handle, "THREADSTACK0").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Spongebob CosmicShake":
        mem = Pymem("CosmicShake-Win64-Shipping.exe")
        module_sponge = module_from_name(mem.process_handle, "CosmicShake-Win64-Shipping.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Metro 2033":
        mem = Pymem("metro")
        module_sponge = module_from_name(mem.process_handle, "metro.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Fallout 3":
        mem = Pymem("Fallout3")
        module_fallout = module_from_name(mem.process_handle, "Fallout3.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Company of Heroes":
        mem = Pymem("RelicCOH")
        module_coh1 = module_from_name(mem.process_handle, "WW2Mod.dll").lpBaseOfDll
        module_coh2 = module_from_name(mem.process_handle, "RelicCOH.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Deep Rock Galactic":
        mem = Pymem("FSD-Win64-Shipping.exe")
        module_drg = module_from_name(mem.process_handle, "FSD-Win64-Shipping.exe").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "Garfield Kart":
        mem = Pymem("GarfieldKartNoMulti")
        module_garfield = module_from_name(mem.process_handle, "mono.dll").lpBaseOfDll
        print("Game Found!")
        break
    elif game == "L4D2":
        mem = Pymem("left4dead2")
        module_l4d2_client = module_from_name(mem.process_handle, "client.dll").lpBaseOfDll
        module_l4d2_engine = module_from_name(mem.process_handle, "engine.dll").lpBaseOfDll
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
