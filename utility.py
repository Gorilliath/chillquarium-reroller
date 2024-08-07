import pyautogui

from config import LOCATE_ARGS


def print_help():
    print("\033[2J\033[H", end="", flush=True)
    print("F1: Freshwater Friends")
    print("F2: Rivers and Ponds")
    print("F3: Reef Fellas")
    print("F4: Marine Dwellers")
    print("F5: Giants")
    print("F6: Spring Pals")
    print("---")
    print("F11: Start/Stop")
    print("---")
    print("Listening for keypresses...")
    print("---")


def get_centre_point():
    screen_width, screen_height = pyautogui.size()
    return [screen_width / 2, screen_height / 2]


def image_exists(image_path):
    try:
        img = pyautogui.locateOnScreen(image_path, **LOCATE_ARGS)
        if img:
            return True
    except:
        return False


def try_click_image(image_path):
    try:
        img = pyautogui.locateOnScreen(image_path, **LOCATE_ARGS)
        if img:
            pyautogui.click(img)
    except:
        print("...Failed to click something - continuing anyway...")


def try_click_nth_image(image_path, index):
    try:
        image_positions = list(pyautogui.locateAllOnScreen(image_path, **LOCATE_ARGS))
        image = image_positions[index]
        if image:
            pyautogui.click(image)
    except:
        print(f"...Failed to click nth: {index} something - continuing anyway...")
