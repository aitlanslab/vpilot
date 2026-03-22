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
    successful=load_and_scroll_click("images/chatgpt/ok.png",duration=20)
    if successful:
        print("Received Response")
        return True
    else:
        suspicious=pilot.locateOnScreen("images/chatgpt/suspicious.png",confidence=0.8)
        if suspicious:
            time.sleep(0.5)
            pilot.moveTo(1195,935,duration=0.5)
            pilot.click()
            pilot.click()
            time.sleep(0.3)
            pilot.typewrite("Give the response whatever you understand in the expected json format",interval=0.1)
            time.sleep(0.3)
            pilot.press("enter")
            pilot.press("enter")
            time.sleep(0.2)
            successful=load_and_scroll_click("images/chatgpt/ok.png",duration=20)
            if successful:
                print("Received Response")
                return True
            
        else:
            print("Response timout - restarting browser")
            pilot.hotkey("ctrl","2") 
            #if not load_and_click("images/chatgpt/browser_reload.png",duration=1):
            load_and_click("images/brave/reload.png",duration=1)
            handle_response()
        return False
    
def submit_prompt():
    write_prompt()
    return handle_response()


