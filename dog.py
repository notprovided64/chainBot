import pydirectinput as pdi
import pyautogui as auto

def moveTo(coords):
    pdi.moveTo(coords[0], coords[1])

def moveClick(coords):
    pdi.click(coords[0], coords[1])

def drag(startCoord, endCoord):
    moveTo(startCoord)
    time.sleep(0.3)

    pdi.mouseDown()

    moveTo(endCoord)
    time.sleep(0.3)

    pdi.mouseUp()

def hold_left_joystick(controller, x_value_float, y_value_float, hold_time_seconds):
    controller.left_joystick_float(x_value_float, y_value_float)
    controller.update()
    time.sleep(hold_time_seconds)
    controller.left_joystick_float(0.0, 0.0)  # Reset joystick to the center
    controller.update()  # Call gamepad.update() to apply the changes

def pressButton(controller, button):
    controller.press_button(button = button_mapping[button])
    controller.update()
    time.sleep(0.1)
    controller.release_button(button = button_mapping[button])
    controller.update()
    time.sleep(0.1)

def pressSequence(controller, buttons):
    time.sleep(0.2)
    for button in buttons:
        pressButton(controller, button)

