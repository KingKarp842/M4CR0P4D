import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins=[
        board.D0,
        board.D1,
        board.D2,
        board.D3,
        board.D6,
        board.D7,
        board.D8,
        board.D9,
    ],
    value_when_pressed=False,
    pull=True,
)

keyboard.keymap = [[
    KC.LGUI(KC.C),
    KC.LGUI(KC.V),
    KC.F1,
    KC.LGUI(KC.L),
    KC.BSPC,
    KC.LGUI(KC.A),
    KC.LGUI(KC.T),
    KC.LGUI(KC.W),
]]

if __name__ == "__main__":
    keyboard.go()
