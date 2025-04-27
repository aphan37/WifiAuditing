# === wifi_auditor/scanner.py ===
from scapy.all import *
def packet_handler(packet, networks):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode(errors='ignore')
        bssid = packet[Dot11].addr3
        channel = int(ord(packet[Dot11Elt:3].info))
        if bssid not in networks:
            networks[bssid] = {'ssid': ssid, 'bssid': bssid, 'channel': channel}

def scan_networks(interface):
    networks = {}
    sniff(iface=interface, prn=lambda pkt: packet_handler(pkt, networks), timeout=15)
    return list(networks.values())
