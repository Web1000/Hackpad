# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the encoder extension
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Define your button pins based on schematic
# SW1 is connected to GP0 (Pin 7)
# SW2 is connected to GP1 (Pin 8)
BUTTON_PINS = [
    board.GP0,  # SW1 - Left button
    board.GP1,  # SW2 - Right button
]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=BUTTON_PINS,
    value_when_pressed=False,
)

# Define your encoders based on actual schematic
# SW3 (Volume): A=GP26, B=GP29, C=GND
# SW4 (Brightness): A=GP28, B=GP27, C=GND
keyboard.encoders = [
    ((board.GP26, board.GP29, None, False),),  # SW3 - Volume encoder
    ((board.GP28, board.GP27, None, False),),  # SW4 - Brightness encoder
]

# Define encoder map
encoder_handler.map = [
    # Layer 0
    (
        (KC.VOLU, KC.VOLD),                          # Volume encoder: up/down
        (KC.BRIGHTNESS_UP, KC.BRIGHTNESS_DOWN),      # Brightness encoder: up/down
    ),
]

# Define the button keymap
keyboard.keymap = [
    [
        KC.LEFT,  # SW1 (Left button) - Play/Pause
        KC.RIGHT,              # SW2 (Right button) - Mute
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()