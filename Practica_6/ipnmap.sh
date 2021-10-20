#!/bin/bash

x= curl ifconfig.me
echo "Mi IP"
echo x

y= nmap 192.168.215.1
echo NMAP A MI IP
echo y

z= nmap facebook.com
echo NMAP A FACEBOOK
echo z
 
w= nmap --script all 192.168.215.1
echo NMAP CON UN SCRIPT
echo w
