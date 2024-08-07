import pyautogui
import pygetwindow

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
    print("Listening for keypresses ...")
    print("---")


def get_visible_window_with_title(title):
    try:
        windows = pygetwindow.getWindowsWithTitle(title)
        for window in windows:
            if window.visible and window.title == title:
                return window
    except:
        return


def get_window_position_and_size_as_region():
    try:
        window = get_visible_window_with_title("Chillquarium")
        if window:
            return (window.left, window.top, window.width, window.height)
    except:
        print("... Failed to get region from game window: defaulting to screen region")
    return (0, 0, *pyautogui.size())


def get_locate_args():
    return {**LOCATE_ARGS, "region": get_window_position_and_size_as_region()}


def get_centre_point():
    left, top, width, height = get_window_position_and_size_as_region()
    return [left + (width / 2), top + (height / 2)]


def image_exists(image_path):
    try:
        img = pyautogui.locateOnScreen(image_path, **get_locate_args())
        if img:
            return True
    except:
        return False


def try_click_image(image_path):
    try:
        img = pyautogui.locateOnScreen(image_path, **get_locate_args())
        if img:
            pyautogui.click(img)
    except:
        print("... Failed to click something: continuing anyway")


def try_click_nth_image(image_path, index):
    try:
        image_positions = list(
            pyautogui.locateAllOnScreen(image_path, **get_locate_args())
        )
        image = image_positions[index]
        if image:
            pyautogui.click(image)
    except:
        print(f"... Failed to click nth: {index} something: continuing anyway")
