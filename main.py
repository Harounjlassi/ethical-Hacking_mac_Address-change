#!usr/bin/env python
import subprocess
import optparse
import re
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac adress")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac adress")
    (options,arguments)= parser.parse_args()
    if not options.interface:
         parser.error("[-] please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] please specify a mac , use --help for more info")
    return  options

def changemac(interface,new_mac):
    print("[+] changing mac adress for " + interface+"  " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


"""
interface = input("interface>")
new_mac = input("mac>")
"""

def readmac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result_str = ifconfig_result.decode('utf-8')

    mac_adress_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result_str)
    if mac_adress_search_result:
        return mac_adress_search_result.group(0)
    else:
        print("[-] could not read the mac adress")

options=get_arguments()
current_mac=readmac(options.interface)
print("current Mac = "+str(current_mac))
changemac(options.interface,options.new_mac)
current_mac=readmac(options.interface)
if current_mac==options.new_mac:
    print("[+] MAC address was successfully changed to "+current_mac)
else:
    print("[+] MAC address did not  get changed ")

