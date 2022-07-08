#!/bin/bash

echo "Start listening on port 23..."
while read line
do
    if [ "$line" == 'exit' ] ; then
      echo "Received 'exit'"
      break
    elif [[ $line =~ 'S' ]] ; then
      echo "STOP"
      /usr/bin/python /home/pi/RS-B665_control/STOP.py
    elif [[ $line =~ 'F' ]] ; then
      echo "FF"
      /usr/bin/python /home/pi/RS-B665_control/FF.py
    elif [[ $line =~ 'R' ]] ; then
      echo "REW"
      /usr/bin/python /home/pi/RS-B665_control/REW.py
    elif [[ $line =~ 'P' ]] ; then
      echo "PLAY"
      /usr/bin/python /home/pi/RS-B665_control/PLAY.py
    fi

done < <((echo -e "RS-B665 control. Available commands: RPFS\r\n") | sudo nc -kltv 23) 
