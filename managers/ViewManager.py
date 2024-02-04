"""The purpose of this manager is to intantiate all the view objects and supply it to the user of the objects
"""
from controller.RecordingController import RecordingController
from controller.VideoController import VideoController
from managers.EventManager import EventManager
from view.RecordingView import RecordingView
from view.AnnotationEditView import AnnotationEditView
from view.VideoView import VideoView
#from view import *
class ViewManager:

    def __init__(self, eventManager: EventManager) -> None:
        self.eventManager = eventManager

    def getAnnotationEditView(self, recordingController: RecordingController, eventManager: EventManager): 
        return AnnotationEditView(recordingController, eventManager)
    
    def getRecordingView(self, recordingController: RecordingController, eventManager: EventManager): 
        return RecordingView(recordingController, eventManager)
        
    def getVideoView(self):
        return VideoView(self.eventManager)
