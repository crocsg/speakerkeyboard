import os
import platform
import threading
import options
import keyboard
import queue
from espeakng import ESpeakNG

flagspeak = False
flagdown = False
speakmutex = threading.Lock()
esng = ESpeakNG()
kevent = queue.Queue()

def voice_func ():
    esng.voice = options.get_voice ()
    esng.speed = options.get_speed ()
    esng.volume = options.get_volume ()
    esng.say('bonjour')
    print ("thread started")
    #wait queue data
    while True:
        try:
            
            d = kevent.get(block=True, timeout=5)
            process_key(str(d))
            print ("thread", d)
            
        except queue.Empty:
            print ("queue empty")
            
        # except Exception as e:
        #     print ("process error", e)
        #     print (e)

def process_key (scan_code):
    global flagspeak
    
    if speakmutex.acquire(blocking=False):
        flagspeak = True
        msg = options.get_messages()
        if scan_code in msg:
            text = msg[scan_code]
            
            print ("debut", text)
            esng.say (text, sync=options.get_sync())
            print ("fin")

        speakmutex.release()
    else:
        print ("locked")

def onKey (event):
    global flagdown
    if event.event_type == keyboard.KEY_DOWN:
        if flagdown == False: # avoid repeating keydown events
            flagdown = True
            msg = options.get_messages()
            print ("event ", event.name, event.scan_code)
            kevent.put (event.scan_code)
            if str(event.scan_code) in msg:
                process_key (str(event.scan_code))
            else:
                print ("Key event", event.scan_code, event.event_type, event.device, event)

    elif event.event_type == keyboard.KEY_UP:
        if flagdown == True: # avoid repeating keyup events
            print ("Key event", event.scan_code, event.event_type, event.device, event)
            flagdown = False



def main ():
    options.load_options()

    v = threading.Thread(target=voice_func)
    v.start()

    keyboard.hook (onKey)

    while (1):
        evt = keyboard.read_event ()
        onKey (evt)

if __name__ == "__main__":
    main ()
