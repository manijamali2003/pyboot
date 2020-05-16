# In the name of God, the Compassionate, the Merciful
# PyBoot (c) 2020 Mani Jamali. Free Software Lesser General Public License v3.0

import shutil, os, sys

## Check installer script ##
if os.path.isfile ('install.py'):
	print ("Runing installer script ...")
	os.system("\""+sys.executable + "\" install.py")
	os.system('/sbin/reboot')

## Check boot script ##
if not os.path.isdir ("stor"):
	input ("Fatal: Cannot find clouding system storage! Press Enter key to shutdown.")
	exit()

if not os.path.isdir ("stor/boot"):
	input ("Fatal: Cannot find boot directory! Press Enter key to shutdown.")
	exit()

if not os.path.isfile ("stor/boot/pyboot"):
	input ("Fatal: Cannot find boot script! Press Enter key to shutdown.")
	exit()

## Find kernel path and name ##

file = open ("stor/boot/pyboot")
kernel = file.read()
file.close()


print ("Runing "+kernel+" Python kernel ...")
os.system ("cd stor && \""+sys.executable+"\" "+kernel)
