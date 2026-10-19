from pynput import keyboard

# Recorder.py:
# Records and saves all keys using pynput

word = []

def on_press(key):
    global word
    try:
        # handle normal characters
        word.append(key.char)
    except AttributeError:
        # Handle special keys (like Space, Enter, Backspace)
        if key == keyboard.Key.space:
            # Returning False here stops the listener immediately on press
            return False 

def GetWord():
    global word
    word = []
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        
    return "".join(word)

def Replace(replacement:str):
    with keyboard.Controller.pressed(keyboard.Key.ctrl):
        keyboard.Controller.press(keyboard.Key.backspace)
        keyboard.Controller.release(keyboard.Key.backspace)

    keyboard.Controller.type(replacement)