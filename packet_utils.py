# === wifi_auditor/utils/packet_utils.py ===
# (placeholder for future functions)

def create_deauth_packet(target_bssid, client_mac):
    from scapy.all import RadioTap, Dot11, Dot11Deauth
    dot11 = Dot11(addr1=client_mac, addr2=target_bssid, addr3=target_bssid)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    return packet
