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
             "● The binding of isaac"]
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

    else:
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "How fucking stupid are you???")

print("""
██╗░░██╗░█████╗░██╗░░░██╗███████╗  ███████╗██╗░░░██╗███╗░░██╗
██║░░██║██╔══██╗██║░░░██║██╔════╝  ██╔════╝██║░░░██║████╗░██║
███████║███████║╚██╗░██╔╝█████╗░░  █████╗░░██║░░░██║██╔██╗██║
██╔══██║██╔══██║░╚████╔╝░██╔══╝░░  ██╔══╝░░██║░░░██║██║╚████║
██║░░██║██║░░██║░░╚██╔╝░░███████╗  ██║░░░░░╚██████╔╝██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝""")


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


endInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class input_i(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", input_i)]


# Actuals Functions
def presskey(hexkeycode):
    extra = ctypes.c_ulong(0)
    ii_ = input_i()
    ii_.ki = KeyBdInput(0, hexkeycode, 0x0008, 0, ctypes.pointer(extra))
    x = input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def releasekey(hexkeycode):
    extra = ctypes.c_ulong(0)
    ii_ = input_i()
    ii_.ki = KeyBdInput(0, hexkeycode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# Threads for pycho 1


def multi_run_god():
    new_thread = Thread(target=god_hack, daemon=True)
    new_thread.start()


def multi_run_move():
    new_thread = Thread(target=fuck_walking, daemon=True)
    new_thread.start()


def multi_run_move2():
    new_thread = Thread(target=fuck_walking2, daemon=True)
    new_thread.start()


def multi_run_walls():
    new_thread = Thread(target=fuck_walls, daemon=True)
    new_thread.start()


def multi_run_gravity():
    new_thread = Thread(target=fuck_gravity, daemon=True)
    new_thread.start()


def multi_run_legendary():
    new_thread = Thread(target=Legendary_mode, daemon=True)
    new_thread.start()


def multi_run_stats():
    new_thread = Thread(target=stats, daemon=True)
    new_thread.start()


def multi_run_small():
    new_thread = Thread(target=small_raz, daemon=True)
    new_thread.start()


def multi_run_big():
    new_thread = Thread(target=big_raz, daemon=True)
    new_thread.start()


# Threads for pycho 2


def multi_run_god2():
    new_thread = Thread(target=god_hack2, daemon=True)
    new_thread.start()


def multi_run_meth():
    new_thread = Thread(target=meth, daemon=True)
    new_thread.start()


def multi_run_fuck_gravity():
    new_thread = Thread(target=fuck_gravity_pycho2, daemon=True)
    new_thread.start()


def multi_run_spam():
    new_thread = Thread(target=spam, daemon=True)
    new_thread.start()


def multi_run_flip():
    new_thread = Thread(target=flip_gravity, daemon=True)
    new_thread.start()


def multi_run_slow():
    new_thread = Thread(target=clock_decrease, daemon=True)
    new_thread.start()


def multi_run_fast():
    new_thread = Thread(target=clock_increase, daemon=True)
    new_thread.start()


def multi_run_stop():
    new_thread = Thread(target=clock_stop, daemon=True)
    new_thread.start()


# Threads for bioshock inf

def multi_bio_fly():
    new_thread = Thread(target=bio_fly, daemon=True)
    new_thread.start()


def multi_bio_mon():
    new_thread = Thread(target=bio_mon, daemon=True)
    new_thread.start()


def multi_bio_pistol():
    new_thread = Thread(target=bio_pistol, daemon=True)
    new_thread.start()


# Threads for Halo 1
def multi_run_117():
    new_thread = Thread(target=John117, daemon=True)
    new_thread.start()


def multi_run_0ld_117():
    new_thread = Thread(target=oldJohn117, daemon=True)
    new_thread.start()


def multi_run_gravity2():
    new_thread = Thread(target=fuck_gravity2_halo, daemon=True)
    new_thread.start()


def multi_run_clip2():
    new_thread = Thread(target=fuck_walls2, daemon=True)
    new_thread.start()


def multi_run_clip():
    new_thread = Thread(target=fuck_walls, daemon=True)
    new_thread.start()


def multi_run_gravity_halo():
    new_thread = Thread(target=fuck_gravity_halo, daemon=True)
    new_thread.start()


def multi_run_plasma():
    new_thread = Thread(target=plasma, daemon=True)
    new_thread.start()


def multi_run_hands():
    new_thread = Thread(target=hands, daemon=True)
    new_thread.start()


def multi_run_speed():
    new_thread = Thread(target=speed, daemon=True)
    new_thread.start()


def multi_run_nospread():
    new_thread = Thread(target=no_spread, daemon=True)
    new_thread.start()


def multi_run_bullet():
    new_thread = Thread(target=stats, daemon=True)
    new_thread.start()


def multi_run_pause():
    new_thread = Thread(target=pause_game, daemon=True)
    new_thread.start()


def multi_run_haha():
    new_thread = Thread(target=haha_number_go_brrr, daemon=True)
    new_thread.start()


def multi_run_shotgun():
    new_thread = Thread(target=shotgun, daemon=True)
    new_thread.start()


def multi_run_old_health():
    new_thread = Thread(target=old_health, daemon=True)
    new_thread.start()


def multi_run_new_health():
    new_thread = Thread(target=new_health, daemon=True)
    new_thread.start()


def multi_run_wall_pierce():
    new_thread = Thread(target=wall_pierce, daemon=True)
    new_thread.start()


def multi_run_plasma_pistol():
    new_thread = Thread(target=plasma_pistol, daemon=True)
    new_thread.start()


# Isaac threads
def multi_isaac_health():
    new_thread = Thread(target=isaac_health, daemon=True)
    new_thread.start()


def multi_isaac_bomb():
    new_thread = Thread(target=isaac_bombs, daemon=True)
    new_thread.start()


def multi_isaac_fire():
    new_thread = Thread(target=isaac_fire_rate, daemon=True)
    new_thread.start()


# funcs for pycho 1


def god_hack():
    addr = getpointeraddress(module1 + 0x0038CBB8, health1_offsets)
    addr2 = getpointeraddress(module1 + 0x0038CBB8, raz_lives)
    while 1:
        try:
            mem.write_int(addr, 0x47960000)
            mem.write_int(addr2, 0x41000000)
            sleep(0.02)
            if keyboard.is_pressed("space"):
                keyboard.press_and_release("space")
                sleep(0.07)
                continue
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def Legendary_mode():
    addr = getpointeraddress(module1 + 0x0038CBB8, health1_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def fuck_gravity():
    addr = getpointeraddress(module1 + 0x00386AE0, gravity1_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x1380)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr, 0x1)
            break


def fuck_walls():
    addr = getpointeraddress(module1 + 0x00386AE0, no_clip_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x00000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("H"):
            mem.write_int(addr, 0x2)
            break


def fuck_walking():
    addr = getpointeraddress(module1 + 0x00383834, run_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x40c00000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr, 0x3f800000)
            break


def fuck_walking2():
    addr = getpointeraddress(module1 + 0x003839D8, walk_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x40c00000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr, 0x3f800000)
            break


def stats():
    Reader = getpointeraddress(module1 + 0x003839D8, z_offsets)
    Reader1 = getpointeraddress(module1 + 0x00386AE0, y_offsets)
    Reader2 = getpointeraddress(module1 + 0x003839D8, x_offsets)

    while 1:
        try:
            mem.read_float(Reader)
            mem.read_float(Reader1)
            mem.read_float(Reader2)
            print(Reader, Reader1, Reader2)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


# tele
def tele_main_lodge():
    addr = getpointeraddress(module1 + 0x003839D8, z_offsets)
    addr1 = getpointeraddress(module1 + 0x00386AE0, y_offsets)
    addr2 = getpointeraddress(module1 + 0x003839D8, x_offsets)
    try:
        mem.write_int(addr, 0x45d690af)
        mem.write_int(addr1, 0xc5981d25)
        mem.write_int(addr2, 0x45cda36d)
    except pymem.exception.MemoryWriteError as e:
        print(f"Error writing memory: {e}")


def big_raz():
    addr = getpointeraddress(module1 + 0X003839D8, player_size_1)
    addr1 = getpointeraddress(module1 + 0X00383A30, player_size_2)
    addr2 = getpointeraddress(module1 + 0X003839D8, player_size_3)
    while 1:
        try:
            mem.write_int(addr, 0x41000000)
            mem.write_int(addr1, 0x41000000)
            mem.write_int(addr2, 0x41000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            mem.write_int(addr1, 0x3f800000)
            mem.write_int(addr2, 0x3f800000)
            break


def small_raz():
    addr = getpointeraddress(module1 + 0X003839D8, player_size_1)
    addr1 = getpointeraddress(module1 + 0X00383A30, player_size_2)
    addr2 = getpointeraddress(module1 + 0X003839D8, player_size_3)
    while 1:
        try:
            mem.write_int(addr, 0x3e4ccccd)
            mem.write_int(addr1, 0x3e4ccccd)
            mem.write_int(addr2, 0x3e4ccccd)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            mem.write_int(addr1, 0x3f800000)
            mem.write_int(addr2, 0x3f800000)
            break


# funcs for pycho 2


def god_hack2():
    addr1 = getpointeraddress(module_pycho2 + 0x05549500, laser_offsets)
    addr2 = getpointeraddress(module_pycho2 + 0x05540360, health_offsets)
    addr3 = getpointeraddress(module_pycho2 + 0x0533DD00, cash_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x57550000)
            mem.write_int(addr2, 0x47960000)
            mem.write_int(addr3, 0x5000)
            sleep(0.02)
            if keyboard.is_pressed("space"):
                keyboard.press_and_release("space")
                sleep(0.07)
                continue
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def spam():
    while 1:
        try:
            # spam e key
            presskey(18)
            time.sleep(0.01)
            releasekey(18)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            print("Bot shutting down...")
            break


def meth():
    addr = getpointeraddress(module_pycho2 + 0x054B9258, player_speed)
    addr2 = getpointeraddress(module_pycho2 + 0x05549500, walk_vel_offsets)
    addr3 = getpointeraddress(module_pycho2 + 0x05549500, max_vel_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x40a00000)
            mem.write_int(addr2, 0x459c4000)
            mem.write_int(addr3, 0x459c4000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            mem.write_int(addr2, 0x43fa0000)
            mem.write_int(addr3, 0x453b8000)
            break


def fuck_gravity_pycho2():
    addr = getpointeraddress(module_pycho2 + 0x054B9258, gravity_offsets2)
    while 1:
        try:
            mem.write_int(addr, 0x00000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def flip_gravity():
    addr = getpointeraddress(module_pycho2 + 0x05549500, flip_gravity_offsets)
    while 1:
        try:
            mem.write_int(addr, 0xbf800000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x40800000)
            break


def clock_increase():
    addr = getpointeraddress(module_pycho2 + 0x0554CE10, clock_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x41400000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def clock_decrease():
    addr = getpointeraddress(module_pycho2 + 0x0554CE10, clock_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x3e99999a)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def clock_stop():
    addr1 = getpointeraddress(module_pycho2 + 0x0554CE10, clock_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x00000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x3f800000)
            break


# funcs for bioshock inf

def bio_fly():
    addr1 = getpointeraddress(module_bio + 0x00358660, fly_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x43fa0000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


def bio_pistol():
    addr1 = getpointeraddress(module_bio + 0x00F6648C, pistol_ammo_offs)
    addr2 = getpointeraddress(module_bio + 0x00F687F8, salt_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x0000000c)
            mem.write_int(addr2, 0x00000064)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0000000c)
            mem.write_int(addr2, 0x0000000c)
            break


def bio_mon():
    addr1 = getpointeraddress(module_bio + 0x00FA2B98, money_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x00002328)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x00002328)
            break


# Halo 1 funcs


def John117():
    addr1 = getpointeraddress(module_halo + 0x01C38880, primary_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C38880, fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr2, 0x3f800000)
            break


def new_health():
    addr = getpointeraddress(module_halo + 0x01C35AB0, shield_offsets)

    while 1:
        try:
            mem.write_int(addr, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def shotgun():
    addr1 = getpointeraddress(module_halo + 0x01C38880, primary_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C38880, shotgun_trig_offsets)
    addr3 = getpointeraddress(module_halo + 0x01C38880, fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0x0)
            mem.write_int(addr3, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def no_spread():
    addr1 = getpointeraddress(module_halo + 0x01C38880, bullet_spread_offsets_2)
    addr2 = getpointeraddress(module_halo + 0x01C38880, trig_offsets)
    addr3 = getpointeraddress(module_halo + 0x01C38880, shotgun_trig_offsets)
    addr4 = getpointeraddress(module_halo + 0x01C38880, fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x000000c8)
            mem.write_int(addr2, 0x1)
            mem.write_int(addr3, 0x0)
            mem.write_int(addr4, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


def wall_pierce():
    addr1 = getpointeraddress(module_halo + 0x01C38880, bullet_spread_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x00000164)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


def old_health():
    addr = getpointeraddress(module_halo + 0x01BEA890, shield)

    while 1:
        try:
            mem.write_int(addr, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x1)
            break


def oldJohn117():
    addr1 = getpointeraddress(module_halo + 0x01C38900, primary_offsets2)
    addr2 = getpointeraddress(module_halo + 0x01C38900, fire_rate_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr2, 0x3f800000)
            break


def speed():
    addr1 = getpointeraddress(module_halo + 0x01C40480, player_speed_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x41700000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x3f800000)
            break


def fuck_walls_halo():
    addr1 = getpointeraddress(module_halo + 0x01C35AB0, noclip_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0xFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def fuck_gravity_halo():
    addr1 = getpointeraddress(module_halo + 0x01C35950, noclip_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0x244)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def fuck_walls2():
    addr1 = getpointeraddress(module_halo + 0x01C35950, noclip_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0xFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def fuck_gravity2_halo():
    addr1 = getpointeraddress(module_halo + 0x01C35950, noclip_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0x244)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def pause_game():
    addr1 = getpointeraddress(module_halo + 0x01C40480, pause)

    while 1:
        try:
            mem.write_int(addr1, 0x00000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x1)
            break


def haha_number_go_brrr():
    addr1 = getpointeraddress(module_halo + 0x01C40480, pause)
    addr2 = getpointeraddress(module_halo + 0x01C40480, pause)

    while 1:
        try:
            mem.write_int(addr1, 0x00000000)
            mem.write_int(addr2, 0x1)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x1)
            break


def hands():
    addr1 = getpointeraddress(module_halo + 0x01C35AB0, melee1_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C35AB0, melee2_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x1)
            mem.write_int(addr2, 0x1)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            mem.write_int(addr2, 0x30)
            break


def plasma():
    addr1 = getpointeraddress(module_halo + 0x01C38880, plasma_fire_rate_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C38880, fire_rate_offsets)
    addr3 = getpointeraddress(module_halo + 0x01C38880, plasma_ammo_offsets)
    addr4 = getpointeraddress(module_halo + 0x01C38880, bullet_spread_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0xFFFFFFFF)
            mem.write_int(addr2, 0xFFFFFFFF)
            mem.write_int(addr3, 0x3f4ccccd)
            mem.write_int(addr4, 0x00000164)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


#  Tele functions

def tele_up():
    addr = getpointeraddress(module_halo + 0x01C35950, Z_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x42480000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def tele_halo():
    addr = getpointeraddress(module_halo + 0x01C35950, Z_offsets)
    addr1 = getpointeraddress(module_halo + 0x01C35950, Y_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C35950, X_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x0)
            mem.write_int(addr1, 0x0)
            mem.write_int(addr2, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def tele_keys():
    addr = getpointeraddress(module_halo + 0x01C35950, Z_offsets)
    addr1 = getpointeraddress(module_halo + 0x01C35950, Y_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C35950, X_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0xbaf40305)
            mem.write_int(addr1, 0xe3860117)
            mem.write_int(addr2, 0x3f8fd600)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def plasma_pistol():
    addr = getpointeraddress(module_halo + 0x01C38880, plasma_ammo_offsets)
    addr2 = getpointeraddress(module_halo + 0x02EABA18, plasma_pistol_offsets)
    addr3 = getpointeraddress(module_halo + 0x01C38880, plasma_fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr, 0x3f4ccccd)
            mem.write_int(addr2, 0x01050e03)
            mem.write_int(addr3, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


# Isaac functions

def isaac_health():
    addr = getpointeraddress(module_isaac + 0x0021E3FC, isaac_health_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x00000006)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def isaac_bombs():
    addr = getpointeraddress(module_isaac + 0x0021E508, bomb_offsets)
    addr2 = getpointeraddress(module_isaac + 0x0021E598, bomb_timer_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x5)
            mem.write_int(addr2, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def isaac_fire_rate():
    addr = getpointeraddress(module_isaac + 0x0021A1F4, isaac_fire_rate_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break

