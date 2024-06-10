from django import forms

from mersana_app.models import Comment

error_message = {
    'required': "تکمیل کردن این فیلد ضروری است!"
}


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(required=True, error_messages=error_message,  widget=forms.Textarea())

    class Meta:
        model = Comment
        fields = ['name', 'message']