import urllib2

def internet_on():
        try:
            response=urllib2.urlopen('http://74.125.228.100', timeout=1)
            return True
        except urllib2.URLError as err: pass
        return False



while True:
    if internet_on():
        print 'Connection Established...'
        break
