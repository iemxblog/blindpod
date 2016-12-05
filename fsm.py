from feed import *
import tts
from mpd import MPDClient
import time

KEY_0 = 0
KEY_1 = 1
KEY_2 = 2
KEY_3 = 3
KEY_4 = 4
KEY_5 = 5
KEY_6 = 6
KEY_7 = 7
KEY_8 = 8
KEY_9 = 9
KEY_DOT = 10
KEY_ENTER = 11
KEY_PLUS = 12
KEY_MINUS = 13
KEY_MULT = 14
KEY_DIV = 15
KEY_NUMLOCK = 16

CMD_UPDATE = 0
CMD_READTITLE = 1
CMD_DOWNLOAD = 2


subscriptions = [
    'http://radiofrance-podcast.net/podcast09/rss_11549.xml' # Sur les épaules de Darwin
    , 'http://radiofrance-podcast.net/podcast09/rss_13942.xml' # Si tu écoutes j'annule tout
    , 'http://feeds.feedburner.com/PodcastScience' # Podcast science
]

feeds = getFeeds(subscriptions)

state=0
cf=None                 # current feed
ce=None                 # current episode

client = MPDClient()
client.connect("localhost", 6600)


def key(k):
    global feeds, state, cf, ce, client
    try:
        if k == KEY_DIV:
            tts.say("Menu principal")
            state=0
            cf=None
            ce=None
            return

        if k == KEY_MULT:
            client.pause()
            return

        if k == KEY_ENTER and cf != None and ce != None:
            tts.say("Téléchargement du podcast")
            download(feeds, cf, ce)
            tts.say("Podcast téléchargé")
            client.stop()
            client.clear()
            client.update()
            time.sleep(1) # wait until update is finished (find a better solution with mpd library ?)
            print("podcast%d-%d.mp3" % (cf, ce))
            client.add("podcast%d-%d.mp3" % (cf, ce))
            time.sleep(5)
            print("play")
            client.play()
            return

        if k == KEY_DOT:
            tts.say("Mise à jour des podcasts")
            feeds = getFeeds(subscriptions)
            tts.say("Mise à jour effectuée")

        if state == 0:
            if k >=0  and k <= 9:
                cf=k
                tts.say(feedTitle(feeds, cf))
                state=1

        elif state == 1:
            if k>=0 and k<= 9:
                ce=k
                tts.say(episodeTitle(feeds, cf, ce))
    except IndexError:
        pass
