#!/bin/bash
# https://unix.stackexchange.com/questions/401759/automatically-login-on-debian-9-2-1-command-line #
mkdir -p /etc/systemd/system/getty@tty1.service.d
cat > /etc/systemd/system/getty@tty1.service.d/override.conf << EOF
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin root --noclear %I 38400 linux
EOF
cat >> .bashrc << EOF
clear
python3 pyboot.py
/sbin/shutdown now # https://linuxize.com/post/linux-shutdown-command/
EOF