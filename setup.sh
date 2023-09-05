#bin/python3
clear
if ! command -v python3 &> /dev/null; then
echo " [!] PYTHON IS NOT INSTALLED"
echo " [=] INSTALLING PYTHON ..."
echo
pkg install -y python
echo " [✓] PYTHON INSTALLED"
else
echo " [✓] REQUIRED PACKAGE FOUND"
fi

pip3 install requests
