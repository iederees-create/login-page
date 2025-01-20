from moviepy.editor import *

# Function to create a slide with text
def create_slide(title, details="", duration=3, bg_color="red", text_color="white", font_size=70):
    """Creates a slide with a title and optional details."""
    text = title if not details else f"{title}\n\n{details}"
    return TextClip(
        text,
        fontsize=font_size,
        color=text_color,
        font="Arial-Bold",
        bg_color=bg_color,
        size=(1080, 1920),  # 9:16 aspect ratio
        method="caption",
    ).set_duration(duration)

# Plan details
slides_data = [
   ("Web Development Services", "Build Smarter. Earn More Online.", 2),  # Intro slide
("Basic Plan", "$20/month\n\n- Simple Website Setup\n- Email Support\n- Ideal for Beginners\n- Single-Page Website Only", 3),
("Pro Plan", "$50/month\n\n- Multi-Page Website\n- Priority Email Support\n- Custom Design Options\n- Mobile-Responsive Development\n- Basic SEO Setup", 3),
("Premium Plan", "$100/month\n\n- Unlimited Web Pages\n- 24/7 VIP Support (Email & WhatsApp)\n- E-commerce Integration\n- Advanced SEO Optimization\n- Monthly Analytics Reports\n- Personalized Consultation", 3),
("Custom Web App", "$100 (One-Time Purchase)\n\n- Tailored Web Applications\n- Customizable Features\n- Performance Optimization\n- Lifetime Access to Updates\n- Step-by-Step User Guide\n- 24/7 Technical Support", 3),

]

# Create slides for each plan
slides = [
    create_slide(title, details, duration, bg_color="red", text_color="white", font_size=60)
    for title, details, duration in slides_data
]

# Add wipe transitions between slides
final_clips = []
for i, slide in enumerate(slides):
    final_clips.append(slide)
    if i < len(slides) - 1:  # Add a transition between slides
        direction = "left" if i % 2 == 0 else "right"  # Alternate directions
        transition = slide.crossfadeout(0.5).set_start(slide.end)
        final_clips.append(transition)

# Concatenate all slides and transitions
final_video = concatenate_videoclips(final_clips, method="compose")

# Speed up the video to fit 15 seconds
final_video = final_video.fx(vfx.speedx, final_video.duration / 15)

# Export the video
output_path = "trading_plans_promo_15sec.mp4"
final_video.write_videofile(output_path, fps=24, codec="libx264", audio=False)
