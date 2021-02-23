import abc

class Clip(abc.ABC):
    """
    Abstraction for clips
    """
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def declare(self):
        """open or create clip"""
        pass

class Video(Clip):
    """
    A video
    """
    def __init__(self, name, path):
        Clip.__init__(self, name, duration)
		self.path = path

    def declare(self):
        """open video"""
        return
		
class Blank(Clip):
    """
    An empty clip
    """
    def __init__(self, name, duration, color = 'black'): # by default the background is black
        Clip.__init__(self, name)
		self.duration = duration
		self.color = color

    def declare(self):
        """create background"""
        return
