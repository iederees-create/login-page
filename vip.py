from moviepy.editor import TextClip, concatenate_videoclips, CompositeVideoClip, ColorClip
import moviepy.video.fx.all as vfx

# Function to create a centered slide
def create_centered_slide(title, content, bg_color=(0, 0, 50), title_fontsize=80, content_fontsize=50, duration=5):
    # Title text
    title_clip = TextClip(
        title,
        fontsize=title_fontsize,
        color="gold",
        font="Arial-Bold",
        size=(1080, None),  # Maintain 9:16 ratio
        method="caption",
        align="center",
    ).set_position(("center", 200))  # Position near the top

    # Content text
    content_clip = TextClip(
        content,
        fontsize=content_fontsize,
        color="white",
        font="Arial",
        size=(900, None),  # Prevent overflow by limiting width
        method="caption",
        align="center",
    ).set_position(("center", 500))  # Position below the title

    # Background
    bg = ColorClip((1080, 1920), color=bg_color, duration=duration)

    # Composite slide
    slide = CompositeVideoClip([bg, title_clip, content_clip]).set_duration(duration)
    return slide

# Create slides for pricing plans
def create_pricing_video():
    intro = create_centered_slide(
        "Our Pricing Plans",
        "Choose a plan that fits your trading needs and budget:",
        bg_color=(0, 0, 50),
        title_fontsize=100,
        content_fontsize=60,
        duration=5,
    )

    basic_plan = create_centered_slide(
        "Basic Plan - $10/month",
        "✔ 3 Trading Signals per Day\n✔ Email Support\n✔ Ideal for Beginners\n✔ Signals for Major Pairs Only",
        bg_color=(10, 50, 100),
    )

    pro_plan = create_centered_slide(
        "Pro Plan - $25/month",
        "✔ 10 Trading Signals per Day\n✔ Priority Email Support\n✔ Signals for Major, Minor Pairs, and Indices\n✔ Daily Market Analysis\n✔ Trailing Stop Recommendations",
        bg_color=(10, 30, 70),
    )

    premium_plan = create_centered_slide(
        "Premium Plan - $50/month",
        "✔ Unlimited Signals\n✔ 24/7 VIP Support (Email & WhatsApp)\n✔ Signals for All Markets\n✔ Advanced Market Insights\n✔ Monthly Live Webinars\n✔ Personalized Recommendations",
        bg_color=(50, 0, 50),
    )

    bot_plan = create_centered_slide(
        "Deriv Bot - $50 (One-Time Purchase)",
        "✔ Automated Trading\n✔ Customizable Settings\n✔ Backtesting Feature\n✔ Lifetime Access\n✔ Step-by-Step User Guide\n✔ 24/7 Technical Support",
        bg_color=(20, 40, 60),
    )

    outro = create_centered_slide(
        "🚀 Start Your Trading Journey Today!",
        "Choose the plan that works for you and unlock your trading potential.\n\nSign up now and take control of your future!",
        bg_color=(0, 50, 0),
        title_fontsize=100,
        content_fontsize=60,
        duration=7,
    )

    # Combine slides
    video = concatenate_videoclips([intro, basic_plan, pro_plan, premium_plan, bot_plan, outro])
    return video

# Generate and save the video
final_video = create_pricing_video()
final_video.write_videofile("pricing_plans.mp4", fps=24)
