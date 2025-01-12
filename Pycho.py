import keyboard
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

print("Games avaliable, Psychonauts, Psychonauts 2, Halo 1, Bioshock infinite")

game = input(Fore.RED + Back.BLACK + Style.BRIGHT + "\nEnter game title: ")
if game == "Psychonauts":
    mem = Pymem("Psychonauts")
    module1 = module_from_name(mem.process_handle, "Psychonauts.exe").lpBaseOfDll

elif game == "Psychonauts 2":
    mem = Pymem("Psychonauts2-Win64-Shipping")
    module = module_from_name(mem.process_handle, "Psychonauts2-Win64-Shipping.exe").lpBaseOfDll

elif game == "Halo 1":
    mem = Pymem("MCC-Win64-Shipping")
    module2 = module_from_name(mem.process_handle, "halo1.dll").lpBaseOfDll

elif game == "Bioshock infinite":
    mem = Pymem("BioShockInfinite.exe")
    module3 = module_from_name(mem.process_handle, "BioShockInfinite.exe").lpBaseOfDll


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


# Threads for pycho 2


def multi_run_god2():
    new_thread = Thread(target=god_hack2, daemon=True)
    new_thread.start()


def multi_run_meth():
    new_thread = Thread(target=meth, daemon=True)
    new_thread.start()


def multi_run_fuck_gravity():
    new_thread = Thread(target=fuck_gravity2, daemon=True)
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


# funcs for pycho 1

def god_hack():
    addr = getpointeraddress(module1 + 0x0038CBB8, health1_offsets)
    addr1 = getpointeraddress(module1 + 0x00383838, blast_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x47960000)
            mem.write_int(addr1, 0x000001d2)
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


# funcs for pycho 2


def god_hack2():
    addr1 = getpointeraddress(module + 0x05549500, laser_offsets)
    addr2 = getpointeraddress(module + 0x05540360, health_offsets)
    addr3 = getpointeraddress(module + 0x0533DD00, cash_offsets)
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
    addr = getpointeraddress(module + 0x054B9258, player_speed)
    addr2 = getpointeraddress(module + 0x05549500, walk_vel_offsets)
    addr3 = getpointeraddress(module + 0x05549500, max_vel_offsets)
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


def fuck_gravity2():
    addr = getpointeraddress(module + 0x054B9258, gravity_offsets2)
    while 1:
        try:
            mem.write_int(addr, 0x00000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def flip_gravity():
    addr = getpointeraddress(module + 0x05549500, flip_gravity_offsets)
    while 1:
        try:
            mem.write_int(addr, 0xbf800000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x40800000)
            break


def clock_increase():
    addr = getpointeraddress(module + 0x0554CE10, clock_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x41400000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def clock_decrease():
    addr = getpointeraddress(module + 0x0554CE10, clock_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x3e99999a)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def clock_stop():
    addr1 = getpointeraddress(module + 0x0554CE10, clock_offsets)
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
    addr1 = getpointeraddress(module3 + 0x00358660, fly_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x43fa0000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


def bio_pistol():
    addr1 = getpointeraddress(module3 + 0x00F6648C, pistol_ammo_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x0000000c)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0000000c)
            break


def bio_mon():
    addr1 = getpointeraddress(module3 + 0x00FA2B98, money_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x00002328)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x00002328)
            break
