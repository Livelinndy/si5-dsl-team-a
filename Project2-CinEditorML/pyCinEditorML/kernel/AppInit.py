class AppInit:
	def execute(self):
		res = "import os\n"
		res += "import sys\n"
		res += "sys.path.append('../')\n"
		res += "import moviepy.editor as mp\n"
		res += "from moviepy.config import change_settings\n"
		res += "if sys.platform != 'linux':\n"
		res += "	change_settings({\"IMAGEMAGICK_BINARY\": r\"C:\\Program Files\\ImageMagick-7.0.11-Q16\\magick.exe\"})\n";
		res += "else:\n"
		res += "	change_settings({\"IMAGEMAGICK_BINARY\": r\"/usr/bin/magick\"})\n\n"
		return res
