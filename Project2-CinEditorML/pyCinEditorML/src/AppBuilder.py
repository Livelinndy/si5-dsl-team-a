from pyCinEditorML.kernel.App import App
from pyCinEditorML.src.ClipBuilder import ClipBuilder
from pyCinEditorML.src.ActionBuilder import ActionBuilder

# pas encore complet

class AppBuilder:
    """
    Builder for the application
    """

    def __init__(self, name):
        self.name = name # app name
        self.clips = []  # List[ClipBuider], builders for the clips
        self.actions = []  # List[ActionBuilder], builders for the actions
