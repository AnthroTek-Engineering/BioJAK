#!/bin/bash

cd /home/pi/BioJAK/proto_v1.1/

python networkTest.py

./googlet2s.sh 'Bye o Jak Online'

./googlet2s.sh 'Uploading User File'

sleep 1

python userIdGen.py

sleep 1

./googlet2s.sh 'Starting Environmental Sensors'
python arduinoSource.py &

sleep 1

./googlet2s.sh 'Enabling global positioning systems'
python gpsSource.py &

sleep 1

./googlet2s.sh 'Starting Heart Rate Monitor'
python hrmSource.py &

sleep 1

./googlet2s.sh 'Enabling Ant Reciever'

sleep 1

./googlet2s.sh 'Waiting for Heart Rate Events'

sleep 1

./googlet2s.sh 'Preparing live stream camera'

sleep 1

./googlet2s.sh 'Uploading Video Stream'
python videoSource.py &

sleep 1

./googlet2s.sh 'Connected To Server and Transmitting Data'

sleep 1

./googlet2s.sh 'System Fully online and ready'
