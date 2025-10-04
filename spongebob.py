from offsets import *
from main import *


# CosmicShake-Win64-Shipping.exe threads
def spongebob_multi_fly():
    new_thread = Thread(target=sponge_fly, daemon=True)
    new_thread.start()


def garfield_rich():
    new_thread = Thread(target=garfield_cash_func, daemon=True)
    new_thread.start()


def garfield_fast():
    new_thread = Thread(target=garfield_speed_func, daemon=True)
    new_thread.start()


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


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


def garfield_cash_func():
    addr = getpointeraddress(module_garfield + 0x001F10AC, garfield_cash)
    while 1:
        try:
            mem.write_int(addr, 0x100000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("c"):
            break


def garfield_speed_func():
    addr = getpointeraddress(module_garfield + 0x001F3944, garfield_speed)
    while True:
        try:
            speed_input = float(input("\nSet speed: "))
            go = input("\nReady for lasagna? (yes/no): ")
            if go == "yes":
                print("It's time for lasagna!!!")
                while 1:
                    try:
                        mem.write_float(addr, speed_input)
                    except pymem.exception.MemoryWriteError as e:
                        print(f"Error writing memory: {e}")
                    if keyboard.is_pressed("c"):
                        break
            else:
                if go == "no":
                    print("Lasagna going in the fridge")
                    break
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break


keyboard.add_hotkey("F", spongebob_multi_fly)
