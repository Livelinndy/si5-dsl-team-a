class UndefinedClip(Exception):
    """
    Exception for references to undefined clips
    """
	__init__():
		super().__init__('undefined clip')
	
class UndefinedAction(Exception):
    """
    Exception for references to undefined actions
    """
	__init__():
		super().__init__('undefined action')

class SyntaxError(Exception):
    """
    Exception for references to syntax errors
    """
	__init__():
		super().__init__('syntax error')