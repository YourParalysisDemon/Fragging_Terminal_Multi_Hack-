import keyboard
import pymem.exception
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from time import *
from offsets import *
from main import *

mem = Pymem("BioShockInfinite.exe")
module_bio = module_from_name(mem.process_handle, "BioShockInfinite.exe").lpBaseOfDll


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset
        
        
# Threads for bioshock inf

def multi_bio_fly():
    new_thread = Thread(target=bio_fly, daemon=True)
    new_thread.start()


def multi_bio_mon():
    new_thread = Thread(target=bio_mon, daemon=True)
    new_thread.start()


def multi_bio_pistol():
    new_thread = Thread(target=bio_pistol, daemon=True)
    new_thread.start()
    
    
# funcs for bioshock inf

def bio_fly():
    addr1 = getpointeraddress(module_bio + 0x00358660, fly_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x43fa0000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


def bio_pistol():
    addr1 = getpointeraddress(module_bio + 0x00F6648C, pistol_ammo_offs)
    addr2 = getpointeraddress(module_bio + 0x00F687F8, salt_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x0000000c)
            mem.write_int(addr2, 0x00000064)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0000000c)
            mem.write_int(addr2, 0x0000000c)
            break


def bio_mon():
    addr1 = getpointeraddress(module_bio + 0x00FA2B98, money_offs)
    while 1:
        try:
            mem.write_int(addr1, 0x00002328)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x00002328)
            break

