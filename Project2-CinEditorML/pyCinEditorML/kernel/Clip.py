import abc
import pyCinEditorML.kernel.Utils

class Clip(abc.ABC):
    """
    Abstraction for clips
    """
    def __init__(self, name, startTime, duration, endTime):
        self.timeDuration = TimeDuration(startTime, duration, endTime)
        self.name = name

    @abc.abstractmethod
    def declare(self):
        """open or create clip"""
        pass

class TimeDuration:
    """
    time linked to clips
    """
    def __init__(self, startTime, duration, endTime = None):
        self.temporalPosition = timeToSeconds(startTime)
        if endTime != None:
            self.duration = timeBetween(startTime, endTime)
        else:
            self.duration = duration

class Video(Clip):
    """
    A video
    """
    def __init__(self, name, path, startTime, duration, endTime):
        super().__init__(self, name, startTime, duration, endTime)
		self.path = path

    def declare(self):
        """open video"""
        return

class Blank(Clip):
    """
    An empty clip
    """
    def __init__(self, name, duration, color = 'black', startTime, duration, endTime): # by default the background is black
        Clip.__init__(self, name, startTime, duration, endTime)
		self.color = color

    def declare(self):
        """create background"""
        return
