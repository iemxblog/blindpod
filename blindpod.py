import evdev
import feed

subscriptions = [
    'http://radiofrance-podcast.net/podcast09/rss_11549.xml' # Sur les épaules de Darwin
    , 'http://radiofrance-podcast.net/podcast09/rss_13942.xml' # Si tu écoutes j'annule tout
    , 'http://feeds.feedburner.com/PodcastScience' # Podcast science
]


print("Updating database")
feeds = feed.getFeeds(subscriptions)
print("Database updated.")

print(feed.feedTitle(feeds, 1))
print(feed.feedSubTitle(feeds, 1))
print(feed.episodeTitle(feeds, 1, 4))
print(feed.episodeSubTitle(feeds, 1, 4))
print(feed.duration(feeds, 1, 4))

#feed.download(feeds, 1, 4)

'''
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    print(device.fn, device.name, device.phys)
'''
device = evdev.InputDevice('/dev/input/event0')

'''
# print(device)
#print(device.leds(verbose=True))
'''

num_keycodes = {82:0, 79:1, 80:2, 81:3, 75:4, 76:5, 77:6, 71:7, 72:8, 73:9}

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        if event.code in num_keycodes.keys():
            feed.download(feeds, num_keycodes[event.code], 0)
        print(evdev.categorize(event))
        print("type")
        print(event.type)
        print("code")
        print(event.code)
        print("value")
        print(event.value)
