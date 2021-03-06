class UndefinedClip(Exception):
    """
    Exception for references to undefined clips
    """
    def __init__(self):
        super().__init__('undefined clip')
    
class UndefinedAction(Exception):
    """
    Exception for references to undefined actions
    """
    def __init__(self):
        super().__init__('undefined action')

class MySyntaxError(Exception):
    """
    Exception for references to syntax errors
    """
    def __init__(self):
        super().__init__('syntax error')
