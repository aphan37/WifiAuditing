# === wifi_auditor/cracker.py ===
import subprocess
def crack_handshake(target_bssid, handshake_file, wordlist_file):
    print("[*] Cracking handshake with Aircrack-ng...")
    cmd = ["aircrack-ng", "-w", wordlist_file, "-b", target_bssid, handshake_file]
    subprocess.run(cmd)
