import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

def on_numpad_dot(event):
    if event.event_type == keyboard.KEY_DOWN:
        mouse.click(Button.right)

def main():
    # The key name for the numpad decimal is usually 'decimal'
    keyboard.hook_key('decimal', on_numpad_dot)
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
