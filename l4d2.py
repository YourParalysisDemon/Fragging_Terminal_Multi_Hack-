import keyboard
import pymem
from main import *
from offsets import *


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


def l4d2_bhop_thread():
    new_thread = Thread(target=l4d2_bhop, daemon=True)
    new_thread.start()


def l4d2_trigger_bot_thread():
    new_thread = Thread(target=l4d2_trigger_bot, daemon=True)
    new_thread.start()


def l4d2_bhop():
    addr1 = readpointeraddress(module_l4d2_client + 0X007C9BA8, l4d2_in_air)
    addr2 = (module_l4d2_client + 0X759E70)
    while 1:
        if keyboard.is_pressed("spacebar"):
            try:
                jump = mem.read_int(addr1)
                if jump == 2:
                    try:
                        mem.write_int(addr2, 5)
                        sleep(0.2)
                    finally:
                        print("\r", "jump", end="", flush=True)
                if jump == 1:
                    try:
                        mem.write_int(addr2, 4)
                    finally:
                        print("\r", "In air", end="", flush=True)
            except pymem.exception.MemoryReadError as e:
                print(f"Error reading memory: {e}")
                break
        if keyboard.is_pressed("F1"):
            print("\r", "bhop off", end="", flush=True)
            break


def l4d2_trigger_bot():
    addr1 = readpointeraddress(module_l4d2_client + 0X000F8826, l4d2_trigger)  # NPC traceline value 68 to 69
    addr2 = (module_l4d2_client + 0X759F48)  # Fire gun
    players = []  # chose if you want to target only players
    zombies = []  # chose if you want to only target zombies
    while 1:
        if keyboard.is_pressed("C"):
            try:
                trigger = mem.read_int(addr1)
                if trigger > 255:
                    try:
                        mem.write_int(addr2, 6)
                    finally:
                        print("\r", "Target", end="", flush=True)
                if trigger == 255:
                    try:
                        mem.write_int(addr2, 4)
                        sleep(0.06)
                    finally:
                        print("\r", "No Target", end="", flush=True)
            except pymem.exception.MemoryReadError as e:
                print(f"Error reading memory: {e}")
                break
        if keyboard.is_pressed("F1"):
            print("\r", "Trigger_bot off", end="", flush=True)
            break
