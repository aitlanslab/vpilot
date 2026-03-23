import pyautogui as pilot
import time
from checks.bsi import load_annotation
from checks.gemini import load_temp_chat, copy_image, paste_image, write_prompt, handle_response
from utils.executor import execute
from operations.copy_paste_image import copy_paste_image
from operations.submit_prompt import submit_prompt
from operations.submit_response import submit_response
from start import auto_start

pilot.moveTo(921,22,duration=0.5)
pilot.click()

for i in range(500):
    load_temp_chat()
    copy_image()
    paste_image()
    write_prompt()
    if handle_response():
        submit_response()
