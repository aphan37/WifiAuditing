# === wifi_auditor/handshake_capture.py ===

from scapy.all import *  # Import all Scapy networking tools

def capture_handshake(interface, target_bssid):
    """
    Listens for WPA/WPA2 EAPOL handshake packets on a given wireless interface.

    Parameters:
        interface (str): The monitor-mode wireless interface (e.g., wlan0mon).
        target_bssid (str): The MAC address of the target access point (used for filtering).
    """

    print("[*] Listening for handshake packets...")

    # Define a filter function that checks if a packet contains EAPOL (used in 4-way handshake)
    def handshake_filter(pkt):
        return pkt.haslayer(EAPOL) and pkt.addr1 and pkt.addr2

    # Sniff packets for 60 seconds or until interrupted, filtering only EAPOL-related traffic
    packets = sniff(iface=interface, lfilter=handshake_filter, timeout=60)

    # Further filter packets to include only those with the EAPOL layer
    handshake_packets = [pkt for pkt in packets if pkt.haslayer(EAPOL)]

    # If handshake packets are captured, save them to a .pcap file
    if handshake_packets:
        print("[+] Handshake captured!")
        wrpcap("captures/handshake.pcap", handshake_packets)  # Save to file
    else:
        print("[-] No handshake captured.")
