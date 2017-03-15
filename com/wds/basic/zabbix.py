import psutil
import re
import sys
from psutil import Process

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

if __name__ == "__main__":

    proc = process_info("pycharm64.exe")
    print(proc.cpu_times())
    print(proc.memory_info_ex)
    print(proc.memory_info)
    print(proc.memory_full_info())
    print(proc)