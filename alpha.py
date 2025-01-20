import os
import yt_dlp

def download_youtube_videos(channel_url, output_directory):
    try:
        # Ensure output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        print(f"Downloading videos from: {channel_url}")
        print(f"Videos will be saved in: {output_directory}")

        # yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # Download videos
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([channel_url])

        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for input
    channel_url = input("Enter the YouTube channel URL or handle: ").strip()
    output_directory = input("Enter the output directory path: ").strip()

    if channel_url and output_directory:
        download_youtube_videos(channel_url, output_directory)
    else:
        print("Error: Both the YouTube channel URL and output directory path are required.")
