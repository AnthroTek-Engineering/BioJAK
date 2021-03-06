import sys, time, math, serial
from ant.core import driver, node, event, message, log
from ant.core.constants import CHANNEL_TYPE_TWOWAY_RECEIVE, TIMEOUT_NEVER
from Pubnub import Pubnub


publish_key   = 'pub-c-ea55afd0-74eb-4ed4-9f56-4cd96bb87b0a'
subscribe_key = 'sub-c-55cf6ccc-4585-11e4-8772-02ee2ddab7fe'
secret_key    = 'demo'
cipher_key    =  ''
ssl_on        = False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)

HR = "0"

class HRM(event.EventCallback):
    
    global pubnub
    global HR

    def __init__(self, serial, netkey):
        self.serial = serial
        self.netkey = netkey
        self.antnode = None
        self.channel = None
        

    def start(self):
        print("starting Ant Reciever")
        self._start_antnode()
        self._setup_channel()
        self.channel.registerCallback(self)
        print("Heart Rate Sensor Online")

    def stop(self):
        print("Closing Channel")
        if self.channel:
            self.channel.close()
            self.channel.unassign()
        if self.antnode:
            self.antnode.stop()

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        self.stop()

    def _start_antnode(self):
        stick = driver.USB2Driver(self.serial)
        self.antnode = node.Node(stick)
        self.antnode.start()

    def _setup_channel(self):
        key = node.NetworkKey('N:ANT+', self.netkey)
        self.antnode.setNetworkKey(0, key)
        self.channel = self.antnode.getFreeChannel()
        self.channel.name = 'C:HRM'
        self.channel.assign('N:ANT+', CHANNEL_TYPE_TWOWAY_RECEIVE)
        self.channel.setID(120, 0, 0)
        self.channel.setSearchTimeout(TIMEOUT_NEVER)
        self.channel.setPeriod(8070)
        self.channel.setFrequency(57)
        self.channel.open()

    def process(self, msg):
        global HR
        if isinstance(msg, message.ChannelBroadcastDataMessage):
            HR = str((format(ord(msg.payload[-1]))))
	

SERIAL = '/dev/ttyUSB0'
NETKEY = 'B9A521FBBD72C345'.decode('hex')

with HRM(serial=SERIAL, netkey=NETKEY) as hrm:
    hrm.start()
    while True:
        try:
            pubnub.publish('hr_channel',HR)
            time.sleep(1)
        except KeyboardInterrupt:
            hrm.stop()
            sys.exit(0)           

