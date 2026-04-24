import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)

media = MediaKeys()
keyboard.extensions.append(media)

keyboard.matrix = KeysScanner(
    pins=[
        board.D1,   # SW1
        board.D2,   # SW2
        board.D3,   # SW3
        board.D4,   # SW4
        board.D7,   # SW5
        board.D8,   # SW6
        board.D9,   # SW7
        board.D10,  # SW8
    ],
    value_when_pressed=False,
    pull=True,
)

keyboard.keymap = [
    [  # Layer 0
        KC.COPY,
        KC.PASTE,
        KC.CUT,
        KC.UNDO,
        KC.REDO,
        KC.MUTE,
        KC.VOLU,
        KC.MO(1),
    ],
    [  # Layer 1
        KC.F1,
        KC.F2,
        KC.F3,
        KC.F4,
        KC.F5,
        KC.F6,
        KC.F7,
        KC.TRNS,
    ],
]

if __name__ == '__main__':
    keyboard.go()
