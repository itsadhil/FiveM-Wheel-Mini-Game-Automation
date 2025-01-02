# FiveM Wheel Mini-Game Automation

This project automates the wheel mini-game in FiveM by detecting specific zones (like a green zone or red bar) on the screen and pressing keys automatically based on the detection. It also highlights the detection zone for better visualization.

## Features

- **Automated Key Press:** Detects green zones (RGB: `#40C057`) and automatically presses the `W` key.
- **Visualization:** Highlights the detection zone on the screen with a white rectangular border.
- **Continuous Monitoring:** Runs indefinitely to assist in real-time gameplay.

## Requirements

- Python 3.8+
- Required Python libraries:
  - `pyautogui`
  - `numpy`
  - `Pillow`
  - `keyboard`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/itsadhil/FiveM-Wheel-Mini-Game-Automation.git
   cd FiveM-Wheel-Mini-Game-Automation
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python GTA.py
   ```

## How It Works

1. **Screen Capture:** Captures a specific region of the screen (default: `(500, 300, 1500, 1000)`).
2. **Zone Detection:** Identifies:
   - Green zones (`#40C057`)
   - Red bars (`#FF0000`)
3. **Automation:**
   - Presses the `W` key when a green zone is detected.
   - Highlights the detection area on the screen for debugging.
4. The script loops continuously, monitoring and acting in real-time.

## Configuration

### Screen Capture Region

Modify the `capture_screen` function to adjust the screen region:
```python
region = (left, top, right, bottom)
```

### Zone Colors

- **Green Zone:** Update `green_min` and `green_max` in the `detect_green_zone` function.
- **Red Bar:** Update `red_min` and `red_max` in the `detect_red_bar` function.

### Key Bindings

The script presses the `W` key by default. Change the key in the `main` function:
```python
pyautogui.press('W')  # Replace 'W' with your desired key
```

## Notes

- Run the game in windowed mode and ensure the screen region includes the target area.
- The script is designed for the FiveM Wheel Mini-Game and may require customization for other games.
- To stop the script, press `Ctrl+C` in the terminal.

## Troubleshooting

- **Detection Issues:** Ensure the screen region and color values are accurate.
- **Performance:** Close unnecessary applications to optimize performance.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy automating!
```
