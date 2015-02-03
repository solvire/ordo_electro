from django import forms

class AccountForm(forms.Form):
        OPTIONS = (
                ("AUT", "Australia"),
                ("DEU", "Germany"),
                ("NLD", "Neitherlands"),
                )
        Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)