from django import forms
from django.forms import formset_factory

class noFS_Form(forms.Form):
    campo1 = forms.CharField(label='campo1', max_length=100)

class ArticleForm(forms.Form):
    campo1cf = forms.CharField()
    campo2df = forms.DateField()

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


#fin qui nessuna novità


#ArticleFormSet = formset_factory(ArticleForm)
