from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Constants
VIDEO_WIDTH, VIDEO_HEIGHT = 1080, 1920  # 9:16 aspect ratio
DURATION_PER_SLIDE = 3  # seconds per slide
FONT_PATH = "C:/Windows/Fonts/arial.ttf"  # Update this with a valid font path
OUTPUT_FILE = "intro_nextgenwebs.mp4"

# Slide details (including the new content)
slides_content = [
    "Business Elite\nScale your business\nUS$ 24/mo",
    "US$48.00\nPay less upfront, gain more traction.\nInvest in your growth today!",
    "100 collaborators\nEmpower your team.\nCollaborate without limits.",
    "Unlimited storage space\nStore all your business data safely and securely.",
    "Advanced marketing suite\nAutomate campaigns.\nTrack and grow effectively.",
    "Free domain for 1 year\nGive your business an elite identity online.",
    "500,000 CMS items\nManage extensive content with ease.",
    "Accept payments\nStreamline transactions effortlessly.\nWorldwide compatibility.",
    "Advanced eCommerce\nBoost your online sales.\nIntelligent features for your store.",
    "Advanced developer platform\nBuild and innovate with robust tools.\nStay ahead with elite technology."
]

# Function to create a slide with better text positioning and spacing
def create_slide(text, bg_color, font_color=(255, 255, 255), font_size=60):
    img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, font_size)

    # Split text into lines and calculate spacing to avoid overlap
    lines = text.split("\n")
    total_text_height = sum([draw.textbbox((0, 0), line, font=font)[3] for line in lines]) + (len(lines) - 1) * 20
    y_text = (VIDEO_HEIGHT - total_text_height) // 2

    # Create a slide with proper line spacing
    slides = []
    for line in lines:
        text_width = draw.textbbox((0, 0), line, font=font)[2]
        x_text = (VIDEO_WIDTH - text_width) // 2
        slide = TextClip(line, font=FONT_PATH, fontsize=font_size, color="white", align="center")
        slide = slide.set_position((x_text, y_text)).set_duration(DURATION_PER_SLIDE)

        slides.append(slide)
        y_text += slide.size[1] + 20  # Add spacing between lines

    # Create a background clip for each slide
    background = ColorClip(size=(VIDEO_WIDTH, VIDEO_HEIGHT), color=bg_color, duration=DURATION_PER_SLIDE)
    return CompositeVideoClip([background] + slides)

# Create video slides for each content
video_slides = [create_slide(slide_content, (70, 130, 180)) for slide_content in slides_content]

# Combine slides into a video
final_video = concatenate_videoclips(video_slides, method="compose")

# Export the video
final_video.write_videofile(OUTPUT_FILE, fps=24, codec="libx264")
