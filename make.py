from moviepy.editor import TextClip, concatenate_videoclips

def create_slide(text, color, duration=2, fontsize=100, slide_direction="left"):
    txt_clip = TextClip(text, fontsize=fontsize, color="white", font="Arial-Bold", size=(1080, 1920))
    txt_clip = txt_clip.set_position("center").set_duration(duration)

    # Apply background color using RGB tuple
    color_rgb = color  # Use the passed RGB color
    txt_clip = txt_clip.on_color(color=color_rgb, col_opacity=1)

    # Slide animation
    if slide_direction == "left":
        txt_clip = txt_clip.set_position(lambda t: (1080 - t * 1080 / duration, 960))  # slide from right to left
    elif slide_direction == "right":
        txt_clip = txt_clip.set_position(lambda t: (t * 1080 / duration, 960))  # slide from left to right

    return txt_clip

# Set the video duration and slide duration
video_duration = 15  # Total video duration (seconds)
slide_duration = video_duration / 7  # Dividing the total video time across the slides

# Create slides with the updated duration and same info as the previous video
slide1 = create_slide("Deriv Signals", (255, 0, 0), duration=slide_duration, fontsize=100, slide_direction="left")
slide2 = create_slide("Choose your plan", (255, 0, 0), duration=slide_duration, fontsize=80, slide_direction="right")
slide3 = create_slide("$10/month", (0, 255, 0), duration=slide_duration, fontsize=70, slide_direction="left")
slide4 = create_slide("3 Trading Signals per Day", (0, 255, 0), duration=slide_duration, fontsize=70, slide_direction="right")
slide5 = create_slide("$25/month", (0, 0, 255), duration=slide_duration, fontsize=70, slide_direction="left")
slide6 = create_slide("10 Trading Signals per Day", (0, 0, 255), duration=slide_duration, fontsize=70, slide_direction="right")
slide7 = create_slide("$50/month", (255, 255, 0), duration=slide_duration, fontsize=70, slide_direction="left")
slide8 = create_slide("Unlimited Signals", (255, 255, 0), duration=slide_duration, fontsize=70, slide_direction="right")
slide9 = create_slide("Automated Trading", (255, 165, 0), duration=slide_duration, fontsize=70, slide_direction="left")
slide10 = create_slide("24/7 VIP Support", (255, 165, 0), duration=slide_duration, fontsize=70, slide_direction="right")
slide11 = create_slide("Get Started Today!", (255, 0, 255), duration=slide_duration, fontsize=80, slide_direction="left")

# Concatenate all the slides
final_video = concatenate_videoclips([slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8, slide9, slide10, slide11])

# Save the video file with the 9:16 aspect ratio
final_video.write_videofile("energetic_deriv_video.mp4", fps=24)
