import yt_dlp

def download_youtube_video(url, save_path="."):
    options = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",  # Force MP4 format
        "merge_output_format": "mp4",  # Ensure merging into MP4 format
        "outtmpl": f"{save_path}/%(title)s.%(ext)s"  # Saves as video title
    }
    
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

# Example usage
youtube_url = input("Enter YouTube URL: ")
download_youtube_video(youtube_url)
