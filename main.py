def on_button_pressed_a():
    global Mood
    Mood += 1
    basic.show_icon(IconNames.HAPPY)
    Reflect_Mood()
input.on_button_pressed(Button.A, on_button_pressed_a)

def Setup():
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.pause(1000)
    basic.clear_screen()
    basic.show_string("Mood Level " + ("" + str(Mood)))
    basic.clear_screen()
def Reflect_Mood():
    basic.pause(1000)
    basic.show_string("Mood Level " + ("" + str(Mood)))
    basic.clear_screen()

def on_button_pressed_ab():
    basic.show_icon(IconNames.ASLEEP)
    Reflect_Mood()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Mood
    Mood += -1
    basic.show_icon(IconNames.SAD)
    Reflect_Mood()
input.on_button_pressed(Button.B, on_button_pressed_b)

Mood = 0
Mood = 0
Setup()

def on_forever():
    if Mood >= 10:
        for index in range(5):
            basic.clear_screen()
    if Mood <= -10:
        for index2 in range(5):
            basic.clear_screen()
basic.forever(on_forever)
