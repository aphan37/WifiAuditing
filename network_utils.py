# === wifi_auditor/utils/network_utils.py ===

import os  # Used to run system-level commands for interface configuration

def set_monitor_mode(interface):
    """
    Puts the specified wireless interface into monitor mode.

    Monitor mode allows the interface to capture all wireless traffic,
    including packets not addressed to the device. This is necessary for
    sniffing and injecting packets in Wi-Fi auditing.

    Parameters:
        interface (str): The name of the wireless interface (e.g., wlan0).
    """
    os.system(f"ifconfig {interface} down")          # Bring the interface down
    os.system(f"iwconfig {interface} mode monitor")  # Change the mode to monitor
    os.system(f"ifconfig {interface} up")            # Bring the interface back up
    print(f"[*] {interface} set to monitor mode.")   # Confirm change


def reset_interface(interface):
    """
    Resets the specified wireless interface back to managed mode.

    Managed mode is the standard mode for connecting to Wi-Fi networks.
    This should be done after auditing to return the system to normal operation.

    Parameters:
        interface (str): The name of the wireless interface (e.g., wlan0mon).
    """
    os.system(f"ifconfig {interface} down")           
    os.system(f"iwconfig {interface} mode managed")   
    os.system(f"ifconfig {interface} up")             
    print(f"[*] {interface} reset to managed mode.")  
