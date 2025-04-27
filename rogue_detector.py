# === wifi_auditor/rogue_detector.py ===
from scapy.all import *

known_networks = {}


def rogue_detector(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode(errors='ignore')
        bssid = packet[Dot11].addr3
        if ssid in known_networks:
            if known_networks[ssid] != bssid:
                print(f"[!] Rogue AP detected: SSID={ssid}, BSSID={bssid}")
        else:
            known_networks[ssid] = bssid
