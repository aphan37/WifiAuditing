# === wifi_auditor/handshake_capture.py ===
from scapy.all import *
def capture_handshake(interface, target_bssid):
    print("[*] Listening for handshake packets...")

    def handshake_filter(pkt):
        return pkt.haslayer(EAPOL) and pkt.addr1 and pkt.addr2

    packets = sniff(iface=interface, lfilter=handshake_filter, timeout=60)
    handshake_packets = [pkt for pkt in packets if pkt.haslayer(EAPOL)]

    if handshake_packets:
        print("[+] Handshake captured!")
        wrpcap("captures/handshake.pcap", handshake_packets)
    else:
        print("[-] No handshake captured.")
