import keyboard
import pyautogui
import threading
import time

import utility
import atomic_game_actions as actions
from ShopItems import ShopItems


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
        print("Thread with main logic will continue indefinitely again...")
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
            actions.close_any_popup_windows()
            time.sleep(1)
            print("Opening shop...")
            actions.open_shop()
            time.sleep(1)
            print(f"Buying fish packs ({shop_item_to_buy})")
            actions.buy_max_fish(shop_item_to_buy)
            time.sleep(1)
            print("Closing shop...")
            actions.close_any_popup_windows()
            print("Opening packs of fish...")
            actions.open_all_packs()
            print("Adding fish to tank...")
            actions.put_fish_into_tank()
            print("Opening current tank...")
            actions.open_current_tank()
            time.sleep(1)
            print("Filtering golden and rainbow to other tank...")
            actions.filter_golden_and_rainbow_to_other_tank()
            print("Selling all unlocked fish...")
            actions.sell_all_unlocked_fish()
            pyautogui.moveTo(utility.get_centre_point())
            time.sleep(1)
        except:
            print("...Main logic failed")
        utility.print_help()
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

utility.print_help()

# Keep the program running and listening
keyboard.wait()
