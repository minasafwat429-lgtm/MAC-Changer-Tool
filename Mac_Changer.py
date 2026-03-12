<<<<<<< HEAD
import subprocess
import optparse
import re
#08:00:27:63:b0:05
#this is a reader that will take network interface and mac address
parser = optparse.OptionParser()
parser.add_option("-i", dest="network_interface")
parser.add_option("-m", dest="new_mac")
options, arguments =parser.parse_args()
#
#these are system command that will change the mac address for a network interface
subprocess.call("ifconfig " + options.network_interface + " down", shell=True)
subprocess.call("ifconfig " + options.network_interface + " hw ether " + options.new_mac, shell=True)
subprocess.call("ifconfig " + options.network_interface + " up", shell=True)
print("[+] Changing MAC Adress For " + options.network_interface + "to" + options.new_mac)

#Filtering mac address
ifconfig_result =subprocess.check_output("ifconfig eth0", shell=True).decode("UTF-8")
mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
=======
import subprocess
import optparse
import re
#08:00:27:63:b0:05
#this is a reader that will take network interface and mac address
parser = optparse.OptionParser()
parser.add_option("-i", dest="network_interface")
parser.add_option("-m", dest="new_mac")
options, arguments =parser.parse_args()
#
#these are system command that will change the mac address for a network interface
subprocess.call("ifconfig " + options.network_interface + " down", shell=True)
subprocess.call("ifconfig " + options.network_interface + " hw ether " + options.new_mac, shell=True)
subprocess.call("ifconfig " + options.network_interface + " up", shell=True)
print("[+] Changing MAC Adress For " + options.network_interface + "to" + options.new_mac)

#Filtering mac address
ifconfig_result =subprocess.check_output("ifconfig eth0", shell=True).decode("UTF-8")
mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
>>>>>>> 2f7227b027af854c9d52b48bcae97a9cbee65cb8
print(mac_address[0])