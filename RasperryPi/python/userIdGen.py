import sys, os, time, json
from Pubnub import Pubnub

def userFileGen(name, rHR, phNum, usrNum):
    userFile = ({'name':name,'RHR':rHR,'phNum':phNum,'usrNum':usrNum})
    print('User file created...')
    return userFile

publish_key   = 'pub-c-ea55afd0-74eb-4ed4-9f56-4cd96bb87b0a'
subscribe_key = 'sub-c-55cf6ccc-4585-11e4-8772-02ee2ddab7fe'
secret_key    = 'demo'
cipher_key    =  ''
ssl_on        = False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)

userFile = open('userFile')
userData = userFile.read()

name = userData.split(',')[0]
rHR = userData.split(',')[1]
phNum = userData.split(',')[2]
usrNum = userData.split(',')[3]

usrJson = userFileGen(name,rHR,phNum,usrNum)

pubnub.publish('usrid_channel', usrJson)

os.system('./googlet2s.sh User Name ' + name )
os.system('./googlet2s.sh resting heart rate ' + rHR)

print('User File Uploaded...')


