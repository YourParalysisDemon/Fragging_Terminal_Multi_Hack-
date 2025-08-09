from main import *
from offsets import *


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


def multi_isaac_health():
    new_thread = Thread(target=isaac_health, daemon=True)
    new_thread.start()


def multi_isaac_health_set():
    new_thread = Thread(target=isaac_health_set, daemon=True)
    new_thread.start()


def multi_isaac_bomb():
    new_thread = Thread(target=isaac_bombs, daemon=True)
    new_thread.start()


def multi_isaac_fire():
    new_thread = Thread(target=isaac_fire_rate, daemon=True)
    new_thread.start()


# Isaac functions needs to be fixed :(

def isaac_health():
    addr = getpointeraddress(module_isaac + 0x007FD65C, isaac_health_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x41200000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            break


def isaac_health_set():
    addr1 = getpointeraddress(module_isaac + 0x007FD65C, isaac_health_offsets)
    try:
        health_input = float(input("\nEnter health value: "))
        print("\nHealth set")
        mem.write_float(addr1, health_input)
    except pymem.exception.MemoryWriteError as e:
        print(f"Error writing memory: {e}")


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
    addr = getpointeraddress(module_isaac + 0x007FD65C, isaac_fire_rate_offsets)
    while 1:
        try:
            mem.write_double(addr, float(0))
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            break
