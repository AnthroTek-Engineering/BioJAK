import os, time, urllib2

piCamParams =  "-o - -t 0 -w 1280 -h 720 -fps 25 -b 2000000 -g 50 -vf"
streamKey   = "John.A.Hogg.zp33-jg8t-h0jp-ar4g"

def internet_on():
        try:
            response=urllib2.urlopen('http://74.125.228.100', timeout=1)
            return True
        except urllib2.URLError as err: pass
        return False

def bioJAK_video(piCamParams, streamKey):
    while True:
        if internet_on():
            os.system("(cd /home/pi/bin/arm/bin && raspivid " + piCamParams + " | ./ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/" + streamKey + ") &")
            break

        
bioJAK_video(piCamParams, streamKey)
