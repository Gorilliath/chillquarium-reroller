## Prerequisites

### To run this tool

- Python
- `pip install -r requirements.txt`

### Game settings/state

- Ensure `img/*` files are according to your window size
- Ensure 'Fewer clicks' option is enabled so this tool doesn't need to hold LMB when adding fish to the tank
- Ensure your game's 'Color' filter is enabled so golden and rainbow fish are at the top of the tank
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
