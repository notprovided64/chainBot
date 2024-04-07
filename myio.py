import pyautogui as auto
import mss
import mss.tools
import numpy as np
from PIL import Image
import time
import cv2
import os
import uuid
from datetime import datetime

def log(subject, message):
    time = datetime.now().time()
    print(f"({time}) {subject:7}: {message}")

def match_in_folder(screenshot, folder_path):
  file_names = os.listdir(folder_path)

  for entry in file_names:
    full_path = os.path.join(folder_path, entry)
    if full_path.endswith('.png'):
        if on_screen(screenshot, full_path):
            return True
        
  return False

def click():
    auto.click()

def moveTo(coords):
    auto.moveTo(coords[0], coords[1])

def moveClick(coords):
    auto.click(coords[0], coords[1])

def drag(startCoord, endCoord):
    moveTo(startCoord)
    time.sleep(0.2)

    auto.mouseDown()

    moveTo(endCoord)
    time.sleep(0.2)

    auto.mouseUp()

def hold_keys(keys, hold_time_seconds):
    for key in keys:
        auto.keyDown(key)

    time.sleep(hold_time_seconds)

    for key in keys:
        auto.keyUp(key)

def hotkey(*args):
    auto.hotkey(*args)

def on_screen(screenshot, filename):
    img = cv2.imread(filename)

    # cv2.imshow("yo", img)
    # cv2.imshow("ee", screenshot)

    # cv2.waitKey(0)

    # cv2.destroyAllWindows()

    result = cv2.matchTemplate(screenshot, img, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    log("imgrec", f"{filename} : {max_val}")
    
    threshold = 0.9
    if max_val >= threshold:
        return True
    else:
        return False

def screenshot(coords, top_half_only=False):
    sct = mss.mss()

    height = coords["window_height"]
    if top_half_only:
        height = coords["window_height"] / 2

    monitor = {
        "top": coords["window_top_left"][1], 
        "left": coords["window_top_left"][0], 
        "width": coords["window_width"], 
        "height": height
    }

    img = sct.grab(monitor)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

    return img

def addToTargetList(coords):
    sct = mss.mss()

    monitor = {
        "top": coords["gif_top_left"][1], 
        "left": coords["gif_top_left"][0], 
        "width": coords["gif_width"], 
        "height": coords["gif_height"], 
    }
    
    img = sct.grab(monitor)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

    name = f"images/target/{str(uuid.uuid4())}.png"
    cv2.imwrite(name, img)
    
def record_gif(top_left, width, height, output_file, duration=200, num_frames=120):
    sct = mss.mss()
    
    monitor = {"top": top_left[1], "left": top_left[0], "width": width, "height": height}
    
    img_list = []

    for _ in range(num_frames):
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        img_list.append(img)

        # Pause between capturing frames
        time.sleep(0.05)

    img_list[0].save(output_file, save_all=True, append_images=img_list[1:], duration=duration, loop=0)


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

