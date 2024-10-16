import scapy.all as scapy

def process_packet(pkt):
    """ This function processes each captured packet and displays relevant information. """
    print("\nCaptured Packet Info:")
    
    # Display timestamp of the packet capture
    print(f"Timestamp: {pkt.time}")
    
    # Display Source and Destination IPs if the packet contains an IP layer
    if pkt.haslayer(scapy.IP):
        print(f"Source IP Address: {pkt[scapy.IP].src}")
        print(f"Destination IP Address: {pkt[scapy.IP].dst}")
    
    # Check if the packet has a TCP layer and display relevant info
    if pkt.haslayer(scapy.TCP):
        print(f"Transport Protocol: TCP")
        print(f"Source Port: {pkt[scapy.TCP].sport}")
        print(f"Destination Port: {pkt[scapy.TCP].dport}")
    
    # Check if the packet has a UDP layer
    elif pkt.haslayer(scapy.UDP):
        print(f"Transport Protocol: UDP")
        print(f"Source Port: {pkt[scapy.UDP].sport}")
        print(f"Destination Port: {pkt[scapy.UDP].dport}")
    
    # Check for ICMP (Ping) protocol
    elif pkt.haslayer(scapy.ICMP):
        print(f"Transport Protocol: ICMP (Ping)")
    
    # Display Raw Payload if present in the packet
    if pkt.haslayer(scapy.Raw):
        payload = pkt[scapy.Raw].load
        print(f"Packet Payload (First 50 bytes): {payload[:50]}...")  # Only show the first 50 bytes of data

def begin_sniffing(interface_name="eth0"):
    """ Starts sniffing network packets on a given interface. """
    print(f"Starting packet capture on {interface_name}...")
    scapy.sniff(iface=interface_name, prn=process_packet, store=0)

if __name__ == "__main__":
    interface_input = input("Enter the network interface for packet capture (e.g., eth0, wlan0): ")
    begin_sniffing(interface_input)
