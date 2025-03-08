import keyboard
import pymem.exception
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from time import *
from offsets import *
from main import *

mem = Pymem("MCC-Win64-Shipping")
module_halo = module_from_name(mem.process_handle, "halo1.dll").lpBaseOfDll


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


# Threads for Halo 1


def multi_run_117():
    new_thread = Thread(target=John117, daemon=True)
    new_thread.start()


def multi_run_0ld_117():
    new_thread = Thread(target=oldJohn117, daemon=True)
    new_thread.start()


def multi_run_gravity2():
    new_thread = Thread(target=fuck_gravity2_halo, daemon=True)
    new_thread.start()


def multi_run_clip2():
    new_thread = Thread(target=fuck_walls2, daemon=True)
    new_thread.start()


def multi_run_clip():
    new_thread = Thread(target=fuck_walls, daemon=True)
    new_thread.start()


def multi_run_gravity_halo():
    new_thread = Thread(target=fuck_gravity_halo, daemon=True)
    new_thread.start()


def multi_run_plasma():
    new_thread = Thread(target=plasma, daemon=True)
    new_thread.start()


def multi_run_hands():
    new_thread = Thread(target=hands, daemon=True)
    new_thread.start()


def multi_run_speed():
    new_thread = Thread(target=speed, daemon=True)
    new_thread.start()


def multi_run_nospread():
    new_thread = Thread(target=no_spread, daemon=True)
    new_thread.start()


def multi_run_bullet():
    new_thread = Thread(target=stats, daemon=True)
    new_thread.start()


def multi_run_pause():
    new_thread = Thread(target=pause_game, daemon=True)
    new_thread.start()


def multi_run_haha():
    new_thread = Thread(target=haha_number_go_brrr, daemon=True)
    new_thread.start()


def multi_run_shotgun():
    new_thread = Thread(target=shotgun, daemon=True)
    new_thread.start()


def multi_run_old_health():
    new_thread = Thread(target=old_health, daemon=True)
    new_thread.start()


def multi_run_new_health():
    new_thread = Thread(target=new_health, daemon=True)
    new_thread.start()


def multi_run_wall_pierce():
    new_thread = Thread(target=wall_pierce, daemon=True)
    new_thread.start()


def multi_run_plasma_pistol():
    new_thread = Thread(target=plasma_pistol, daemon=True)
    new_thread.start()


# Halo 1 funcs


def John117():
    addr1 = getpointeraddress(module_halo + 0x01C38880, primary_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C38880, fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr2, 0x3f800000)
            break


def new_health():
    addr = getpointeraddress(module_halo + 0x01C35AB0, shield_offsets)

    while 1:
        try:
            mem.write_int(addr, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def shotgun():
    addr1 = getpointeraddress(module_halo + 0x01C38880, primary_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C38880, shotgun_trig_offsets)
    addr3 = getpointeraddress(module_halo + 0x01C38880, fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0x0)
            mem.write_int(addr3, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def no_spread():
    addr1 = getpointeraddress(module_halo + 0x01C38880, bullet_spread_offsets_2)
    addr2 = getpointeraddress(module_halo + 0x01C38880, trig_offsets)
    addr3 = getpointeraddress(module_halo + 0x01C38880, shotgun_trig_offsets)
    addr4 = getpointeraddress(module_halo + 0x01C38880, fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x000000c8)
            mem.write_int(addr2, 0x1)
            mem.write_int(addr3, 0x0)
            mem.write_int(addr4, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


def wall_pierce():
    addr1 = getpointeraddress(module_halo + 0x01C38880, bullet_spread_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x00000164)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


def old_health():
    addr = getpointeraddress(module_halo + 0x01BEA890, shield)

    while 1:
        try:
            mem.write_int(addr, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x1)
            break


def oldJohn117():
    addr1 = getpointeraddress(module_halo + 0x01C38900, primary_offsets2)
    addr2 = getpointeraddress(module_halo + 0x01C38900, fire_rate_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr2, 0x3f800000)
            break


def speed():
    addr1 = getpointeraddress(module_halo + 0x01C40480, player_speed_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x41700000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x3f800000)
            break


def fuck_walls_halo():
    addr1 = getpointeraddress(module_halo + 0x01C35AB0, noclip_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0xFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def fuck_gravity_halo():
    addr1 = getpointeraddress(module_halo + 0x01C35950, noclip_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0x244)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def fuck_walls2():
    addr1 = getpointeraddress(module_halo + 0x01C35950, noclip_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0xFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def fuck_gravity2_halo():
    addr1 = getpointeraddress(module_halo + 0x01C35950, noclip_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0x244)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def pause_game():
    addr1 = getpointeraddress(module_halo + 0x01C40480, pause)

    while 1:
        try:
            mem.write_int(addr1, 0x00000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x1)
            break


def haha_number_go_brrr():
    addr1 = getpointeraddress(module_halo + 0x01C40480, pause)
    addr2 = getpointeraddress(module_halo + 0x01C40480, pause)

    while 1:
        try:
            mem.write_int(addr1, 0x00000000)
            mem.write_int(addr2, 0x1)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x1)
            break


def hands():
    addr1 = getpointeraddress(module_halo + 0x01C35AB0, melee1_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C35AB0, melee2_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x1)
            mem.write_int(addr2, 0x1)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            mem.write_int(addr2, 0x30)
            break


def plasma():
    addr1 = getpointeraddress(module_halo + 0x01C38880, plasma_fire_rate_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C38880, fire_rate_offsets)
    addr3 = getpointeraddress(module_halo + 0x01C38880, plasma_ammo_offsets)
    addr4 = getpointeraddress(module_halo + 0x01C38880, bullet_spread_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0xFFFFFFFF)
            mem.write_int(addr2, 0xFFFFFFFF)
            mem.write_int(addr3, 0x3f4ccccd)
            mem.write_int(addr4, 0x00000164)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


#  Tele functions

def tele_up():
    addr = getpointeraddress(module_halo + 0x01C35950, Z_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x42480000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def tele_halo():
    addr = getpointeraddress(module_halo + 0x01C35950, Z_offsets)
    addr1 = getpointeraddress(module_halo + 0x01C35950, Y_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C35950, X_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x0)
            mem.write_int(addr1, 0x0)
            mem.write_int(addr2, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def tele_keys():
    addr = getpointeraddress(module_halo + 0x01C35950, Z_offsets)
    addr1 = getpointeraddress(module_halo + 0x01C35950, Y_offsets)
    addr2 = getpointeraddress(module_halo + 0x01C35950, X_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0xbaf40305)
            mem.write_int(addr1, 0xe3860117)
            mem.write_int(addr2, 0x3f8fd600)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def plasma_pistol():
    addr = getpointeraddress(module_halo + 0x01C38880, plasma_ammo_offsets)
    addr2 = getpointeraddress(module_halo + 0x02EABA18, plasma_pistol_offsets)
    addr3 = getpointeraddress(module_halo + 0x01C38880, plasma_fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr, 0x3f4ccccd)
            mem.write_int(addr2, 0x01050e03)
            mem.write_int(addr3, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break

