from haystack import indexes
from .models import TaigaProject

class TaigaProjectIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField()
	description = indexes.TextField()
	# 
	# Put taiga project attributes here
	# 

	def get_model(self):
		return TaigaProject

