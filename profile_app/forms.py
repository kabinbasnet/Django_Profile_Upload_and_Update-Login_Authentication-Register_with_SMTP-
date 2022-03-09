from django.forms import ModelForm
from profile_app.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
