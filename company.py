from main import *
from offsets import *

# The game were hacking
mem = Pymem("RelicCOH")
# The dll we write to
module = module_from_name(mem.process_handle, "WW2Mod.dll").lpBaseOfDll


# Are threads
def multi_run_money_coh():
    new_thread = Thread(target=money_hack_coh, daemon=True)
    new_thread.start()


def multi_run_gas_coh():
    new_thread = Thread(target=gas_hack_coh, daemon=True)
    new_thread.start()


def multi_run_pop_coh():
    new_thread = Thread(target=cap_hack_coh, daemon=True)
    new_thread.start()


def multi_run_ammo_coh():
    new_thread = Thread(target=ammo_hack_coh, daemon=True)
    new_thread.start()


# Are functions
def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


def money_hack_coh():
    addr = getpointeraddress(module + 0x0061E810, Money_offsets_coh)
    addr2 = getpointeraddress(module + 0x0061E810, command_offsets_coh)

    while 1:
        try:
            mem.write_int(addr, 0x47960000)
            mem.write_int(addr2, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            break


def gas_hack_coh():
    addr = getpointeraddress(module + 0x0061E810, gas_offsets_coh)
    while 1:
        try:
            mem.write_int(addr, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            break


def ammo_hack_coh():
    addr = getpointeraddress(module + 0x0061E810, ammo_offsets_coh)
    while 1:
        try:
            mem.write_int(addr, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            break


def cap_hack_coh():
    addr = getpointeraddress(module + 0x0061E810, cap_offsets_coh)
    while 1:
        try:
            mem.write_int(addr, 0x1)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            break
