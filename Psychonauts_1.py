import keyboard
import pymem.exception
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from time import *
from offsets import *
from main import *

mem = Pymem("Psychonauts")
module1 = module_from_name(mem.process_handle, "Psychonauts.exe").lpBaseOfDll


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


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


def multi_run_raz_stats():
    new_thread = Thread(target=stats, daemon=True)
    new_thread.start()


def multi_run_raz_flip():
    new_thread = Thread(target=flip_gravity_pycho1, daemon=True)
    new_thread.start()


# funcs for pycho 1

def stats():
    Reader = getpointeraddress(module1 + 0x003839D8, z_offsets)
    Reader1 = getpointeraddress(module1 + 0x00386AE0, y_offsets)
    Reader2 = getpointeraddress(module1 + 0x003839D8, x_offsets)

    while 1:
        try:
            mem.read_float(Reader)
            mem.read_float(Reader1)
            mem.read_float(Reader2)
            print(f"Coordinates: ({Reader}, {Reader1}, {Reader2})")
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


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


def flip_gravity_pycho1():
    addr = getpointeraddress(module1 + 0x00386AE0, roof_walker)
    while 1:
        try:
            mem.write_int(addr, 0xbf800000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr, 0x3f800000)
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


def stats_halo():
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
