from django import forms


class NameForm(forms.Form):

    one = forms.IntegerField(label='first number')
    second = forms.IntegerField(label='seocnd number')
