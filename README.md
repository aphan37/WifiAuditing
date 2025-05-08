# Wi-Fi Security Auditing Tool

A simple project designed for educational and authorized testing purposes. This tool allows you to scan Wi-Fi networks, capture WPA/WPA2 handshakes, launch deauthentication attacks, crack captured handshakes, and detect rogue access points. Work with Jared Robinson and Dawn Marshall.

## Purpose
This Wi-Fi Security Auditing Tool demonstrates real-world wireless security auditing techniques. The goal of this project is to simulate a controlled penetration testing environment for education and research purposes. It mainly showcases how Python can bridge CLI tools like aircrack-ng with automated workflows.

## Setup
Clone and set up the project on Kali Linux virtual machine or a compatible Linux distro.
```
git clone https://github.com/aphan37/WifiAuditing.git
cd WifiAuditing
sudo apt update && sudo apt install aircrack-ng python3-pip python3-venv
pip install scapy pywifi
```
Download and unzip a sample .cap file for testing cracking functionality.
```
wget https://github.com/aircrack-ng/aircrack-ng/raw/master/test/wpa.cap
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
aircrack-ng wpa.cap -w /usr/share/wordlists/rockyou.txt
```

## Technical Details
- Scanning: Utilizes pywifi or scapy to list available SSIDs through signal strength, encryption type, and MAC addresses.
- Handshake Capture: Passive and active methods using monitor mode and deauthentication packets (aircrack-ng or scapy).
- Cracking: Automates dictionary attacks using aircrack-ng, referencing wordlists (rockyou.txt).
- Interface Handling: Shell commands like ifconfig and iwconfig manage interface modes.
- Rogue AP Detection: Analyzes anomalies in SSID broadcasting frequency or strength to warn about fake APs.


## Features
- Network Scanner	| Scans and lists nearby Wi-Fi networks
- Handshake Capturer	| Captures WPA/WPA2 authentication handshakes
- Deauthentication | Attack	Forces devices to reconnect to capture handshakes
- Password Cracker	| Launches dictionary attacks on handshake captures
- Rogue AP Detector	| Detects suspicious fake access points
- Auto Modes	| Optional full-auto scanning, attacking, and cracking

## Structure
![image](https://github.com/user-attachments/assets/b7c4ddfb-ecd2-45d3-8c44-0e750a8e71f0)

## Implement Tools
![image](https://github.com/user-attachments/assets/bba8790b-9dab-457b-bab7-8b3910160b85)

## Novelty
This project merges manual CLI tools with Python to offer an automated auditing pipeline. Future improvements could include:
* GUI dashboard
* AI-based rogue AP classification
* Expanded cracking strategies

## Legal Disclaimer
This tool is intended only for educational purposes and authorized security testing.
Unauthorized use on networks without permission is illegal and unethical.
Always perform penetration testing activities with explicit permission.
