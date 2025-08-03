from offsets import *
from Pycho1 import *


def southpark_multi_health():
    new_thread = Thread(target=health_hack, daemon=True)
    new_thread.start()
    
    
def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


def health_hack():
    addr = getpointeraddress(module + 0x03CDD688, health_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x57550000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
                        
            
