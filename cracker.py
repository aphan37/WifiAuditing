# === wifi_auditor/cracker.py ===
import subprocess
def crack_handshake(target_bssid, handshake_file, wordlist_file, log_file="aircrack_out.log"):
    print("[*] Cracking handshake with Aircrack-ng...")
    cmd = ["aircrack-ng", "-w", wordlist_file, "-b", target_bssid, handshake_file]

    with open(log_file, "w") as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)

    print(f"[*] Output saved to {log_file}")    