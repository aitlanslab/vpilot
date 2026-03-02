import pyautogui as pilot
import time
from checks.bsi import load_annotation
from checks.chatgpt import load_chatgpt
from utils.executor import execute
from operations.copy_paste_image import copy_paste_image
from operations.submit_prompt import submit_prompt
from operations.submit_response import submit_response
from start import auto_start

#auto_start()

# Focus browser 
pilot.moveTo(921,22,duration=0.5)
pilot.click()

for i in range(500):
    # Check and fix
    annotation_ok=execute(load_annotation)
    chatgpt_ok=execute(load_chatgpt)

    if annotation_ok and chatgpt_ok:
        # Step 1: Copy Paste Image
        copy_paste_image()
        # Step 2: Write Prompt and Submit
        submit_prompt()
        # Step 3: Receive generated output and submit 
        submit_response()
    time.sleep(0.1)
    



