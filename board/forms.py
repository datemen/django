from.models import Third_Topic , Second_Topic , First_Topic , Board_Message
from django import forms


class CreateTitleForm(forms.ModelForm):
    class Meta:
        model = Third_Topic
        fields = ['third_topic']
        
class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Second_Topic
        fields = ['second_topic']
        
class BoardMessageForm(forms.ModelForm):
    class Meta:
        model = Board_Message
        fields = ['screenname','content']

class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)