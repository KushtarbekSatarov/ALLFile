from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, AudioFileClip
import os

os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

# List all your video file paths
video_files = [
    "clip1.mp4",
    "clip2.mp4",
    # Add more video paths here
]

# Load video clips and apply fade effects
video_clips = []
for index, video in enumerate(video_files):
    clip = VideoFileClip(video)
    # Apply different fade-in durations based on the video index
    fade_duration = 3 if index == 0 else 1  # 3 seconds for the first video, 1 second for others
    video_clips.append(clip.fadein(fade_duration).fadeout(1))  # Fade out for all clips is 1 second

# Combine all the video clips
combined_clip = concatenate_videoclips(video_clips)

# Get the duration of the combined video clip
video_duration = combined_clip.duration

# Create a text clip with fade-in and fade-out effects
text = (TextClip("Relax in Nature", fontsize=80, font="Arial", color='white')
        .set_position(('center', 'center'))
        .set_duration(10)
        .fadein(4)  # 4-second fade-in for text
        .fadeout(1))  # 1-second fade-out for text

# Overlay the text onto the video
final_clip = CompositeVideoClip([combined_clip, text.set_opacity(1)])  # Ensure text has no background

# Load background music and cut it to match the video duration
audio = (AudioFileClip("gudio1.mp3")
         .subclip(0, video_duration)  # Cut the audio to match the video duration
         .audio_fadein(3)  # 3-second fade-in for audio
         .audio_fadeout(3))  # 3-second fade-out for audio

# Set the audio for the video
final_clip = final_clip.set_audio(audio)

# Export the final video
final_clip.write_videofile("relaxation_video.mp4", codec="libx264", audio_codec="aac")
