#!/bin/bash

if [ ! -d "facemaskswap-env" ]
then
    python3 -m venv "facemaskswap-env"  # "env" is the name of the environment here.
    source facemaskswap-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r ../requirements.txt
    python -m pip install opencv-contrib-python
    python -m pip install opencv-python
else
    source facemaskswap-env/bin/activate
fi

python main.py --src imgs/test6.jpg --dst imgs/test7.jpg --out results/output6_7.jpg --correct_color