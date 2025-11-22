import os
import socket
import fcntl
import struct

# list of network interfaces
network_interfaces = []


# Get the IP adress for the interface
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(
            fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack("256s", ifname.encode("utf-8")[:15]),
            )[20:24]
        )
    except OSError:
        return None


# scan for interfaces using the net folder
def scan_network_interfaces():
    try:
        interfaces = os.listdir("/sys/class/net/")
    except FileNotFoundError:
        print("/sys/class/net/ not found")
        return

    for interface in interfaces:
        interface_path = f"/sys/class/net/{interface}"

        # Get interface status
        try:
            with open(os.path.join(interface_path, "operstate"), "r") as file:
                up = file.read().strip() == "up"
        except Exception as e:
            print(f"Error getting interface status: {e}")
            up = "No"

        # Get MAC address
        try:
            with open(os.path.join(interface_path, "address"), "r") as file:
                mac = file.read().strip()
        except Exception as e:
            print(f"Error getting Mac address: {e}")

            mac = "Empty"

        # Get IPv4 address
        ip = get_ip_address(interface)

        network_interfaces.append(
            {"Name": interface, "IP": [ip] if ip else "no ipv4", "MAC": mac, "Up": up}
        )

    return network_interfaces
