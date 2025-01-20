from moviepy.editor import *

# Convert USD to ZAR using a hardcoded conversion rate
def get_zar_price(usd_price):
    conversion_rate = 18.75  # Approximate USD to ZAR conversion rate
    return round(usd_price * conversion_rate, 2)

# Configurations
usd_price = 20
zar_price = get_zar_price(usd_price)
trading_tips = [
    "💡 Start small, trade smart!",
    "📈 Never risk more than you can afford to lose.",
    "📊 Master the basics before chasing profits.",
    "⚖️ Consistency beats big wins in trading.",
    "🔒 Always use a stop-loss to protect your capital."
]

ad_text = (
    f"🔥 Join our Beginner's Trading Class for only ${usd_price} (~R{zar_price}). "
    "Start your journey to becoming a trading pro today! 🚀"
)

# Slide generation
def create_slide(text, bg_color, text_color):
    clip = TextClip(
        text,
        fontsize=80,
        color=text_color,
        font="Arial-Bold",
        bg_color=bg_color,
        size=(1080, 1920),  # 9:16 aspect ratio
        method="caption",
    ).set_duration(3)  # 3 seconds per slide
    return clip

# Create slides
slides = [
    create_slide("💡 Trading Tips for Beginners 💡", "white", "red"),
]

for tip in trading_tips:
    slides.append(create_slide(tip, "red", "white"))

slides.append(create_slide(ad_text, "white", "red"))

# Add transitions (crossfade)
final_clip = concatenate_videoclips(slides, method="compose").fadein(0.5).fadeout(0.5)

# Save the video
output_path = "gamma1.mp4"
final_clip.write_videofile(output_path, fps=24)

print(f"Advertisement video saved as {output_path}")
