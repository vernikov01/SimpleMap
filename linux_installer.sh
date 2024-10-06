#!/bin/bash
echo "Checking if Nmap has been installed.."
if ! command -v nmap &> /dev/null; then
    echo "Nmap is not installed. Installing..."
    sudo apt install nmap -y
else
    echo "Nmap is already installed."
fi

SHELL_SCRIPT_PATH="/usr/local/bin/smap"
sudo mkdir /etc/smap
sudo cp src/main.py /etc/smap
sudo cp src/helpmenu.py /etc/smap
sudo cp src/basics.py /etc/smap
sudo cp src/colours.py /etc/smap
sudo cp src/networkenum.py /etc/smap
sudo cp src/config.py /etc/smap
echo "#!/bin/bash" | sudo tee $SHELL_SCRIPT_PATH > /dev/null
echo "python3 /etc/smap/main.py \"\$@\"" | sudo tee -a $SHELL_SCRIPT_PATH > /dev/null
sudo chmod +x $SHELL_SCRIPT_PATH
echo "smap installed successfully. You can now use 'smap' to run the program."
