class Song(object):
	def __init__(self,title,artist):
		self.title = title
		self.artist = artist

	def __str__(self):
		return ('"%(title)" by %(artist)'%self.__dict__)


	