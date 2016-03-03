# README #
This is the code we found worked best with the I2C 16x2 character display. 

Credit for the working code goes to "natbett" on the [Raspberry Pi Forums](http://www.raspberrypi.org/forums/viewtopic.php?f=32&t=34261&p=378524) & Michael Horne's Tutorial on the awesome [RasPi Pod](http://www.recantha.co.uk/blog/?p=4849)

To get going follow the instructions below. Automatic Setup should work perfectly fine on a new SD card. If not we recommend to use manual setup

# Automatic Setup #
```
git clone https://bitbucket.org/ryanteckltd/16x2-python-i2c-lib.git
cd 16*
sh LCDinstall.sh
```

Not tested for Raspbian Jan 31st.

# Manual Setup #
First install python-smbus using "sudo apt-get install python-smbus"

sudo nano /etc/modprobe.d/raspi-blacklist.conf # infront of i2c
sudo nano /etc/modules i2c-dev
sudo reboot
