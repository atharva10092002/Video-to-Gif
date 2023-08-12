# Video-to-Gif Converter using Moviepy
This Python script uses the MoviePy library to convert a video (video.mp4) into a GIF (mygif.gif) with a specified frame rate (fps).

## Prerequisites
### Install Moviepy: (bash command given below)
pip install moviepy

## Making Your Own Gif

1.Clone or download this repository to your local machine.
2.Place the video file (video.mp4) that you want to convert to a GIF in the same directory as the script.
3.Open the script videoToGif.py in a text editor or an integrated development environment (IDE) of your choice.
4.Modify the video.mp4 filename in the script if your video file has a different name.
5.Set the desired frames per second (fps) for the GIF by adjusting the fps parameter in the video.write_gif() function.
6.Run the script by executing the following command in your terminal or command prompt: python convert_to_gif.py
7.After the script execution completes, you will find the generated GIF file named mygif.gif in the same directory.

## Customization
You can customize the script according to your requirements:

1.Adjust the fps parameter to control the speed of the GIF.
2.Change the input video filename if your video has a different name or is located in a different directory.

## Troubleshooting
If you encounter any issues, ensure that you have installed the MoviePy library and have provided the correct video filename.
Make sure the input video is in a compatible format that MoviePy supports (e.g., MP4, AVI, etc.).

## Acknowledgments
This script utilizes the MoviePy library to simplify the process of converting videos to GIFs.
