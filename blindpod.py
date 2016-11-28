import evdev
import feed

subscriptions = [
    'http://radiofrance-podcast.net/podcast09/rss_11549.xml' # Sur les épaules de Darwin
    , 'http://radiofrance-podcast.net/podcast09/rss_13942.xml' # Si tu écoutes j'annule tout
]


print("Updating database")
feeds = feed.getFeeds(subscriptions)
print("Database updated.")




feed.download(feeds, 1, 4)
'''
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    print(device.fn, device.name, device.phys)

device = evdev.InputDevice('/dev/input/event0')
print(device)

print(device.leds(verbose=True))

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
        print("type")
        print(event.type)
        print("code")
        print(event.code)
        print("value")
        print(event.value)
'''
