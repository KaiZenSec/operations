#!/bin/bash
#https://miloserdov.org/?p=337
iw reg set BZ
ip link set wlan0 down
iw dev wlan0 set txpower fixed 30mBm
ip link set wlan0 up
iw dev
