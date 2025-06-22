from offsets import *
from main import *


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


def multi_isaac_bomb():
    new_thread = Thread(target=isaac_bombs, daemon=True)
    new_thread.start()


def multi_isaac_fire():
    new_thread = Thread(target=isaac_fire_rate, daemon=True)
    new_thread.start()


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

