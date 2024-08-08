import pyautogui
import pygetwindow
import time
from PIL import Image

from config import LOCATE_ARGS, ORIGINAL_IMAGE_RESOLUTION


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


def get_window_centre_point():
    left, top, width, height = get_window_position_and_size_as_region()
    return [left + (width / 2), top + (height / 2)]


def get_locate_args():
    return {**LOCATE_ARGS, "region": get_window_position_and_size_as_region()}


def scale_image_to_current_window(image_path):
    original_width, original_height = ORIGINAL_IMAGE_RESOLUTION
    _, _, current_width, current_height = get_window_position_and_size_as_region()

    scale_x = current_width / original_width
    scale_y = current_height / original_height

    img = Image.open(image_path)

    new_width = int(img.width * scale_x)
    new_height = int(img.height * scale_y)
    return img.resize((new_width, new_height))


def image_exists(image_path):
    try:
        image = scale_image_to_current_window(image_path)
        img = pyautogui.locateOnScreen(image, **get_locate_args())
        if img:
            return True
    except:
        return False


def try_click_image(image_path):
    try:
        image = scale_image_to_current_window(image_path)
        img = pyautogui.locateOnScreen(image, **get_locate_args())
        if img:
            pyautogui.click(img)
    except:
        print("... Failed to click something: continuing anyway")


def dedupe_matches(matches, threshold=5):
    filtered_matches = []

    for match in matches:
        left, top, _, _ = match
        is_duplicate = False

        for filtered_match in filtered_matches:
            f_left, f_top, _, _ = filtered_match
            if abs(left - f_left) <= threshold and abs(top - f_top) <= threshold:
                is_duplicate = True
                break

        if not is_duplicate:
            filtered_matches.append(match)

    return filtered_matches


def try_click_nth_image(image_path, index):
    try:
        image = scale_image_to_current_window(image_path)
        deduped_matches = dedupe_matches(
            pyautogui.locateAllOnScreen(image, **get_locate_args())
        )
        img = deduped_matches[index]
        if img:
            pyautogui.click(img)
    except:
        print(f"... Failed to click nth: {index} something: continuing anyway")
