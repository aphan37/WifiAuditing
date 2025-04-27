# Wi-Fi Security Auditing Tool

A simple project designed for educational and authorized testing purposes. This tool allows you to scan Wi-Fi networks, capture WPA/WPA2 handshakes, launch deauthentication attacks, crack captured handshakes, and detect rogue access points.

## Feature
- Network Scanner	| Scans and lists nearby Wi-Fi networks
- Handshake Capturer	| Captures WPA/WPA2 authentication handshakes
- Deauthentication | Attack	Forces devices to reconnect to capture handshakes
- Password Cracker	| Launches dictionary attacks on handshake captures
- Rogue AP Detector	| Detects suspicious fake access points
- Auto Modes	| Optional full-auto scanning, attacking, and cracking

## Structure
![image](https://github.com/user-attachments/assets/b7c4ddfb-ecd2-45d3-8c44-0e750a8e71f0)

## Implement Tools
Component | Tool/Library | Purpose
Programming Language | Python 3.8+ | Main logic and control
Packet Capture / Injection | Scapy | Build and sniff 802.11 packets
Password Cracking | Aircrack-ng | WPA/WPA2 handshake cracking
Monitor Mode Management | ifconfig / iwconfig (Linux CLI) | Enable monitor mode on Wi-Fi interface
Hardware | USB Wi-Fi Adapter with Monitor Mode | Required for packet injection/sniffing
Virtual Machine (Optional) | VirtualBox or VMware | Host Kali Linux environment on Windows

## Setup Process
📋 Setup Process
- Install Kali Linux (VM or Dual Boot)
- Connect external Wi-Fi USB adapter
- Pass adapter to Kali (in VM settings)
- Update system packages: sudo apt update && sudo apt upgrade
- Install required tools:
+ sudo apt install aircrack-ng python3-pip
+ pip3 install scapy pywifi
- Set Wi-Fi adapter to monitor mode:
+ sudo ifconfig wlan0 down
+ sudo iwconfig wlan0 mode monitor
+ sudo ifconfig wlan0 up

## Mechanism
- scanner.py identifies all nearby Wi-Fi networks
- User selects a target (or tool picks strongest automatically)
- handshake_capture.py captures WPA/WPA2 handshake (passive and/or active deauth)
- Handshake saved into captures/ folder as .pcap
- cracker.py automatically starts dictionary attack on captured handshake
- If rogue APs are detected, alert user
