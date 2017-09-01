# /usr/bin/python

import netifaces
import subprocess

print (netifaces.interfaces())

def_gw_device = netifaces.gateways()['default'][netifaces.AF_INET][1]
print def_gw_device
myargs = "sudo wondershaper {} 10000 1024".format(def_gw_device)
ll = subprocess.Popen(["echo pmc | {}".format(myargs)],stdout=subprocess.PIPE,shell=True)
ll.communicate()