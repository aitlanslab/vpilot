import time
import pyautogui as pilot
from pyautogui import ImageNotFoundException
from utils.executor import load_and_click, load_and_scroll_click, execute, is_element_present
from utils.cursors import get
from utils.operator import click_element
from helpers.image import find
from credentials import prompt
import pyperclip


def load_temp_chat():
    def swicth_to_temp_chat():
        attempts = 5
        for att in range(attempts):
            current = find("images/gemini/temp_chat.png", confidence=0.9)
            if current:
                print(f"Found temp on {(att+1)} attempts")
                return True
            # Check if temp chat is visible on top
            top_visibility = find("images/gemini/top_temp_chat.png", confidence=0.8)
            if top_visibility:
                curr_mode = find("images/gemini/top_temp_chat_active.png", confidence=1)
                if curr_mode:
                    print("Found Temp Chat")
                    return True
                else:
                    print("Need to enable temp chat")
                    temp_mode = load_and_click("images/gemini/top_temp_chat.png", confidence=0.8)
                    time.sleep(0.5)
                    continue
            else:
                # check if new chat available on top
                new_chat = find("images/gemini/top_new_chat.png")
                if new_chat:
                    load_and_click("images/gemini/top_new_chat.png", confidence=0.8)
                    continue
                # Open Navbar
                res = load_and_click("images/gemini/navbar.png", confidence=0.9)
                if res:
                    curr_mode = find("images/gemini/temp_chat_active.png", confidence=1)
                    if curr_mode:
                        print("Found Temp Chat")
                        return True
                    else:
                        print("Need to enable temp chat")
                        temp_mode = load_and_click("images/gemini/temp_chat_mode.png", confidence=0.8)
                        time.sleep(0.5)
                        continue
                    print(f"Attemps {(att+1)}")
                    continue
    
    def dismiss_intro():
        print("Need to Dismiss intro")
        res = find("images/gemini/intro.png")
        if res:
            load_and_click("images/gemini/intro_close.png")
        return True
    
    swicth_to_temp_chat()
    dismiss_intro()

def copy_image():
    position = 211, 306
    pilot.moveTo(position, duration=0.5)
    pilot.rightClick()
    copy_ss = "images/bsi/copy_image.png"
    if(find(copy_ss)):
        click_element(copy_ss, confidence=0.8)
        return True
    if(find("images/bsi/no_image.png")):
        pilot.hotkey("ctrl", "1")
        time.sleep(0.3)
        pilot.hotkey("ctrl", "r")
        time.sleep(1)
    time.sleep(0.5)
    copy_image()


def paste_image():
    prompt_ss = "images/gemini/prompt_input.png"
    if(find(prompt_ss)):
        click_element(prompt_ss, confidence=0.8)
        pilot.hotkey('ctrl', 'v')
        return True
    return False

def write_prompt():
    time.sleep(1)
    pilot.click()
    pilot.click()
    pyperclip.copy("")  # Clean the clipboard
    pyperclip.copy(prompt)
    pilot.hotkey("ctrl", "v")
    time.sleep(1)
    pilot.press("enter")
    time.sleep(1)
    pilot.press("enter")
    time.sleep(1)
    pilot.press("enter")
    time.sleep(0.8)
    pyperclip.copy("")

def handle_response():
    print("Waiting for response")
    successful = load_and_scroll_click("images/chatgpt/ok.png", duration=20)
    if successful:
        print("Received Response")
        return True
    else:
        return False