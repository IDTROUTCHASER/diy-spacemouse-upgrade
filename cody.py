import board
import busio
import adafruit_tlv493d
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import digitalio
import time

i2c = busio.I2C(board.SCL1, board.SDA1, frequency=100000)
sensor = adafruit_tlv493d.TLV493D(i2c)
mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)

button1 = digitalio.DigitalInOut(board.A2)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.SDA)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

cal_samples = 500
mag_range = 1000
out_range = 20
xy_threshold = 2000
in_range = mag_range * 8

x_offset = 0
y_offset = 0
z_offset = 0

print("Calibrating...")
for i in range(cal_samples):
    x, y, z = sensor.magnetic
    x_offset += x
    y_offset += y
    z_offset += z

x_offset /= cal_samples
y_offset /= cal_samples
z_offset /= cal_samples
print("Done")

btn1_last = True
btn2_last = True

while True:
    x, y, z = sensor.magnetic
    x_current = x - x_offset
    y_current = y - y_offset

    btn1_current = button1.value
    btn2_current = button2.value

    if not btn1_current and btn1_last:
        keyboard.press(Keycode.CONTROL, Keycode.LEFT_SHIFT, Keycode.H)
        time.sleep(0.01)
        keyboard.release_all()

    if not btn2_current and btn2_last:
        mouse.press(Mouse.MIDDLE_BUTTON)
        mouse.release(Mouse.MIDDLE_BUTTON)
        mouse.press(Mouse.MIDDLE_BUTTON)
        mouse.release(Mouse.MIDDLE_BUTTON)

    btn1_last = btn1_current
    btn2_last = btn2_current

    if abs(x_current) > xy_threshold or abs(y_current) > xy_threshold:
        x_move = int(max(-out_range, min(out_range, x_current / in_range * out_range)))
        y_move = int(max(-out_range, min(out_range, y_current / in_range * out_range)))

        mouse.press(Mouse.MIDDLE_BUTTON)
        mouse.move(x=-x_move, y=y_move)
    else:
        mouse.release(Mouse.MIDDLE_BUTTON)
        keyboard.release_all()

    time.sleep(0.02)
