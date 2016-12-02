import feedparser
import urllib.request

def getFeeds(subscriptions):
    feeds = [feedparser.parse(s) for s in subscriptions]
    return feeds


def feedTitle(feeds, n):
    return feeds[n]['feed']['title']

def feedSubTitle(feeds, n):
    return feeds[n]['feed']['subtitle']

def episodeTitle(feeds, n, i):
    return feeds[n].entries[i]['title']

def episodeSubTitle(feeds, n, i):
    return feeds[n].entries[i]['subtitle']

def audiolink(feeds, n, i):
    return[di['href'] for di in feeds[n].entries[i].links if di['rel'] == 'enclosure'][0]

def duration(feeds, n, i):
    return feeds[n].entries[i]['itunes_duration']

def download(feeds, n, i):
    podfile = audiolink(feeds, n, i)
    print("Downloading file")

    def reportHook(count, blockSize, totalSize):
        print(count, blockSize, totalSize)

    testfile = urllib.request.urlretrieve(podfile, "/tmp/podcast%d-%d.mp3" % (n, i) , reportHook)
    print("File downloaded.")

