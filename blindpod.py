import feedparser
import urllib.request

subscriptions = [
    'http://radiofrance-podcast.net/podcast09/rss_11549.xml' # Sur les épaules de Darwin
    , 'http://radiofrance-podcast.net/podcast09/rss_13942.xml' # Si tu écoutes j'annule tout
]

print("Updating database")
feeds = [feedparser.parse(s) for s in subscriptions]
print("Database updated.")


def download(n, i):
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


download(1, 4)
