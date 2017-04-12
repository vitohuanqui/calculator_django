from django import forms


class NameForm(forms.Form):

    one = forms.IntegerField(label='first number')
    second = forms.IntegerField(label='seocnd number')


class NameForm1(forms.Form):
    one = forms.IntegerField(label='first number')
    second = forms.IntegerField(label='seocnd number')