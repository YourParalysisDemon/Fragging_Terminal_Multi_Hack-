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
             "● The binding of isaac",
             "● Spongebob CosmicShake",
             "● Metro 2033"]
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
    elif game == "TF2":  # Do not attach to a VAC secured server retard. Only run this code in -insecure mode.  
        mem = Pymem("tf_win64")
        module_tf2 = module_from_name(mem.process_handle, "engine.dll").lpBaseOfDll
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


# CosmicShake-Win64-Shipping.exe threads

def spongebob_multi_fly():
    new_thread = Thread(target=sponge_fly, daemon=True)
    new_thread.start()


# TF2 threads

def multi_tf2():
    new_thread = Thread(target=stats_tf2, daemon=True)
    new_thread.start()


def stats_tf2():  # Just a little experiment :) still heavily a wip. Will not work in VAC secured servers so don't be stupid. 
    addr1 = readpointeraddress(module_tf2 + 0x006DA9F8, health_tf2_offsets_1)
    addr2 = readpointeraddress(module_tf2 + 0x00479848, health_tf2_offsets_2)
    addr3 = readpointeraddress(module_tf2 + 0x0072FD18, health_tf2_offsets_3)
    addr4 = readpointeraddress(module_tf2 + 0x00779CD8, player_name_1)
    addr5 = readpointeraddress(module_tf2 + 0x00479868, player_name_2)
    addr6 = readpointeraddress(module_tf2 + 0x0053E6E8, player_name_3)
    while 1:
        try:
            h1 = mem.read_short(addr1)
            h2 = mem.read_short(addr2)
            h3 = mem.read_short(addr3)
            p1 = mem.read_string(addr4)
            p2 = mem.read_string(addr5)
            p3 = mem.read_string(addr6)
            R = [p1, h1,
                 p2, h2,
                 p3, h3]
            print("\r", R, end="", flush=True)
        except pymem.exception.MemoryReadError as e:
            print(f"Error reading memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            break


# funcs for bioshock inf

def bio_fly():
    addr1 = getpointeraddress(module_bio + 0x00358660, fly_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x43fa0000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
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
            break
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
            break
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x00002328)
            break


# Isaac functions needs to be fixed :(

def isaac_health():
    addr = getpointeraddress(module_isaac + 0x0021E3FC, isaac_health_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x00000006)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
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
            break
        if keyboard.is_pressed("F1"):
            break


def isaac_fire_rate():
    addr = getpointeraddress(module_isaac + 0x0021A1F4, isaac_fire_rate_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            break


# Spongebob CosmicShake

def sponge_fly():
    addr = getpointeraddress(module_sponge + 0x057309F0, spongebob_fly)
    while 1:
        try:
            mem.write_int(addr, 0x43fa0000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("c"):
            break
