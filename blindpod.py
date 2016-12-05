import evdev
import feed
import stack


'''
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

kc = {82:stack.KEY_0, 79:stack.KEY_1, 80:stack.KEY_2, 81:stack.KEY_3, 75:stack.KEY_4, 76:stack.KEY_5, 77:stack.KEY_6, 71:stack.KEY_7, 72:stack.KEY_8, 73:stack.KEY_9,
    83:stack.KEY_DOT, 96:stack.KEY_ENTER, 78:stack.KEY_PLUS, 74:stack.KEY_MINUS, 55:stack.KEY_MULT, 98:stack.KEY_DIV, 69:stack.KEY_NUMLOCK}

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        if event.code in kc.keys():
            stack.key(kc[event.code])
'''
        print(evdev.categorize(event))
        print("type")
        print(event.type)
        print("code")
        print(event.code)
        print("value")
        print(event.value)
'''
