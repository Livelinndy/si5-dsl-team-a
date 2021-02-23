import abc

# pas encore complet

class Action(abc.ABC):
	"""
    Abstraction for actions over clips
    """
    def __init__(self, clip):
        self.clip = clip
		
	@abc.abstractmethod
    def execute(self):
        """execute action"""
        pass

		
		
class AddText(Action):
    def __init__(self, clip):
        self.clip = clip
		
	def execute(self):
        """execute action"""
        return
		
class AddTitle(AddText):
    def __init__(self, clip):
        self.clip = clip
	
	def execute(self):
        """execute action"""
        return
		
class AddSubtitle(AddText):
    def __init__(self, clip):
        self.clip = clip
		
	def execute(self):
        """execute action"""
        return


		
class Concatenate(Action):
    def __init__(self, clip):
        self.clip = clip
		
	def execute(self):
        """execute action"""
        return
		
class ConcatenateWithTransition(Action):
    def __init__(self, clip):
        self.clip = clip
		
	def execute(self):
        """execute action"""
        return
		
		
		
class Cut(Action):
    def __init__(self, clip):
        self.clip = clip
		
	def execute(self):
        """execute action"""
        return
		
		
		
class SetColor(Action):
    def __init__(self, clip):
        self.clip = clip
		
	def execute(self):
        """execute action"""
        return
		
		
		
class Superpose(Action):
    def __init__(self, clip):
        self.clip = clip
		
	def execute(self):
        """execute action"""
        return
		
		
		
class Export(Action):
    def __init__(self, clip):
        self.clip = clip
		
	def execute(self):
        """execute action"""
        return