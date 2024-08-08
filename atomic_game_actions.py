import pyautogui
import time

import utility


def close_any_popup_windows():
    print("Closing any popup windows")
    utility.try_click_image("img/2560-1440-close-window-button.png")
    time.sleep(1)


def open_shop():
    print("Opening shop")
    utility.try_click_image("img/2560-1440-shop-button.png")
    time.sleep(1)


def open_shop_fish_tab():
    print("Ensuring the 'Fish' tab is selected")
    utility.try_click_image("img/2560-1440-shop-fish-tab-button.png")
    time.sleep(1)


# Expecting `shop_item` to be instance of `ShopItems`
def buy_max_fish(shop_item):
    print(f"Buying fish packs ({shop_item})")
    utility.try_click_nth_image("img/2560-1440-buy-max-button.png", shop_item.value)
    time.sleep(1)


def open_all_packs():
    print("Opening packs of fish")
    x, y = utility.get_window_centre_point()
    for i in range(30):
        pyautogui.click(x, y + 50)


def put_fish_into_tank():
    print("Adding fish to tank")

    duration = 9  # seconds
    end_time = time.time() + duration

    centreX, centreY = utility.get_window_centre_point()
    _, _, width, _ = utility.get_window_position_and_size_as_region()

    # The length of the line which will be drawn side to side to put the fish into the tank
    line_length = (width / 3) * 2

    # Move the mouse to its starting position, which is the centre offset with:
    #  X to be the apex of the line toward the right
    #  Y to align with the fish cards
    pyautogui.moveTo(centreX + (line_length / 2), centreY - 75)

    pyautogui.mouseDown()

    while time.time() < end_time:
        # Move the mouse to the left and right
        pyautogui.moveRel(-line_length, 0, duration=0.2)
        pyautogui.moveRel(line_length, 0, duration=0.2)

    pyautogui.mouseUp()

    # Reset mouse to centre
    pyautogui.moveTo(centreX, centreY)


def open_current_tank():
    print("Opening current tank")
    utility.try_click_image("img/2560-1440-current-tank-button.png")
    time.sleep(1)


def click_color_tank_filter():
    print("Toggling 'Color' tank filter")
    utility.try_click_image("img/2560-1440-color-filter-button.png")
    time.sleep(1)


def filter_golden_and_rainbow_to_other_tank():
    print("Filtering golden and rainbow to other tank")
    while utility.image_exists(
        "img/2560-1440-common-rainbow.png"
    ) or utility.image_exists("img/2560-1440-common-golden.png"):
        # 0 is the 'Switch Tank' button at very top, so skip that one
        utility.try_click_nth_image("img/2560-1440-switch-tank-button.png", 1)
        time.sleep(1)
        utility.try_click_image("img/2560-1440-switch-tank-gilded-button.png")
        time.sleep(1)


def sell_all_unlocked_fish():
    print("Selling all unlocked fish")
    utility.try_click_image("img/2560-1440-sell-all-unlocked-fish-button.png")
