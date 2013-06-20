from django import forms

class PublisherForm(forms.Form):
    name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    city = forms.CharField(max_length=60)
    state_province = forms.CharField(max_length=30)
    country = forms.CharField(max_length=50)
    website = forms.URLField()

    def add_to_db(self):
        pass

