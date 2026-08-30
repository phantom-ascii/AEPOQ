import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

# Initialize Keyboard
keyboard = KMKKeyboard()

# Hardware Pin Mapping (Extracted from KiCad Schematic)
keyboard.col_pins = (
    board.GP0,  # Col 1
    board.GP1,  # Col 2
    board.GP2,  # Col 3
    board.GP3,  # Col 4
    board.GP4,  # Col 5
    board.GP5,  # Col 6
    board.GP6,  # Col 7
    board.GP7,  # Col 8
    board.GP8,  # Col 9
    board.GP9,  # Col 10
    board.GP10, # Col 11
    board.GP11, # Col 12
    board.GP12, # Col 13
    board.GP13, # Col 14
    board.GP14, # Col 15
)

keyboard.row_pins = (
    board.GP15, # Row 1
    board.GP16, # Row 2
    board.GP17, # Row 3
    board.GP18, # Row 4
    board.GP19, # Row 5
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Add Media Keys Extension
media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

# Initialize 0.91" I2C OLED Display (128x32)
displayio.release_displays()
i2c = busio.I2C(scl=board.GP27, sda=board.GP26)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Volume State Tracker
volume_level = 50  # Initial UI volume tracking percentage
is_muted = False

def update_oled():
    display.fill(0)
    if is_muted:
        text = "  [ MUTED ]"
        bar = "----------------"
    else:
        text = f" Volume: {volume_level}%"
        # Render dynamic visual progress bar
        bars_filled = int((volume_level / 100) * 14)
        bar = "[" + "=" * bars_filled + " " * (14 - bars_filled) + "]"

    display.text("=== 65% KEYBOARD ===", 0, 0, 1)
    display.text(text, 0, 12, 1)
    display.text(bar, 0, 24, 1)
    display.show()

# Render initial screen
update_oled()

# Custom Encoder Actions with OLED Callback
def volume_up(state):
    global volume_level, is_muted
    is_muted = False
    volume_level = min(100, volume_level + 5)
    keyboard.tap_key(KC.AUDIO_VOL_UP)
    update_oled()

def volume_down(state):
    global volume_level, is_muted
    is_muted = False
    volume_level = max(0, volume_level - 5)
    keyboard.tap_key(KC.AUDIO_VOL_DOWN)
    update_oled()

def toggle_mute(state):
    global is_muted
    is_muted = not is_muted
    keyboard.tap_key(KC.AUDIO_MUTE)
    update_oled()

# Configure Rotary Encoder (GPIO20 = A, GPIO21 = B, GPIO22 = S1 Switch)
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP20, board.GP21, board.GP22, False),)
encoder_handler.map = [
    ((volume_up, volume_down, toggle_mute),),
]
keyboard.modules.append(encoder_handler)

# 65% Keymap Layout
keyboard.keymap = [
    [
        # Row 1 (Esc to Ins)
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.INS,
        # Row 2 (Tab to Del)
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL,
        # Row 3 (Caps to PgUp)
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.PGUP,
        # Row 4 (Shift to PgDn)
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.PGDN,
        # Row 5 (Ctrl to Right)
        KC.LCTL, KC.LGUI, KC.LALT,                   KC.SPC,                    KC.RALT, KC.FN,   KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT,
    ]
]

if __name__ == "__main__":
    keyboard.go()