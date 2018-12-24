from django import forms

class MountSearchForm(forms.Form):
    character = forms.CharField(max_length=60)
    server = forms.CharField(max_length=60)

    def __init__(self, *args, **kwargs):
        super(MountSearchForm, self).__init__(*args, **kwargs)
        self.fields['character'].label = "Character:"
        self.fields['server'].label = "Server:"
