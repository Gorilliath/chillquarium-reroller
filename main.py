import keyboard
import pyautogui
import threading
import time
from enum import Enum


# Consts

LOCATE_ARGS = {"grayscale": True, "confidence": 0.9}


class ShopItems(Enum):
    FRESHWATER_FRIENDS = 0
    RIVERS_AND_PONDS = 1
    REEF_FELLAS = 2
    MARINE_DWELLERS = 3
    GIANTS = 4
    SPRING_PALS = 5


# Utility


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


# Atomic game interactions


def close_any_popup_windows():
    try_click_image("img/2560-1440-close-window-button.png")


def open_shop():
    try_click_image("img/2560-1440-shop-button.png")


def buy_max_fish(shop_item):
    try_click_nth_image("img/2560-1440-buy-max-button.png", shop_item.value)


def open_all_packs():
    x, y = get_centre_point()

    for i in range(30):
        pyautogui.click(x, y + 50)


def put_fish_into_tank():
    duration = 9  # seconds
    end_time = time.time() + duration

    # Move the mouse to the starting position
    x, y = get_centre_point()
    pyautogui.moveTo(x + 500, y - 75)

    pyautogui.click()  # Assumes reduced-click mode is on

    while time.time() < end_time:
        # Move the mouse to the left and right
        pyautogui.moveRel(-1000, 0, duration=0.2)
        pyautogui.moveRel(1000, 0, duration=0.2)

    pyautogui.moveTo(x, y)


def open_current_tank():
    try_click_image("img/2560-1440-current-tank-button.png")


def filter_golden_and_rainbow_to_other_tank():
    while image_exists("img/2560-1440-common-rainbow.png") or image_exists(
        "img/2560-1440-common-golden.png"
    ):
        # 0 is the 'Switch Tank' button at very top, so skip that one
        try_click_nth_image("img/2560-1440-switch-tank.png", 1)
        time.sleep(1)
        try_click_image("img/2560-1440-switch-tank-gilded.png")
        time.sleep(1)


def sell_all_unlocked_fish():
    try_click_image("img/2560-1440-sell-all-unlocked-fish-button.png")


# Main thread state

shop_item_to_buy = ShopItems.FRESHWATER_FRIENDS
running = False
main_thread = None


def change_shop_item(shop_item):
    global shop_item_to_buy
    shop_item_to_buy = shop_item
    print(f"Shop item to buy set to: {shop_item_to_buy}")


def change_running_state(next_state):
    global running, main_thread

    running = next_state

    if running and main_thread == None:
        print("Starting thread with main logic...")
        main_thread = threading.Thread(target=main)
        main_thread.start()
    elif running and main_thread:
        print("Thread with main logic already running...")
    elif not running and main_thread == None:
        print("No thread found to close...")
    elif not running and main_thread:
        print(
            "Thread with main logic will stop gracefully after it finishes its current iteration..."
        )


def main():
    global main_thread
    while running:
        try:
            print("Closing any popup windows...")
            close_any_popup_windows()
            time.sleep(1)
            print("Opening shop...")
            open_shop()
            time.sleep(1)
            print(f"Buying fish packs ({shop_item_to_buy})")
            buy_max_fish(shop_item_to_buy)
            time.sleep(1)
            print("Closing shop...")
            close_any_popup_windows()
            print("Opening packs of fish...")
            open_all_packs()
            print("Adding fish to tank...")
            put_fish_into_tank()
            print("Opening current tank...")
            open_current_tank()
            time.sleep(1)
            print("Filtering golden and rainbow to other tank...")
            filter_golden_and_rainbow_to_other_tank()
            print("Selling all unlocked fish...")
            sell_all_unlocked_fish()
            pyautogui.moveTo(get_centre_point())
            time.sleep(1)
        except:
            print("...Main logic failed")
        print_help()
    main_thread = None
    print("... Main thread stopped gracefully")


# Registering keyboard events
keyboard.on_press_key("F1", lambda e: change_shop_item(ShopItems.FRESHWATER_FRIENDS))
keyboard.on_press_key("F2", lambda e: change_shop_item(ShopItems.RIVERS_AND_PONDS))
keyboard.on_press_key("F3", lambda e: change_shop_item(ShopItems.REEF_FELLAS))
keyboard.on_press_key("F4", lambda e: change_shop_item(ShopItems.MARINE_DWELLERS))
keyboard.on_press_key("F5", lambda e: change_shop_item(ShopItems.GIANTS))
keyboard.on_press_key("F6", lambda e: change_shop_item(ShopItems.SPRING_PALS))
keyboard.on_press_key("F11", lambda e: change_running_state(not running))

print_help()

# Keep the program running and listening
keyboard.wait()
