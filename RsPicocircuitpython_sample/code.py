import board
import busio
import displayio
import digitalio
import adafruit_imageload
from gc9a01 import GC9A01
import neopixel

Neopix = neopixel.NeoPixel(board.GP6, 1)
Neopix[0] = (128, 0, 63)

led = digitalio.DigitalInOut(board.GP10)
led.direction = digitalio.Direction.OUTPUT
led.value = True

displayio.release_displays()

sclk = board.GP18
mosi = board.GP19
spi = busio.SPI(sclk, MOSI=mosi, MISO=None)

while not spi.try_lock():
    pass
spi.configure(baudrate=24000000)
spi.unlock()
cs = board.GP13
dc = board.GP11
reset = board.GP12

display_bus = displayio.FourWire(spi, command=dc, chip_select=cs, reset=reset)
display = GC9A01(display_bus, width=240, height=240)

image, palette = adafruit_imageload.load(
    "image/test.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette
)
tile_grid = displayio.TileGrid(image, pixel_shader=palette)

group = displayio.Group()
group.append(tile_grid)
display.show(group)

while True:
    pass
