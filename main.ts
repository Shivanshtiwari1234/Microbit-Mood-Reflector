input.onButtonPressed(Button.A, function () {
    Mood += 1
    basic.showIcon(IconNames.Happy)
    Reflect_Mood()
})
function Setup () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.pause(1000)
    basic.clearScreen()
    basic.showString("Mood Level " + ("" + Mood))
    basic.clearScreen()
}
function Reflect_Mood () {
    basic.pause(1000)
    basic.showString("Mood Level " + ("" + Mood))
    basic.clearScreen()
}
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Asleep)
    Reflect_Mood()
})
input.onButtonPressed(Button.B, function () {
    Mood += -1
    basic.showIcon(IconNames.Sad)
    Reflect_Mood()
})
let Mood = 0
Mood = 0
Setup()
basic.forever(function () {
    if (Mood >= 10) {
        for (let index = 0; index < 5; index++) {
            basic.clearScreen()
        }
        basic.showString("You are really happy")
    }
    if (Mood <= -10) {
        for (let index = 0; index < 5; index++) {
            basic.clearScreen()
        }
        basic.showString("You are really sad")
    }
})
