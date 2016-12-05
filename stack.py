from feed import *
import tts

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

class StackError(Exception):
    pass

class Stack():
    def __init__(self):
        self._stack = []

    def push(self, i):
        self._stack.append(i)

    def pop(self):
        return self._stack.pop()

    def clear(self):
        self._stack = []

    def peek(self, i):
        return self._stack[i]

s = Stack()
r = 0

subscriptions = [
    'http://radiofrance-podcast.net/podcast09/rss_11549.xml' # Sur les épaules de Darwin
    , 'http://radiofrance-podcast.net/podcast09/rss_13942.xml' # Si tu écoutes j'annule tout
    , 'http://feeds.feedburner.com/PodcastScience' # Podcast science
]

feeds = {}


def runCommand():
    global feeds
    try:
        print("runCommand")
        c = s.pop()
        if c == CMD_UPDATE:
            tts.say("Mise à jour")
            feeds = getFeeds(subscriptions)
        elif c == CMD_READTITLE:
            i, n = s.peek(0), s.peek(1)
            tts.say(episodeTitle(feeds, n, i) + " " + episodeSubTitle(feeds, n, i))

    except IndexError:
        tts.say("Erreur")
        
def isDigit(k):
    return k>0 and k<9

def key(k):
    global r
    if isDigit(k):
        r = r*10 + k
    elif k == KEY_DOT:
        s.push(r)
        r=0
    elif k == KEY_MINUS:
        s.pop()
    elif k == KEY_DIV:
        s.clear()
    elif k == KEY_ENTER:
        runCommand()

