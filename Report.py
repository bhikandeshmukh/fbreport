#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time

# Check if the .Akun/.Bahan file exists
if os.path.exists(".Akun/.Bahan"):
    print("[>] Installing dependencies...\n")
    time.sleep(2)
    os.system("bash .Akun/.Bahan")
    os.system("pip3 install --upgrade pip")
    os.system("rm .Akun/.Bahan")

# Run the main script
try:
    os.system("python3 .Akun/.Rt")
except ImportError:
    sys.exit()