from espeak import espeak
from mpd import MPDClient
def say(msg):
    client = MPDClient()
    client.connect("localhost", 6600)
    s = client.status()['state']
    if s == 'play':
        client.pause()
    client.close()
    client.disconnect()
    print(msg)
    espeak.set_voice("fr")
    espeak.synth(msg)
    
