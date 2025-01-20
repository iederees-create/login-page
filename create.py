import os
import subprocess

# Paths
output_dir = r"C:\Users\iederees\Desktop\new2"
yt_url = "https://www.youtube.com/@yourflexiblegirl"
cookie_file_path = r"C:\Users\iederees\Desktop\www.youtube.com_cookies.txt"  # Path to your cookies file

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# yt-dlp command using the cookies file for authentication
command = [
    "yt-dlp",
    "--cookies", cookie_file_path,  # Use the cookies file here
    "-o", os.path.join(output_dir, "%(title)s.%(ext)s"),
    yt_url
]

# Execute command
try:
    print(f"Starting download from {yt_url}...")
    subprocess.run(command, check=True)
    print(f"Download completed. Files saved to {output_dir}.")
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
