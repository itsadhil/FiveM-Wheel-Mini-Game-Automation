import pyautogui
import numpy as np
from PIL import ImageGrab, Image, ImageDraw
import keyboard  # For key press detection

# Function to capture a specific region of the screen
def capture_screen(region=None):
    if region is None:
        # Default region if none is specified (e.g., center of the screen)
        region = (500, 300, 1500, 1000)  # (left, top, right, bottom)
    
    print(f"Capturing region: {region}")
    screen = ImageGrab.grab(bbox=region)  # Capture the region of the screen
    return np.array(screen)

# Function to draw an outline around the detected region
def draw_outline(image, top_left, bottom_right, color=(255, 255, 255)):
    # Convert to PIL image for drawing
    pil_image = Image.fromarray(image)  # Create PIL image from numpy array
    draw = ImageDraw.Draw(pil_image)
    
    # Draw a rectangle outline around the detected region
    draw.rectangle([top_left, bottom_right], outline=color, width=3)
    
    return np.array(pil_image)

# Function to detect the green zone (color #40C057)
def detect_green_zone(image):
    print("Waiting to detect green zone...")
    
    # Define the RGB range for green zone (#40C057)
    green_min = np.array([64, 192, 87], dtype=np.uint8)  # RGB for #40C057
    green_max = np.array([64, 192, 87], dtype=np.uint8)  # Exact match
    
    # Extract RGB channels
    red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    
    # Mask for green zone: check if the RGB values match #40C057
    green_mask = (red == green_min[0]) & (green == green_min[1]) & (blue == green_min[2])
    
    # Get the coordinates of the green pixels
    green_pixels = np.column_stack(np.where(green_mask))
    
    if green_pixels.size > 0:  # Check if any green pixels are detected
        print("Green zone detected!")
        # Return the bounding box of the green zone
        top_left = (min(green_pixels[:, 1]), min(green_pixels[:, 0]))  # (x, y)
        bottom_right = (max(green_pixels[:, 1]), max(green_pixels[:, 0]))  # (x, y)
        return top_left, bottom_right
    else:
        print("No green zone detected.")
        return None

# Function to detect the red bar (color #FF0000)
def detect_red_bar(image):
    print("Waiting to detect red bar...")
    
    # Define the RGB range for the red bar (#FF0000)
    red_min = np.array([255, 0, 0], dtype=np.uint8)  # RGB for #FF0000
    red_max = np.array([255, 0, 0], dtype=np.uint8)  # Exact match
    
    # Extract RGB channels
    red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    
    # Mask for red bar: check if the RGB values match #FF0000
    red_mask = (red == red_min[0]) & (green == red_min[1]) & (blue == red_min[2])
    
    # Get the coordinates of the red pixels
    red_pixels = np.column_stack(np.where(red_mask))
    
    if red_pixels.size > 0:
        print("Red bar detected!")
        return red_pixels  # Return the coordinates of detected red bar
    else:
        print("No red bar detected.")
        return None

# Main function to control the bot
def main():
    while True:
        # Capture the screen
        screen = capture_screen()
        
        # Detect green zone and red bar
        green_zone = detect_green_zone(screen)
        red_bar = detect_red_bar(screen)
        
        if green_zone:
            # Draw an outline around the green zone
            top_left, bottom_right = green_zone
            screen_with_outline = draw_outline(screen, top_left, bottom_right, color=(255, 255, 255))
            
            # Display the screen with outline (optional, remove if not needed)
            screen_with_outline.show()
        
        # Add your bot's actions here based on green zone and red bar detection
        if keyboard.is_pressed('q'):  # Example: exit the loop if 'q' is pressed
            break

# Run the bot
if __name__ == "__main__":
    main()
