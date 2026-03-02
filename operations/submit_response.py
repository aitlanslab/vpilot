import pyautogui as pilot
import time
from credentials import prompt
from utils.executor import load_and_click, is_element_present

def handle_extension():
    # Switch to annotation tab
    pilot.hotkey("ctrl","1")
    open_ex=load_and_click("images/bsi/extension.png",confidence=0.8)
    time.sleep(0.2)
    input_field=load_and_click("images/bsi/extension_input.png",confidence=0.8)
    time.sleep(0.2)
    pilot.hotkey("ctrl","v")
    time.sleep(0.2)
    input_field=load_and_click("images/bsi/extension_fill.png",confidence=0.8)
    time.sleep(0.2)
    input_field=load_and_click("images/bsi/extension_save.png",confidence=0.8)
    time.sleep(0.2)
    if is_element_present("images/bsi/success.png"):
        pilot.hotkey("enter")
        return True
    if is_element_present("images/chatgpt/invalid_json.png"):
        time.sleep(0.3)
        pilot.hotkey("enter")
        pilot.moveTo(1378,238,duration=0.3)
        time.sleep(0.2)
        pilot.click()
        return True
    return False



def submit_response():
    handle_extension()