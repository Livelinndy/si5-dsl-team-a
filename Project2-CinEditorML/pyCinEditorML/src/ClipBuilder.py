from pyCinEditorML.kernel.Clips import Video, Blank

VIDEO = 0
BLANK = 1

# verifier si complet

class ClipBuilder:
    
    def __init__(self, root, name, kind):
        """
        Constructor.

        :param root: AppBuilder, root builder
        :param name: Int, name of the clip
        :param kind: kind of clip to build
        :return:
        """
        self.root = root
        self.name = name
        self.kind = kind
        self.path = None  # string, path for VIDEO
		self.duration = None # duration for BLANK
		self.color = None # string, background color for BLANK

    def on_color(self, color):
        self.color = color
        return self.root
		
	def on_duration(self, duration):
        self.duration = duration
        return self.root
		
	def on_path(self, path):
        self.path = path
        return self.root

    def get_contents(self):
        """
        Builds the clip

        :return: Clip, the clip
        """
        if self.kind == VIDEO:
            return Video(self.name, self.path)
        if self.kind == BLANK:
			return Blank(self.name, self.duration, self.color)
        return None
