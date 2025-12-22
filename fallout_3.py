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


def fallout_bullet_tele_thread():
    new_thread = Thread(target=bullet_tele, daemon=True)
    new_thread.start()


def bullet_tele():
    addr1 = readpointeraddress(module_fallout + 0X00E3F630, bullet_z_fallout)
    addr2 = readpointeraddress(module_fallout + 0X00E3F630, bullet_x_fallout)
    addr3 = readpointeraddress(module_fallout + 0X00E3F630, bullet_y_fallout)

    player_z = getpointeraddress(module_fallout + 0X00E3F77C, z_offsets_fallout)
    player_x = getpointeraddress(module_fallout + 0X00E9E574, x_offsets_fallout)
    player_y = getpointeraddress(module_fallout + 0X00E9E568, y_offsets_fallout)
    while 1:
        if keyboard.is_pressed("C"):
            try:
                z = mem.read_float(addr1)
                x = mem.read_float(addr2)
                y = mem.read_float(addr3)

                mem.write_float(player_z, z)
                mem.write_float(player_x, x)
                mem.write_float(player_y, y)
            except pymem.exception.MemoryWriteError as e:
                print(f"Error writing memory: {e}")
                break
