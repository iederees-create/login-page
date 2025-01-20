import os
import yt_dlp

def download_youtube_videos(channel_url, output_directory, captions_file, limit=None, start_from=1):
    try:
        # Ensure output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        print(f"Downloading videos from: {channel_url}")
        print(f"Videos will be saved in: {output_directory}")

        # yt-dlp options
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Ensure MP4 format
            'merge_output_format': 'mp4',  # Merge video and audio into MP4
            'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
            'writesubtitles': True,  # Download subtitles if available
            'writeinfojson': True,  # Save metadata about each video
            'retries': 5,  # Retry failed downloads
            'fragment-retries': 5,  # Retry failed fragments
            'continue_dl': True,  # Resume partial downloads
            'noprogress': False,
            'playliststart': start_from,  # Start downloading from the specified position
        }

        # Optional: Limit the number of videos to download
        if limit:
            ydl_opts['playlistend'] = start_from + limit - 1

        # Create a text file to save captions and hashtags
        with open(captions_file, 'a', encoding='utf-8') as file:
            file.write(f"Captions and Hashtags for Videos {start_from} to {start_from + limit - 1}\n")
            file.write("=" * 50 + "\n\n")

        # Download videos
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(channel_url, download=True)

            # Process each video
            if 'entries' in result:
                videos = result['entries']
                for video in videos:
                    if video:
                        title = video.get('title', 'Unknown Title')
                        description = video.get('description', '')
                        hashtags = [tag for tag in video.get('tags', [])]

                        # Check if the file already exists to avoid duplicates
                        output_file = os.path.join(output_directory, f"{title}.mp4")
                        if os.path.exists(output_file):
                            print(f"Skipping already downloaded video: {title}")
                            continue

                        # Save captions and hashtags
                        with open(captions_file, 'a', encoding='utf-8') as file:
                            file.write(f"Video Title: {title}\n")
                            file.write("Description:\n")
                            file.write(description + "\n\n")
                            file.write("Hashtags:\n")
                            file.write(", ".join(f"#{tag}" for tag in hashtags) + "\n")
                            file.write("=" * 50 + "\n\n")

        print("Download and metadata extraction completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for input
    channel_url = input("Enter the YouTube channel URL or handle: ").strip()
    output_directory = input("Enter the output directory path: ").strip()
    captions_file = input("Enter the captions file path (e.g., captions.txt): ").strip()
    limit = input("Enter the number of videos to download (or press Enter to download all): ").strip()
    start_from = input("Enter the starting position for downloads (e.g., 1 for the first video): ").strip()

    try:
        limit = int(limit) if limit else None
        start_from = int(start_from) if start_from else 1
    except ValueError:
        limit = None
        start_from = 1

    if channel_url and output_directory and captions_file:
        download_youtube_videos(channel_url, output_directory, captions_file, limit, start_from)
    else:
        print("Error: All inputs (YouTube channel URL, output directory, and captions file) are required.")
