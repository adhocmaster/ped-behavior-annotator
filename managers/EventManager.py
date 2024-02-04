
from library import AppEvent
from library.AppEvent import AppEventType
from typing import Callable

class EventManager:
    def __init__(self) -> None:
        
        ### event streams
        self.initEventStreams()
        pass

    def initEventStreams(self):
         self.annotateFrameHandlers = [] # kust if functions to be called when a annotation is requested
         self.newProjectHandlers = []
         self.saveProjectHandlers = []
         self.updateRecordingViewHandlers = []
         self.exceptionsHandlers = []
         self.recordingHandlers = []
         
    def unsubscribe(self, appEvent: AppEventType, handler: Callable):
        if appEvent == AppEventType.requestAnnotation:
            self.annotateFrameHandlers.remove(handler)
        if appEvent == AppEventType.newProject:
            self.newProjectHandlers.remove(handler)
        if appEvent == AppEventType.saveProject:
            self.saveProjectHandlers.remove(handler)
        if appEvent == AppEventType.updateRecordingView:
            self.updateRecordingViewHandlers.remove(handler)
        if appEvent == AppEventType.exceptions:
            self.exceptionsHandlers.remove(handler)
        if appEvent == AppEventType.recording:
            self.recordingHandlers.remove(handler)

    
    def subscribe(self, appEvent: AppEventType, handler: Callable):
        if appEvent == AppEventType.requestAnnotation:
            self.annotateFrameHandlers.append(handler)
        if appEvent == AppEventType.newProject:
            self.newProjectHandlers.append(handler)
        if appEvent == AppEventType.saveProject:
            self.saveProjectHandlers.append(handler)
        if appEvent == AppEventType.updateRecordingView:
            self.updateRecordingViewHandlers.append(handler)
        if appEvent == AppEventType.exceptions:
            self.exceptionsHandlers.append(handler)
        if appEvent == AppEventType.recording:
            self.recordingHandlers.append(handler)
    
    def onEvent(self, appEvent: AppEvent):
        # if appEvent.type == AppEventType.requestAnnotation:
        #     # self.annotationFrame = self.leftFrame.addLabelFrame("Annotation Edit View", padx=(0,0), pady=(0,0))
        #     # annotationView = AnnotationEditView(self.context["controllers"]["recording"])
        #     # annotationView.render(self.annotationFrame, 5, 100)
        #     print("requestAnnotation event will be handled")
             
        #     # for handler in self.annotateFrameHandlers:
        #     #     handler(appEvent.data["timestamp"], appEvent.data["frame"])
        # if appEvent.type == AppEventType.newProject:
        #     handlers = self.annotateFrameHandlers[appEvent.type]
        if appEvent.type == AppEventType.requestAnnotation:
            for handler in self.annotateFrameHandlers:
                handler(appEvent)

        if appEvent.type == AppEventType.newProject:
            for handler in self.newProjectHandlers:
                handler(appEvent)

        if appEvent.type == AppEventType.saveProject:
            for handler in self.saveProjectHandlers:
                handler(appEvent)

        if appEvent.type == AppEventType.updateRecordingView:
            for handler in self.updateRecordingViewHandlers:
                handler(appEvent)

        if appEvent.type == AppEventType.exceptions:
            for handler in self.exceptionsHandlers:
                handler(appEvent)
        if appEvent.type == AppEventType.recording:
            for handler in self.recordingHandlers:
                handler(appEvent)
    

    def publishExceptionMessage(self, message):
        event = AppEvent(type=AppEventType.exceptions, data={"message": message})
        self.onEvent(event)

    def publishException(self, e: Exception):
        event = AppEvent(type=AppEventType.exceptions, data=e)
        self.onEvent(event)