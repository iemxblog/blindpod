import evdev
import feed
import fsm


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

kc = {82:fsm.KEY_0, 79:fsm.KEY_1, 80:fsm.KEY_2, 81:fsm.KEY_3, 75:fsm.KEY_4, 76:fsm.KEY_5, 77:fsm.KEY_6, 71:fsm.KEY_7, 72:fsm.KEY_8, 73:fsm.KEY_9,
    83:fsm.KEY_DOT, 96:fsm.KEY_ENTER, 78:fsm.KEY_PLUS, 74:fsm.KEY_MINUS, 55:fsm.KEY_MULT, 98:fsm.KEY_DIV, 69:fsm.KEY_NUMLOCK}

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        if event.code in kc.keys() and event.value == 0:
            fsm.key(kc[event.code])
'''
        print(evdev.categorize(event))
        print("type")
        print(event.type)
        print("code")
        print(event.code)
        print("value")
        print(event.value)
'''
