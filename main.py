"""
Automates playing the Google Dinosaur Game.
"""

import logging
import webbrowser
import keyboard
from config import *
from pyautogui import press, screenshot


# logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def detect_obstacle(x_range: list[int], y_range: list[int]) -> bool:
    """
    Detects when an obstacle is approaching by comparing the pixel colour in front of the dinosaur against
    the surrounding background colour.
    """
    # take screenshot
    image = screenshot()

    # capture background colour of the game screen
    background_colour = image.getpixel(BACKGROUND_COLOUR_COORDINATE)

    for x in x_range:
        for y in y_range:
            # get current pixel colour
            pixel_colour = image.getpixel((x, y))

            # return true if current pixel colour is different from the background by the given tolerance
            if all(
                abs(pc - bc) > TOLERANCE
                for pc, bc in zip(pixel_colour, background_colour)
            ):
                return True
    return False


logging.debug("Launch Game..")
webbrowser.open(DINOSAUR_GAME_URL)

logging.debug("Script running..")

while not keyboard.is_pressed("esc"):
    obstacle_detected = detect_obstacle(
        OBSTACLE_DETECTION_RANGE_X, OBSTACLE_DETECTION_RANGE_Y
    )

    if obstacle_detected:
        press("up")
