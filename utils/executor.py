import time
import pyautogui as pilot
from pyautogui import ImageNotFoundException

def execute(func, params=None, duration=300, frequency=10):
    for i in range(duration*frequency):
        res=func()
        if res:
            print("Executed Successfully")
            return True
        time.sleep(1/frequency)
    return False

def is_element_present(path,duration=5,frequency=10,confidence=0.8):
    iterations = duration * frequency
    for _ in range(iterations):
        try:
            res = pilot.locateOnScreen(path, confidence=confidence)
            if res is not None:
                return True  # Found element
        except ImageNotFoundException:
            # If the file is missing, no point in retrying
            time.sleep(1 / frequency)
        time.sleep(1 / frequency)
    return False

from utils.operator import click_element
def load_and_click(path,duration=30,confidence=0.8):
    duration=duration*10
    for _ in range(duration):
        try:
            res = pilot.locateOnScreen(path, confidence=confidence)
            if res is not None:
                return click_element(path,confidence=confidence)
        except ImageNotFoundException:
            time.sleep(0.1)
        time.sleep(0.1)

def load_and_scroll_click(path,duration=30,confidence=0.8):
    duration=duration*10
    for _ in range(duration):
        try:
            res = pilot.locateOnScreen(path, confidence=confidence)
            if res is not None:
                return click_element(path,confidence=confidence)
            pilot.scroll(-200)
        except ImageNotFoundException:
            time.sleep(0.1)
        time.sleep(0.1)

