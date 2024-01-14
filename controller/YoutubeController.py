from pytube import YouTube
import cv2
from controller.VideoController import VideoController
import os


class YoutubeController(VideoController):
    def __init__(self, url: str) -> None:
        # Use pytube to download the video
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension='mp4').first()
        filepath = stream.download(filename='temp_video.mp4')
        print(filepath)

        # Create a capture object
        self.capture = cv2.VideoCapture(filepath)
        if not self.capture.isOpened():
            raise ValueError(f"Could not open video from URL: {url}")
        super().__init__(self.capture)

    def __del__(self):
        self.capture.release()
        # os.remove('temp_video.mp4')

    # Test that the video is actually deleted after the object is deleted. 