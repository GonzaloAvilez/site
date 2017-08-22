from django.core.files.storage  import FileSystemStorage
from django.conf import settings
from os.path import join 


class OverwriteStorage(FileSystemStorage):
	

	def get_available_name(self,name):
		if self.exists(name):
			join.remove(settings.MEDIA_ROOT, name)
		return name
