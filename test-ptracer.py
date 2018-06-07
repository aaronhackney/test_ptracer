#!/usr/bin/env python
from test_ptracer.asdm import ASDM
from colorama import Fore
from colorama import Style


def main():
    #########################################################
    # User configurable settings
    # !!WARNING!! Never put your credentials in a script! This is for demonstration purposes only!

    asdm_username = 'cisco'
    asdm_password = 'sanfran'
    asa_ip = '172.16.127.127'
    asdm_port = 8443

    # Set IPs/Ports we wish to test
    source_addresses = ['8.8.8.8']
    destination_addresses = ['192.168.248.248', '10.255.255.10', '172.16.127.127']
    destination_ports = {
        "HTTP": 80, "HTTPS": 443, "RDP": 3389, "MYSQL": 3306, "FTP": 21, "SSH": 22, "TELNET": 23, "SMTP": 25, "DNS": 53,
        "TFTP":69, "POP": 110, "NTP": 123, "NETBIOS1": 137, "NETBIOS2": 138, "NETBIOS3": 139, "IMAP": 143, "LDAP": 389,
        "LDAPS": 636, "FTPS":990
    }
    #
    #########################################################

    asdm = ASDM()                                       # Create an instance of the ASDM class
    asdm.set_credentials(asdm_username, asdm_password)  # Set your ASDM credentials
    asdm.set_asdm_endpoint(asa_ip, asdm_port)           # Set management IP and port the ASDM service is listening on
    asdm.set_headers()                                  # Set the auth and content headers
    asdm.set_ssl_insecure()                             # Ignore SSL certificate errors !! DANGER !!

    for source_ip in source_addresses:                  # Loop through the source and destination IP addresses & ports
        print ("Source IP: " + source_ip + '\n')
        for dest_ip in destination_addresses:
            print ("Destination IP: " + dest_ip)
            print ('---------------------------------')
            for dest_port in destination_ports:
                asdm.set_ptrace_data(source_ip, dest_ip, destination_ports[dest_port])
                asdm.asdm_call()

                if asdm.action is None:
                    result = 'UNKNOWN'
                elif asdm.action == 'drop':
                    result = Fore.GREEN + asdm.action + Style.RESET_ALL     # Print drops in green
                else:
                    result = Fore.RED + asdm.action + Style.RESET_ALL       # Print permits in red
                print ('{0:<15} {1:>8}'.format(dest_port, result))
            print ('')


if __name__ == "__main__":
    main()
