import time
import pyautogui as pilot
from pyautogui import ImageNotFoundException
from utils.executor import load_and_click, load_and_scroll_click, execute, is_element_present
from utils.cursors import get
from utils.operator import click_element
from helpers.image import find
from credentials import prompt
import json
import pyperclip


def load_temp_chat():
    def swicth_to_temp_chat():
        attempts = 5
        for att in range(attempts):
            current = find("images/gemini/temp_chat_active.png", confidence=0.9)
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
                    pilot.moveTo(1787,211,duration=0.3)
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
                        pilot.press("tab",interval=0.1)
                        time.sleep(0.1)
                        pilot.press("tab",interval=0.1)
                        time.sleep(0.1)
                        pilot.press("tab",interval=0.1)
                        time.sleep(0.1)
                        pilot.press("enter",interval=0.1)
                        time.sleep(0.1)
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
    no_img = "images/no_image.png"

    # Exit immediately if no image exists
    if find(no_img):
        print("No Image")
        return False

    copy_ss = "images/bsi/copy_image.png"

    while True:
        position = (211, 306)

        pilot.moveTo(position, duration=0.5)
        pilot.rightClick()

        # Success case
        if find(copy_ss):
            click_element(copy_ss, confidence=0.8)
            time.sleep(0.5)
            return True

        # Retry case
        if find("images/bsi/no_image.png"):
            pilot.hotkey("ctrl", "1")
            time.sleep(0.3)

            pilot.hotkey("ctrl", "r")
            time.sleep(1)

        time.sleep(0.5)



def paste_image():
    prompt_ss = "images/gemini/attachment_input.png"

    if find(prompt_ss):
        click_element(prompt_ss, confidence=0.8)
        time.sleep(1)

        pilot.hotkey('ctrl', 'v')
        time.sleep(2)

        send_btn = "images/gemini/send.png"

        # Wait until send button appears
        print("Waiting for send btn visibility")
        while not find(send_btn):
            time.sleep(0.5)
        print("got send btn")
        print(find(send_btn))
        time.sleep(1)
        pilot.press("enter")
        time.sleep(0.5)
        return True

    return False


def write_prompt():
    print("Writing prompt")
    time.sleep(1)
    pyperclip.copy(prompt)
    time.sleep(1)
    prompt_ss = "images/gemini/prompt_input.png"
    if(find(prompt_ss)):
        print("Found Place to write prompt")
        click_element(prompt_ss, confidence=0.8)
        pilot.hotkey('ctrl', 'v')
        print("Prompt pasted")
    time.sleep(2)
    print("Prompt Writing completed")
    return True

def handle_response():
    print("Waiting for response")
    successful = load_and_scroll_click("images/chatgpt/ok.png", duration=20)
    if successful:
        print("Received Response")
        copied_text=pyperclip.paste()
        # Check if family is available
        
        gemini_output=json.loads(copied_text)
        gemini_output["family"]=str(gemini_output.get("family",""))
        if gemini_output.get("family","")=="No Family" or gemini_output.get("family","")=="" or gemini_output.get("family","").lower()=="unknown" or gemini_output.get("family","").lower()=="null":
            print("Need to find the family")
            load_and_click("images/gemini/ipni_ext.png",duration=3)
            load_and_scroll_click("images/gemini/ipni_input.png",duration=2)
            pilot.click()
            pilot.hotkey("ctrl","v")
            time.sleep(1)
            load_and_click("images/gemini/ipni_submit.png",duration=1)
            pilot.click()
            pilot.click()
            got_response = load_and_scroll_click("images/chatgpt/ok.png", duration=20)
            if got_response:
                return True
        return True
    else:
        return False