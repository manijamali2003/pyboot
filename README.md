# PyBoot : Booting Python kernel in computer

In the name of God, the Compassionate, the Merciful

PyBoot &copy; 2020 Mani Jamali. Free Software GNU Lesser General Public License v3.0

 - How to install PyBoot in linux
 - How to run Python kernel on PyBoot
 
## How to install PyBoot in linux and Run Python kernel on it

 - Install Debian 10 without any desktop (only install system utils)
 - Run Debian 10 without any desktop as root user
 - Git PyBoot from github:
 
 ```shell script
 git clone https://github.com/manijamali2003/pyboot
```

 - Copy all files in git source to **/root** directory:
 
 ```shell script
 cp -v /root/pyboot/* /root
```
 
 - Create Boot directories
 
 ```shell script
 mkdir -p /root/stor/boot
```
 
 - Write your simple kernel written in Python (location: /root/stor/kernel.py)
 
 ```python
# This my tiny kernel written in Python
import sys

## Stop in prompt ##
def kstop ():
    input ("Press enter key to shutdown.")

## Kernel entry ##
def kmain (args):
    print ("Welcome to my Python kernel!")
    kstop()

if __name__ == '__main__':
    kmain(sys.argv)
```
 - Set default kernel in /root/stor/kernel.py
 
 ```shell script
echo kernel.py > /root/stor/boot/pyboot
```

 - Run install.sh then reboot the system
 
 ```shell script
chmod +x install.sh
./install.sh
reboot
```
  - After installaction of PyBoot you can see your python kernel!