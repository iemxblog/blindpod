from espeak import espeak

def say(msg):
    print(msg)
    espeak.set_voice("fr")
    espeak.synth(msg)
    
