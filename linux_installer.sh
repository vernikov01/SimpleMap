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
sudo cp src2/smap.py /etc/smap
sudo cp src2/help.py /etc/smap
sudo cp src2/map.py /etc/smap
sudo cp src2/colours.py /etc/smap
sudo cp src2/commands.py /etc/smap
sudo cp src2/config.py /etc/smap
echo "#!/bin/bash" | sudo tee $SHELL_SCRIPT_PATH > /dev/null
echo "python3 /etc/smap/smap.py \"\$@\"" | sudo tee -a $SHELL_SCRIPT_PATH > /dev/null
sudo chmod +x $SHELL_SCRIPT_PATH
echo "smap installed successfully. You can now use 'smap' to run the program."
