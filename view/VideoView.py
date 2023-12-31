import tkinter as tk
from tkinter import ttk
from typing import Callable
from TKinterModernThemes.WidgetFrame import Widget
import TKinterModernThemes as TKMT
import cv2
from PIL import Image, ImageTk
from pytube import YouTube
import threading
import queue
from controller.VideoController import VideoController
from library.AppEvent import AppEvent, AppEventType

from view.View import View

class VideoView(View):

    def __init__(self, videoController: VideoController) -> None:
        self.videoController = videoController

    def render(self, parent: TKMT.WidgetFrame):
        parent.Label("This is our video", size=12)
        return 

        # Create a label to display the video stream
        video = ttk.Label(master=parent)
        video.grid(row=0, column=0, padx=10, pady=10)

        # Create a queue to pass frames between threads
        frame_queue = queue.Queue()

        # Start video streaming in a separate thread
        video_url = "https://www.youtube.com/watch?v=eu4QqwsfXFE"
        video_thread = threading.Thread(target=start_video_stream, args=(video_url, frame_queue))
        video_thread.start()

        # Start updating frames in the GUI thread
        update_thread = threading.Thread(target=update_frame, args=(video, frame_queue))
        update_thread.start()

        # Create a Scale widget
        slider = ttk.Scale(master=parent, from_=0, to=100, orient=tk.HORIZONTAL, command=on_slider_move)
        slider.grid(row=1, column=0, padx=20, pady=10)

def on_slider_move(value):
    # This function will be called when the slider is moved
    print("Slider moved to:", value)

def start_video_stream(video_url, frame_queue):
    # Download the YouTube video
    yt = YouTube(video_url)
    stream = yt.streams.filter(file_extension='mp4').first()

    # Open the video stream
    cap = cv2.VideoCapture(stream.url)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        if not ret:
            break

        # Put the frame into the queue
        frame_queue.put(frame)

    # Release the video stream
    cap.release()

def update_frame(video_label, frame_queue):
    # Get the frame from the queue (if available)
    try:
        frame = frame_queue.get_nowait()

        # Resize the frame to the desired size
        frame = cv2.resize(frame, (960, 540))  # Change the size here as needed

        # Convert frame to PIL Image
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)

        # Convert PIL Image to Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image=pil_image)

        # Update the Tkinter Label with the new frame
        video_label.config(image=photo)
        video_label.image = photo

    except queue.Empty:
        # If the queue is empty, there's no new frame yet, so do nothing
        pass

    # Call this function again after a delay to update frames continuously
    video_label.after(10, update_frame, video_label, frame_queue)

    # events
    def requestAnnotation(eventHandler: Callable):
        event = AppEvent(AppEventType.requestAnnotation, data={"timestamp": 0, "frame": None})
        eventHandler(event) # 