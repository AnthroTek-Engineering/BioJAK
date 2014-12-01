#!/bin/bash
say(){(cd /home/pi/tts/picopi/pico/tts && ./testtts "$*" |aplay --rate=16000 --channels=1 --format=S16_LE);}
say $*
