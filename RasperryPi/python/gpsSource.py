import json
import gps, time, os
from Pubnub import Pubnub

def bioJAK_GPS(pubnub, channel):

    os.system('sudo killall gpsd')
    
    if os.path.exists('/dev/ttyUSB1'):
        os.system('sudo gpsd /dev/ttyUSB1 -F /var/run/gpsd.sock')
    else:
        os.system('sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock')
        
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
    while True:
        try:
            report = session.next()
            if report['class'] == 'TPV':
                if hasattr(report, 'lat'):
                    lat = str(report.lat)
                else:
                    lat = 'Waiting...'
                    
                if hasattr(report, 'lon'):
                    lon = str(report.lon)
                else:
                    lon = 'Waiting...'
                    
                if hasattr(report, 'alt'):
                    alt = str(report.alt)
                else:
                    alt = 'Waiting...'
                    
                if hasattr(report, 'epx'):
                    latErr = str(report.epx)
                else:
                    latErr = 'Waiting...'
                    
                if hasattr(report, 'epy'):
                    lonErr = str(report.epy)
                else:
                    lonErr = 'Waiting...'
                    
                if hasattr(report, 'epv'):
                    altErr = str(report.epv)
                else:
                    altErr = 'Waiting...'
                    
                if hasattr(report, 'climb'):
                    climb = str(report.climb)
                else:
                    climb = 'Waiting..'
                    
                if hasattr(report, 'mode'):
                    mode = str(report.mode)
                else:
                    mode = 'Waiting...'
                    
                if hasattr(report, 'speed'):
                    speed = str(report.speed)
                else:
                    speed = 'Waiting...'

                if hasattr(report, 'track'):
                    head = str(report.track)
                else:
                    head = 'Waiting...'

                if hasattr(report, 'eps'):
                    spErr = str(report.eps)
                else:
                    spErr = 'Waiting...'
                    
                gpsData = ({'lat':lat,
                                'long':lon,
                                'alt':alt,
                                'latErr':latErr,
                                'lonErr':lonErr,
                                'altErr':altErr,
                                'climb':climb,
                                'mode':mode,
                                'speed':speed,
                                'head':head,
                                'spErr':spErr})
                
                pubnub.publish(channel, gpsData)

        except KeyboardInterrupt:
            quit()





publish_key   = 'pub-c-ea55afd0-74eb-4ed4-9f56-4cd96bb87b0a'
subscribe_key = 'sub-c-55cf6ccc-4585-11e4-8772-02ee2ddab7fe'
secret_key    = 'demo'
cipher_key    =  ''
ssl_on        = False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)

channel = 'gps_channel'

bioJAK_GPS(pubnub, channel)



