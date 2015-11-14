#!/bin/bash
pingip='192.168.1.1'

#/bin/ping -c 1 -I wlan0 $pingip > /dev/null 2> /dev/null
if `/sbin/ifconfig wlan0 | grep -q "inet addr:"` ; then
  echo "up"
else
  echo "down"
  /sbin/ifup wlan0
fi
