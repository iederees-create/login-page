from PIL import Image, ImageDraw, ImageFont
import os

# Ask the user for the image path
image_path = input("Please enter the image path: ")

# Define the output file path on the Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "output_image.png")

# Smaller cell size for more pixels (higher resolution)
cell_width, cell_height = 3, 3  # Smaller cell size increases the number of pixels

try:
    # Open the image
    img = Image.open(image_path)
    WIDTH, HEIGHT = img.size

    # Define the font for the text (adjust the size to fit smaller blocks)
    font = ImageFont.truetype("C:/Windows/Fonts/BRITANIC.ttf", 6)  # Smaller font for higher resolution

    # Resize the image to fit the new pixel size (more pixels)
    img = img.resize((int(WIDTH / cell_width), int(HEIGHT / cell_height)), Image.NEAREST)
    new_width, new_height = img.size
    img = img.convert("RGB")  # Convert the image to RGB in case it's RGBA

    # Create a new image with the same dimensions as the original
    new_img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    d = ImageDraw.Draw(new_img)

    # Loop through each "pixel" and draw the text
    for i in range(new_height):
        for j in range(new_width):
            r, g, b = img.getpixel((j, i))  # Get pixel value
            k = int((r + g + b) / 3)  # Calculate the grayscale value
            if k < 128:
                text = "1"
            else:
                text = "0"
            d.text((j * cell_width, i * cell_height), text=text, font=font, fill=(0, g, 0))

    # Save the processed image to the desktop
    new_img.save(desktop_path)

    print(f"Image has been saved to your desktop as 'output_image.png'.")

except Exception as e:
    print(f"An error occurred: {e}")
