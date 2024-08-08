## Prerequisites

### To run this tool

- Python
- `pip install -r requirements.txt`

### Game settings/state

- Ensure the game window is at a size without any black bars padding the actual game content (it breaks scaling of source images)
- Ensure you have a tank with 'Gilded' in its name to receive the golden and rainbow fish

## What this tool's main logic loop will do

- Ensure any open game popup window is closed
- Open the shop
- Buy max amount of fish (Which fish depends on which key you have last pressed to configure that)
- Open fish packs
- Add fish to tank
- Open current tank
- Filter gold and rainbow to a tank with 'Gilded' in name
- Sell all unlocked fish

## Usage

- Start the program in a terminal with `py main.py`
- Configure the fish that will be bought (Can be done at any time):
  - `F1`: Freshwater Friends
  - `F2`: Rivers and Ponds
  - `F3`: Reef Fellas
  - `F4`: Marine Dwellers
  - `F5`: Giants
  - `F6`: Spring Pals
- Press `F11` to start/stop the execution of the main logic (When you stop it, it will finish the current iteration and stop gracefully)
