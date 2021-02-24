from pyCinEditorML.kernel.Actions import AddText, AddTitle, AddSubtitle, Export, Concatenate
from pyCinEditorML.src.Exceptions import UndefinedClip, UndefinedAction

ADD_TEXT = 0
ADD_TITLE = 1
ADD_SUBTITLE = 2
EXPORT = 3
CONCATENATE = 4

# pas encore complet

class ActionBuilder:
    """
    Builder for actions
    """

    def __init__(self, root, kind, clip):
        self.root = root
        self.kind = kind
        self.clip = clip
        self.text = None  # string, text for ADD_TEXT, ADD_TITLE or ADD_SUBTITLE
        self.textSize = None # int, textsize for ADD_TEXT
        self.horizontalPosition = None # string "left", "center" or "right" for ADD_TEXT
        self.verticalPosition = None # string "top", "center" of "bottom" for ADD_TEXT

    def on_text(self, text):
        self.text = text
        return self.root

    def get_contents(self):
        """
        Builds the action

        :return: Action, the action
        """
        if self.kind == ADD_TEXT:
            return AddText(self.name, self.clip, self.text)
        if self.kind == ADD_TITLE:
            return AddTitle(self.name, self.clip, self.text)
        if self.kind == ADD_SUBTITLE:
			return AddSubitle(self.name, self.clip, self.text)
        if self.kind == EXPORT:
			return Export(self.name, self.clip)
        return None
