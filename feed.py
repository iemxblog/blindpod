import feedparser
import urllib.request

def getFeeds(subscriptions):
    feeds = [feedparser.parse(s) for s in subscriptions]
    return feeds


def download(feeds, n, i):
    print('Titre : ')
    print(feeds[n]['feed']['title'])

    print('Sous titre ')
    print(feeds[n]['feed']['subtitle'])

    print('Nombre d\'épisodes :')
    print(len(feeds[n]['entries']))

    print('Episode n°%d :' % i)
    print(feeds[n].entries[i]['title'])
    print(feeds[n].entries[i]['subtitle'])

    podfile = [di['href'] for di in feeds[n].entries[i].links if di['rel'] == 'enclosure'][0]



    print("Downloading file")

    def reportHook(count, blockSize, totalSize):
        print(count, blockSize, totalSize)

    testfile = urllib.request.urlretrieve(podfile, "/tmp/podcast%d-%d.mp3" % (n, i) , reportHook)
    print("File downloaded.")

