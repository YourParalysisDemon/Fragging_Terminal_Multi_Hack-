from offsets import *
from main import *


# CosmicShake-Win64-Shipping.exe threads
def spongebob_multi_fly():
    new_thread = Thread(target=sponge_fly, daemon=True)
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


keyboard.add_hotkey("F", spongebob_multi_fly)
