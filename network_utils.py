# === wifi_auditor/utils/network_utils.py ===
import os
def set_monitor_mode(interface):
    os.system(f"ifconfig {interface} down")
    os.system(f"iwconfig {interface} mode monitor")
    os.system(f"ifconfig {interface} up")
    print(f"[*] {interface} set to monitor mode.")


def reset_interface(interface):
    os.system(f"ifconfig {interface} down")
    os.system(f"iwconfig {interface} mode managed")
    os.system(f"ifconfig {interface} up")
    print(f"[*] {interface} reset to managed mode.")
