from main import *
from offsets import *


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


# Threads
def multi_run_primary():
    new_thread = Thread(target=primary, daemon=True)
    new_thread.start()


def multi_run_money():
    new_thread = Thread(target=cash, daemon=True)
    new_thread.start()


def multi_run_fov():
    new_thread = Thread(target=fov, daemon=True)
    new_thread.start()


def multi_run_z():
    new_thread = Thread(target=Z, daemon=True)
    new_thread.start()


def multi_run_zd():
    new_thread = Thread(target=Zd, daemon=True)
    new_thread.start()


def multi_run_z2():
    new_thread = Thread(target=Z2, daemon=True)
    new_thread.start()


def multi_run_z3():
    new_thread = Thread(target=Z3, daemon=True)
    new_thread.start()


def cash():
    addr1 = getpointeraddress(module1 + 0x00D022D0, money)
    while 1:
        try:
            mem.write_int(addr1, 0x42c80000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
            break


def primary():
    addr1 = getpointeraddress(module1 + 0x00D01E50, primary_offsets)
    addr2 = getpointeraddress(module1 + 0x00D23550, health_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0x3f800000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def Z():
    addr1 = getpointeraddress(module1 + 0x00D01EB0, z_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x42c80000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
            break


def Z2():
    addr1 = getpointeraddress(module1 + 0x00D01EB0, z_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x42480000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
            break


def Z3():
    addr1 = getpointeraddress(module1 + 0x00D01EB0, z_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x41700000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
            break


def fov():
    addr1 = getpointeraddress(module1 + 0x00D3EFD0, fov_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x42b40000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x424c0000)
            break


def Zd():
    addr1 = getpointeraddress(module1 + 0x00D01EB0, dead_z_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x42480000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
            break

