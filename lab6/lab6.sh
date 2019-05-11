#!/bin/bash
#for changing the current working directory into the home directory
V_MY_PATH=$HOME
echo $V_MY_PATH
ls $V_MY_PATH
#for reading MBR and writing into a file.
dd if=/dev/sda of=mbr.bin bs=512 count=1
od -xa mbr.bin
#for a new entry
sudo apt-get install grml-rescueboot
sudo mv ~/Downloads/ubuntu-18.04.2-desktop-amd64.iso /boot/grml/
sudo update-grub





