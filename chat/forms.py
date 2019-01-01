from django.forms import ModelForm
from .models import ChatMessage


class MessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('text',)
        labels = {'text': ''}

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'placeholder': 'Send Message'})
