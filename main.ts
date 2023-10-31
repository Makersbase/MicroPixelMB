function MaakSprite (tekst: string) {
    strip.clear()
    strip.show()
    if (20 < tekst.length) {
        lengte = 255
        positie = 0
    } else {
        lengte = 15
        positie = parseFloat(tekst.substr(16, 2))
    }
    for (let index = 0; index <= lengte; index++) {
        if (Math.trunc(index / 16) % 2 == 0) {
            positiepixel = 16 - (index - Math.trunc(index / 16) * 16) + (16 + Math.trunc(index / 16) * 16 - 16) - 1
        } else {
            positiepixel = 16 * positie + index
        }
        if (tekst.substr(index, 1) == ".") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Black))
        } else if (tekst.substr(index, 1) == "1") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.White))
        } else if (tekst.substr(index, 1) == "2") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Red))
        } else if (tekst.substr(index, 1) == "3") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Purple))
        } else if (tekst.substr(index, 1) == "4") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Orange))
        } else if (tekst.substr(index, 1) == "5") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Yellow))
        } else if (tekst.substr(index, 1) == "6") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Violet))
        } else if (tekst.substr(index, 1) == "7") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Green))
        } else if (tekst.substr(index, 1) == "8") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Blue))
        } else if (tekst.substr(index, 1) == "9") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Indigo))
        } else if (tekst.substr(index, 1) == "0") {
            strip.setPixelColor(positiepixel, neopixel.colors(NeoPixelColors.Black))
        } else {
            strip.setPixelColor(16 * positiepixel + index, neopixel.colors(NeoPixelColors.Black))
        }
    }
    if (256 == tekst.length) {
        strip.show()
    } else if (15 == parseFloat(tekst.substr(16, 2))) {
        strip.show()
    }
}
function Pixel (x: number, y: number) {
    if (y % 2 == 0) {
        positie = (y - 1) * 16 + (x - 1)
    } else {
        positie = (y - 1) * 16 + (16 - (x / 16 + (x - 1) + 0))
    }
    strip.setPixelColor(positie, neopixel.colors(NeoPixelColors.Blue))
    strip.show()
}
radio.onReceivedString(function (receivedString) {
    MaakSprite(receivedString)
})
input.onButtonPressed(Button.B, function () {
    MaakSprite("0000000000000000000000000000000000000006000000000000002220800000000022662080000000220002208000000220600220000000020006022008800002200606222000000000202228200000000000662200600000000060000000000000000000000000000000000000000000000000000000000000000000000000")
    basic.pause(2000)
    MaakSprite("0000000000000000000000000000000000000006000000000000006000800000000000660080000000000000008000000000600600000000000006060008800000000606008000000000006608800000000000666000600000000060000000000000000000000000000000000000000000000000000000000000000000000000")
    basic.pause(2000)
})
function ScrollUp (tekst: string) {
    for (let index = 0; index <= 15; index++) {
        MaakSprite("" + tekst.substr(index * 16 + 16, 240 - index * 16) + tekst.substr(0, index * 16 + 16))
    }
}
function StringVerzender16x (tekst: string) {
    for (let index2 = 0; index2 <= 15; index2++) {
        radio.sendString("" + tekst.substr(16 * index2, 16) + index2)
        basic.pause(5)
    }
}
let positiepixel = 0
let positie = 0
let lengte = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P0, 256, NeoPixelMode.RGB)
strip.clear()
strip.setBrightness(100)
radio.setGroup(1)
