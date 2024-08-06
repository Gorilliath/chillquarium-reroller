import keyboard
import pyautogui
import time
from enum import Enum


# Utility

LOCATE_ARGS = {"grayscale": True, "confidence": 0.9}


class ShopItems(Enum):
    FRESHWATER_FRIENDS = 0
    RIVERS_AND_PONDS = 1
    REEF_FELLAS = 2
    MARINE_DWELLERS = 3
    GIANTS = 4
    SPRING_PALS = 5


def print_help():
    print("\033[2J\033[H", end="", flush=True)
    print("F1: Freshwater Friends")
    print("F2: Rivers and Ponds")
    print("F3: Reef Fellas")
    print("F4: Marine Dwellers")
    print("F5: Giants")
    print("F6: Spring Pals")
    print("Listening for keypresses...")


def get_centre_point():
    screen_width, screen_height = pyautogui.size()
    return [screen_width / 2, screen_height / 2]


# Granular interactions


def try_click_image(image_path):
    try:
        img = pyautogui.locateOnScreen(image_path, **LOCATE_ARGS)
        if img:
            pyautogui.click(img)
    except:
        print(".")


def close_any_popup_windows():
    try_click_image("img/2560-1440-close-window-button.png")


def open_shop():
    try_click_image("img/2560-1440-shop-button.png")


def buy_max_fish(shop_item):
    try:
        button_positions = list(
            pyautogui.locateAllOnScreen(
                "img/2560-1440-buy-max-button.png", **LOCATE_ARGS
            )
        )
        button = button_positions[shop_item.value]
        if button:
            pyautogui.click(button)
    except:
        print(".")


def open_current_tank():
    try_click_image("img/2560-1440-current-tank-button.png")


def sell_all_unlocked_fish():
    try_click_image("img/2560-1440-sell-all-unlocked-fish-button.png")


def open_all_packs():
    x, y = get_centre_point()

    for i in range(50):
        pyautogui.click(x, y + 50)


def put_fish_into_tank():
    duration = 10  # seconds
    end_time = time.time() + duration

    # Move the mouse to the starting position
    x, y = get_centre_point()
    pyautogui.moveTo(x + 500, y - 75)

    pyautogui.click()  # Assumes reduced-click mode is on

    while time.time() < end_time:
        # Move the mouse to the left and right
        pyautogui.moveRel(-1000, 0, duration=0.25)
        pyautogui.moveRel(1000, 0, duration=0.25)

        time.sleep(0.1)

    pyautogui.moveTo(x, y)


# Main logic


def main(shop_item):
    try:
        close_any_popup_windows()
        time.sleep(1)
        open_shop()
        time.sleep(1)
        print(f"Buying feesh packs ({shop_item})")
        buy_max_fish(shop_item)
        time.sleep(1)
        close_any_popup_windows()
        print("Opening packs of feesh...")
        open_all_packs()
        print("Adding feesh to tank...")
        put_fish_into_tank()
        print("Opening current tank...")
        open_current_tank()
        pyautogui.moveTo(get_centre_point())
        time.sleep(1)
    except:
        print(".")
    print_help()


# Keyboard event functions


def freshwater_friends(event):
    main(ShopItems.FRESHWATER_FRIENDS)


def rivers_and_ponds(event):
    main(ShopItems.RIVERS_AND_PONDS)


def reef_fellas(event):
    main(ShopItems.REEF_FELLAS)


def marine_dwellers(event):
    main(ShopItems.MARINE_DWELLERS)


def giants(event):
    main(ShopItems.GIANTS)


def spring_pals(event):
    main(ShopItems.SPRING_PALS)


# Hook the functions to their keyboard events
keyboard.on_press_key("F1", freshwater_friends)
keyboard.on_press_key("F2", rivers_and_ponds)
keyboard.on_press_key("F3", reef_fellas)
keyboard.on_press_key("F4", marine_dwellers)
keyboard.on_press_key("F5", giants)
keyboard.on_press_key("F6", spring_pals)

print_help()

# Keep the program running and listening
keyboard.wait()
