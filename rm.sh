#!/bin/bash

# Creator : Raunak Raj
# Note: This script only works for RoyalManager. So , don't try to use it for another software.


function requirements(){
    apt install python-tkinter
    pip install tk
    pip install Pillow
}

if [[ $1 == "-ir" ]]
then
    echo -e '\e[1;36m [*]installing requirements for RoyalManager... \e[0m'
    echo -e '\033[0;33m'
    requirements
    echo -e ''
    echo -e '\e[1;32m [*]requirements are installed... \e[0m'
    echo -e ''
elif [[ $1 == "" ]]
then
    clear
    echo -e '\e[1;36m [*]starting RoyalManager.... \e[0m'
    echo -e '\033[0;33m'
    python main.py
else
    echo -e ''
    echo -e '\e[31m [!]Invalid arguments... \e[0m'
    echo -e ''
    exit
fi
