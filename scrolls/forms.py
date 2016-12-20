from django import forms
from scrolls.models import Scroll

class QueryForm(forms.ModelForm):
    class Meta:
        model = Scroll
        fields = ('element', 'book', 'episode', 'benders')

#  class ScrollForm(forms.ModelForm):
#      class Meta:
#          model = Scroll
