import psutil
import re
import sys
from psutil import Process
from time import sleep

def process_info(procName):
    try:
        for proc in psutil.process_iter():
            #print(proc.name())
            if proc.name().lower() == procName.lower():
                return proc
    except psutil.AccessDenied:
        pass
    except psutil.NoSuchProcess:
        pass
    return None

def print_sys_info():
    proc = process_info("pycharm64.exe")
    print(proc.environ())
    print(proc.cpu_percent())
    print(proc.cpu_times())
    print(proc.memory_maps())
    print(proc.num_ctx_switches())
    print(proc.num_threads())
    print(proc.num_handles())

if __name__ == "__main__":
    proc = psutil.Process(8384)
    #print(proc.name())
    #print(proc.connections())
    #for conn in proc.connections():
       # print(conn)
    #print(proc.status())
    #print(proc.io_counters())
    #print(proc.uids())
    #print(proc.gids())
    while(0 == 0):
        sleep(1)
        proc = process_info("pycharm64.exe")
        print(proc.cpu_times)
    print(proc.cpu_percent())
    #print(proc.memory_info)
    #print(proc.memory_percent())
    #for memmap in proc.memory_maps():
        #print(memmap)
