import keyboard
import pymem.exception
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from time import *
from offsets import *
from main import *

mem = Pymem("Psychonauts2-Win64-Shipping")
module_pycho2 = module_from_name(mem.process_handle, "Psychonauts2-Win64-Shipping.exe").lpBaseOfDll


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


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

