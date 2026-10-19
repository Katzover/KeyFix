from pynput import keyboard

# Recorder.py:
# Records and saves all keys using pynput

word = []
nonAlphaCount = 0 # try to account for characters like , and . that block the ctrl + backspace meathod.
STOPS = [keyboard.Key.space, keyboard.Key.enter, keyboard.Key.down, keyboard.Key.up, keyboard.Key.left, keyboard.Key.right, keyboard.Key.tab] # list of keys that will trigger the word to reset.
replacement_pending = False
listener = None


def _send_ctrl_z():
    controller = keyboard.Controller()
    with controller.pressed(keyboard.Key.ctrl):
        controller.tap(keyboard.KeyCode.from_char("z"))

def on_press(key):
    global word
    global nonAlphaCount
    global replacement_pending

    if replacement_pending:
        replacement_pending = False
        if key == keyboard.Key.backspace:
            _send_ctrl_z()
            return

    try:
        # handle normal characters
        if not ord(key.char) < 32: word.append(key.char)
        else:
            print('reset')
            return False

        if not str(key.char).isalpha(): nonAlphaCount += 2
    except AttributeError:
        # Handle special keys (like Space, Enter, Backspace)
        if key == keyboard.Key.backspace and word: word.pop() # remove last item if backspace is pressed.
        if key in STOPS:
            print('reset')
            # Returning False here stops the listener immediately on press
            return False 
    print(word)

def _start_listener():
    global word
    global nonAlphaCount
    global listener

    word = []
    nonAlphaCount = 0
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def GetWord():
    global listener

    if listener is None:
        _start_listener()

    listener.join()
    listener = None
    return "".join(word)

def Replace(replacement:str=""):
    global nonAlphaCount
    global replacement_pending

    controller = keyboard.Controller()
    while True:
        with controller.pressed(keyboard.Key.ctrl):
            controller.tap(keyboard.Key.backspace)

        if not nonAlphaCount:
            break
        nonAlphaCount -= 1

    nonAlphaCount = 0
    replacement_pending = bool(replacement)
    if replacement:
        controller.type(replacement + " ")
        _start_listener()
