import sys
import serial
import os
import time
from Pubnub import Pubnub


def bioJAK_arduino(pubnub, ser, channel_1, channel_2, channel_3, channel_4):

    while True:

        dataArray = ser.readline().split(",")

        if len(dataArray) == 10:
            
            temps = ({'intemp':dataArray[0],'extemp':dataArray[1]})
            humid = ({'inhum':dataArray[2],'exhum':dataArray[3]})
            impac = ({'impact':dataArray[4],'freefall':dataArray[5],'inact':dataArray[6]})
            rawAccel=({'x':dataArray[7],'y':dataArray[8],'z':dataArray[9],})

            pubnub.publish(channel_1, impac)
            pubnub.publish(channel_2, temps)
            pubnub.publish(channel_3, humid)
            pubnub.publish(channel_4, rawAccel)


if os.path.exists('/dev/ttyACM1'):
    ser = serial.Serial('/dev/ttyACM1', 9600)
else:
    ser = serial.Serial('/dev/ttyACM0', 9600)

publish_key   = 'pub-c-ea55afd0-74eb-4ed4-9f56-4cd96bb87b0a'
subscribe_key = 'sub-c-55cf6ccc-4585-11e4-8772-02ee2ddab7fe'
secret_key    = 'demo'
cipher_key    =  ''
ssl_on        = False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)

channel_1 = 'impact_channel'
channel_2 = 'temp_channel'
channel_3 = 'humidity_channel'
channel_4 = 'rawAccel_channel'

bioJAK_arduino(pubnub, ser, channel_1, channel_2, channel_3, channel_4)



        
    

    


