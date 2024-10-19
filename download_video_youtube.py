import yt_dlp

# Ask the user for the video URL
video_url = input("Enter the YouTube video URL: ")

# Replace 'best' with the desired format code
ydl_opts = {
    'format': 'best',  # You can replace 'best' with the format code like '18' or '137+140' based on the list you got
    'outtmpl': '%(title)s.%(ext)s',  # Saves the file with the video title as the filename
}

try:
    # Use yt_dlp to download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Downloading...")
        ydl.download([video_url])
    print("Download completed!")

except Exception as e:
    print(f"An error occurred: {e}")
