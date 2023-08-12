from moviepy.editor import VideoFileClip

video = VideoFileClip("video.mp4")
video.write_gif("mygif.gif", fps=10)