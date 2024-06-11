from django import forms

from mersana_app.models import ContactUs, Comment

error_message = {
    'required': "تکمیل کردن این فیلد ضروری است!"
}

attr1 = {'class': 'w-100 form-control border-0 py-3 mb-4 placeholder-gray', 'placeholder': 'نام (در صورت تمایل)'}
attr2 = {'class': 'w-100 form-control border-0 py-3 mb-4 placeholder-gray', 'placeholder': 'موضوع'}
attr3 = {'class': 'w-100 form-control border-0 py-3 mb-4 placeholder-gray', 'placeholder': 'شماره تماس یا ایمیل (درصورت تمایل)'}
attr4 = {'class': 'w-100 form-control border-0 mb-4 placeholder-gray', 'rows': '6', 'cols': '10', 'placeholder': 'پیام شما'}


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(required=True, error_messages=error_message,  widget=forms.Textarea())

    class Meta:
        model = Comment
        fields = ['name', 'message']


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=attr1))
    subject = forms.CharField(widget=forms.TextInput(attrs=attr2))
    mobile = forms.CharField(widget=forms.TextInput(attrs=attr3))
    message = forms.CharField(required=True, error_messages=error_message,  widget=forms.Textarea(attrs=attr4))

    class Meta:
        model = ContactUs
        fields = ['name', 'subject', 'mobile', 'message']