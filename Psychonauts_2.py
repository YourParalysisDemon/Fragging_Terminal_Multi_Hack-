from Pycho1 import *
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


endInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class input_i(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", input_i)]


# Actuals Functions
def presskey(hexkeycode):
    extra = ctypes.c_ulong(0)
    ii_ = input_i()
    ii_.ki = KeyBdInput(0, hexkeycode, 0x0008, 0, ctypes.pointer(extra))
    x = input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def releasekey(hexkeycode):
    extra = ctypes.c_ulong(0)
    ii_ = input_i()
    ii_.ki = KeyBdInput(0, hexkeycode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# Threads for pycho 2


def multi_run_god2():
    new_thread = Thread(target=god_hack2, daemon=True)
    new_thread.start()


def multi_run_meth():
    new_thread = Thread(target=meth, daemon=True)
    new_thread.start()


def multi_run_fuck_gravity():
    new_thread = Thread(target=fuck_gravity_pycho2, daemon=True)
    new_thread.start()


def multi_run_spam():
    new_thread = Thread(target=spam, daemon=True)
    new_thread.start()


def multi_run_flip():
    new_thread = Thread(target=flip_gravity, daemon=True)
    new_thread.start()


def multi_run_slow():
    new_thread = Thread(target=clock_decrease, daemon=True)
    new_thread.start()


def multi_run_fast():
    new_thread = Thread(target=clock_increase, daemon=True)
    new_thread.start()


def multi_run_stop():
    new_thread = Thread(target=clock_stop, daemon=True)
    new_thread.start()


# funcs for pycho 2


def god_hack2():
    addr1 = getpointeraddress(module_pycho2 + 0x05549500, laser_offsets)
    addr2 = getpointeraddress(module_pycho2 + 0x05540360, health_offsets)
    addr3 = getpointeraddress(module_pycho2 + 0x0533DD00, cash_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x57550000)
            mem.write_int(addr2, 0x47960000)
            mem.write_int(addr3, 0x5000)
            sleep(0.02)
            if keyboard.is_pressed("space"):
                keyboard.press_and_release("space")
                sleep(0.07)
                continue
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            break


def spam():
    while 1:
        try:
            # spam e key
            presskey(18)
            time.sleep(0.01)
            releasekey(18)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            print("Bot shutting down...")
            break


def meth():
    addr = getpointeraddress(module_pycho2 + 0x054B9258, player_speed)
    addr2 = getpointeraddress(module_pycho2 + 0x05549500, walk_vel_offsets)
    addr3 = getpointeraddress(module_pycho2 + 0x05549500, max_vel_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x40a00000)
            mem.write_int(addr2, 0x459c4000)
            mem.write_int(addr3, 0x459c4000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            mem.write_int(addr2, 0x43fa0000)
            mem.write_int(addr3, 0x453b8000)
            break


def fuck_gravity_pycho2():
    addr = getpointeraddress(module_pycho2 + 0x054B9258, gravity_offsets2)
    while 1:
        try:
            mem.write_int(addr, 0x00000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def flip_gravity():
    addr = getpointeraddress(module_pycho2 + 0x05549500, flip_gravity_offsets)
    while 1:
        try:
            mem.write_int(addr, 0xbf800000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x40800000)
            break


def clock_increase():
    addr = getpointeraddress(module_pycho2 + 0x0554CE10, clock_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x41400000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def clock_decrease():
    addr = getpointeraddress(module_pycho2 + 0x0554CE10, clock_offsets)
    while 1:
        try:
            mem.write_int(addr, 0x3e99999a)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            mem.write_int(addr, 0x3f800000)
            break


def clock_stop():
    addr1 = getpointeraddress(module_pycho2 + 0x0554CE10, clock_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x00000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
            break
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x3f800000)
            break