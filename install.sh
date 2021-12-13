#!/bin/bash

## Use sudo when installing to avoid 'permission denied' error
rm /usr/bin/emjl /usr/bin/gramatica.py
ln ./gramatica.py /usr/bin/gramatica.py
ln ./main.py /usr/bin/emjl
chmod +x /usr/bin/emjl

echo "Do not remove any files or move the github repo."

echo "To uninstall use 'sudo sh uninstall.sh'"