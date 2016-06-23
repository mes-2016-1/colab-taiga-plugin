from haystack import indexes
from .models import TaigaProject


class TaigaProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    type = indexes.CharField(model_attr='type')
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')
    slug = indexes.CharField(model_attr='slug')
    # Put taiga project attributes here

    def get_model(self):
        return TaigaProject
