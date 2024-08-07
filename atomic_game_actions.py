import pyautogui
import time

import utility


def close_any_popup_windows():
    utility.try_click_image("img/2560-1440-close-window-button.png")


def open_shop():
    utility.try_click_image("img/2560-1440-shop-button.png")


def open_shop_fish_tab():
    utility.try_click_image("img/2560-1440-shop-fish-tab-button.png")


# Expecting `shop_item` to be instance of `ShopItems`
def buy_max_fish(shop_item):
    utility.try_click_nth_image("img/2560-1440-buy-max-button.png", shop_item.value)


def open_all_packs():
    x, y = utility.get_centre_point()

    for i in range(30):
        pyautogui.click(x, y + 50)


def put_fish_into_tank():
    duration = 9  # seconds
    end_time = time.time() + duration

    # Move the mouse to the starting position
    x, y = utility.get_centre_point()
    pyautogui.moveTo(x + 500, y - 75)

    pyautogui.click()  # Assumes reduced-click mode is on

    while time.time() < end_time:
        # Move the mouse to the left and right
        pyautogui.moveRel(-1000, 0, duration=0.2)
        pyautogui.moveRel(1000, 0, duration=0.2)

    pyautogui.moveTo(x, y)


def open_current_tank():
    utility.try_click_image("img/2560-1440-current-tank-button.png")


def filter_golden_and_rainbow_to_other_tank():
    while utility.image_exists(
        "img/2560-1440-common-rainbow.png"
    ) or utility.image_exists("img/2560-1440-common-golden.png"):
        # 0 is the 'Switch Tank' button at very top, so skip that one
        utility.try_click_nth_image("img/2560-1440-switch-tank.png", 1)
        time.sleep(1)
        utility.try_click_image("img/2560-1440-switch-tank-gilded.png")
        time.sleep(1)


def sell_all_unlocked_fish():
    utility.try_click_image("img/2560-1440-sell-all-unlocked-fish-button.png")
