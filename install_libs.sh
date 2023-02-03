#!/bin/bash
# By Pytel

python3 -m pip install --upgrade pip
if [ -f dependencies.txt ]; then 
    pip install -r dependencies.txt
fi

exit 0
#END