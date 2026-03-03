import pyautogui as pilot
import time
from credentials import prompt
from utils.executor import load_and_click, load_and_scroll_click, execute, is_element_present
from utils.operator import click_element
import pyperclip

def write_prompt():
    pyperclip.copy("") # Clean the clipboard
    pyperclip.copy(prompt)
    pilot.hotkey("ctrl","v")
    time.sleep(1)
    pilot.press("enter")
    time.sleep(1)
    pilot.press("enter")
    time.sleep(1)
    pilot.press("enter")
    time.sleep(0.8)
    pyperclip.copy("") # Clean the clipboard
    while(is_element_present("images/chatgpt/send.png",duration=1,confidence=0.9)):
        load_and_click("images/chatgpt/send.png")
        time.sleep(0.2)
        pilot.click()

    time.sleep(1)
    if is_element_present("images/chatgpt/arrow_down.png",duration=1):
        click_element("images/chatgpt/arrow_down.png",confidence=0.8)

    return True

def handle_response():
    print("Waiting for response")
    successful=load_and_scroll_click("images/chatgpt/ok.png",duration=30)
    if successful:
        print("Received Response")
        return True
    else:
        print("Response timout - restarting browser")
        pilot.hotkey("ctrl","2")
        load_and_click("images/brave/reload.png",duration=1)
        return False
    
def submit_prompt():
    write_prompt()
    handle_response()
    return True


