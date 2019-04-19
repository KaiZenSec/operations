#!/bin/bash
#https://askubuntu.com/questions/453110/rtl8187-wireless-card-drops-signal-within-seconds
iwconfig wlan0 rate 18M AUTO
iwconfig wlan0 frag 256
iwconfig wlan0 rts 256
iwconfig wlan0 retry short 21
iwconfig wlan0 retry long 21
