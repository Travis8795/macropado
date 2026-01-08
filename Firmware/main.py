import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.extensions.oled import OLED

# -------------------------
# Keyboard init
# -------------------------
keyboard = KMKKeyboard()

# -------------------------
# Matrix pins (3x3)
# -------------------------
keyboard.row_pins = (
    board.GP2,   # ROW1
    board.GP4,   # ROW2
    board.GP3,   # ROW3
)

keyboard.col_pins = (
    board.GP26,  # COL1
    board.GP27,  # COL2
    board.GP28,  # COL3 (encoder button)
)

keyboard.diode_orientation = keyboard.DIODE_COL2ROW

# -------------------------
# Keymap
# -------------------------
keyboard.keymap = [
    # Layer 0
    [
        KC.MPLY, KC.MPRV, KC.NO,
        KC.MNXT, KC.VOLU, KC.NO,
        KC.VOLD, KC.MUTE, KC.TG(1),  # Encoder button
    ],

    # Layer 1
    [
        KC.F1, KC.F2, KC.NO,
        KC.F3, KC.F4, KC.NO,
        KC.F5, KC.F6, KC.TG(0),
    ],
]

# -------------------------
# Encoder (rotation only)
# -------------------------
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.GP0, board.GP1),  # EnA, EnB
)

encoder.map = [
    ((KC.VOLD, KC.VOLU),),     # Layer 0
    ((KC.LEFT, KC.RIGHT),),   # Layer 1
]

# -------------------------
# RGB (WS2812)
# -------------------------
rgb = RGB(
    pixel_pin=board.GP29,
    num_pixels=8,
    val=60,
    sat=255,
)
keyboard.extensions.append(rgb)

# -------------------------
# OLED (SSD1306 I2C)
# -------------------------
i2c = busio.I2C(
    scl=board.GP7,
    sda=board.GP6
)

oled = OLED(
    i2c=i2c,
    width=128,
    height=32,
)
keyboard.extensions.append(oled)

def oled_task(oled, keyboard):
    oled.clear()
    oled.text("MacroPado", 0, 0)
    oled.text(f"Layer: {keyboard.active_layers[0]}", 0, 12)
    oled.show()

oled.after_update = oled_task

# -------------------------
# Start
# -------------------------
if __name__ == '__main__':
    keyboard.go()
