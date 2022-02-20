
## To launch this script you have to add the attribute --target or -t, like so:
## network_scanner.py -t 192.168.0.1/24 (for example)

import scapy.all as scapy
import optparse

def get_arguments():
    
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest='target', help='Which IP range do you want to target?')
    (values,arguments) = parser.parse_args()
    if not values.target:
        parse.error('[-] Please specify an IP range.')
    else:
        return values

def scan(ip):
    #pdst is the IPField, dst = broadcast MAC Address
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # We can combine them using forward slash
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # capturing answered packets through the 'send n receive' function
    # into the variable 'answered'. As we don't need the unanswered packets,
    # we only ask for the first element in the list, [0]

    clients_list = []
    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list

# We are creating a list of dictionaries


def print_result(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

target_ip_range = get_arguments()
scan_result = scan(target_ip_range.target)

# We capture the clients_list returned by the function scan
# in the variable scan_result
print_result(scan_result)
# We loop over the list we captures in scan_result and print it
