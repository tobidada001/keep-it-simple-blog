from django import forms
from .models import Contact, Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('contact_name', 'contact_email', 'subject', 'message')
        widgets = {

            "contact_name" : forms.TextInput(attrs = {"class": "cnameclass", "style": "width:80%"}),
            "contact_email" : forms.TextInput(attrs = {"class": "cnameclass", "style": "width:80%"}),
            "subject" : forms.TextInput(attrs = {"class": "cnameclass", "style": "width:80%"}),
            "message" : forms.Textarea(attrs = {"class": "careaclass", "cols": "100", "rows": "10"}),
        }

class NewPost(forms.ModelForm):
    post_body = forms.CharField(widget = CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ('post_title', 'post_body' , 'cover', 'category', 'tagsagain' )
        widgets = {

            "post_title" : forms.TextInput(attrs = {"class": "cnameclass", "style": "width:100%"}),
        }
        



    
