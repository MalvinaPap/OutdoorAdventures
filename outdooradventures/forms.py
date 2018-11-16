from django import forms

class CreatePostForm(forms.Form):
    activity = forms.CharField(label='activity', max_length=100)
    destination = forms.CharField(label='destination', max_length=100)
    noparticipants = forms.IntegerField(label='participants', max_value=80)
    date = forms.DateField()
    comments = forms.CharField(widget=forms.Textarea)
