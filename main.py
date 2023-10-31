def on_button_pressed_a():
    global test, positie
    for index in range(256):
        test = index
        if int(test / 16) % 2 != 0:
            positie = 16 - (test - int(test / 16) * 16) + (16 + int(test / 16) * 16 - 16) - 1
        else:
            positie = test
        strip.set_pixel_color(positie, neopixel.colors(NeoPixelColors.YELLOW))
        strip.show()
        basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    ScrollUp("................................................................222.222.2.2.22222....2.2.2...2.22.2...2.2.2....22222.2.2.22..2.22.2...2.2.2.2......2.2.2.2...2.22.2.222.222.2222................................................................................")
    basic.pause(1000)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def MaakSprite(tekst: str):
    global lengte, positie, positiepixel
    if 20 < len(tekst):
        lengte = 255
        positie = 0
    else:
        lengte = 15
        positie = parse_float(tekst.substr(16, 2))
    index2 = 0
    while index2 <= lengte:
        if int(index2 / 16) % 2 != 0:
            positiepixel = 16 - (index2 - int(index2 / 16) * 16) + (16 + int(index2 / 16) * 16 - 16) - 1
        else:
            positiepixel = 16 * positie + index2
        if tekst.substr(index2, 1) == ".":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.BLACK))
        elif tekst.substr(index2, 1) == "1":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.WHITE))
        elif tekst.substr(index2, 1) == "2":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.RED))
        elif tekst.substr(index2, 1) == "3":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.BLUE))
        elif tekst.substr(index2, 1) == "4":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.ORANGE))
        elif tekst.substr(index2, 1) == "5":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.YELLOW))
        elif tekst.substr(index2, 1) == "6":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.BLUE))
        elif tekst.substr(index2, 1) == "7":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.GREEN))
        elif tekst.substr(index2, 1) == "8":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.BLUE))
        elif tekst.substr(index2, 1) == "9":
            strip.set_pixel_color(positiepixel, neopixel.colors(NeoPixelColors.BLUE))
        elif tekst.substr(index2, 1) == "0":
            strip.set_pixel_color(16 * positiepixel + index2,
                neopixel.colors(NeoPixelColors.BLUE))
        else:
            strip.set_pixel_color(16 * positiepixel + index2,
                neopixel.colors(NeoPixelColors.BLACK))
        index2 += 1
    if 256 == len(tekst):
        strip.show()
    elif 15 == parse_float(tekst.substr(16, 2)):
        strip.show()

def on_button_pressed_ab():
    Pixel(6, 6)
    Pixel(0, 0)
    Pixel(16, 16)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def ScrollLeft(tekst2: str):
    for index3 in range(16):
        pass
def Pixel(x: number, y: number):
    global positie
    if y % 2 == 0:
        positie = y * 16 - 16 + (17 - x)
    else:
        positie = y * 16 + y
    strip.set_pixel_color(positie - 1, neopixel.colors(NeoPixelColors.YELLOW))
    strip.show()

def on_received_string(receivedString):
    MaakSprite(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    MaakSprite(".................................22..2.222.2...2..2..2...2.2...2..2..2..22.2...2..2..2...2.2...2..2..2...2.2.2.2.22.22.222.22222..................................222.22222.222.....2.2.2.2.2.2...222.2.2.2.2.2.....2.2.2.2.2.2.....2.2...2.2.2...222.2...2.222.")
    basic.pause(5000)
    ScrollUp(".................................22..2.222.2...2..2..2...2.2...2..2..2..22.2...2..2..2...2.2...2..2..2...2.2.2.2.22.22.222.22222..................................222.22222.222.....2.2.2.2.2.2...222.2.2.2.2.2.....2.2.2.2.2.2.....2.2...2.2.2...222.2...2.222.")
    basic.pause(5000)
    MaakSprite("...................8..8.......8....8..8.......8....8..8.......8....8..8....8888....8..8....8..8....8..8....8..8....8888....8888....................5555...55555.......5...5...5....5555...5...5....5......55555....5......5...5....5......5...5....5555...5...5.")
    basic.pause(5000)
    ScrollUp("...................8..8.......8....8..8.......8....8..8.......8....8..8....8888....8..8....8..8....8..8....8..8....8888....8888....................5555...55555.......5...5...5....5555...5...5....5......55555....5......5...5....5......5...5....5555...5...5.")
    basic.pause(5000)
input.on_button_pressed(Button.B, on_button_pressed_b)

def ScrollUp(tekst3: str):
    for index4 in range(16):
        MaakSprite("" + tekst3.substr(index4 * 16 + 16, 240 - index4 * 16) + tekst3.substr(0, index4 * 16 + 16))
def StringVerzender16x(tekst4: str):
    for index22 in range(16):
        radio.send_string("" + tekst4.substr(16 * index22, 16) + str(index22))
        basic.pause(5)
positiepixel = 0
lengte = 0
positie = 0
test = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 256, NeoPixelMode.RGB)
strip.clear()
strip.set_brightness(100)
radio.set_group(1)