from django.forms import ModelForm
from .models import Automobiles

class AutoForm(ModelForm):
    class Meta:

        model = Automobiles
        fields = '__all__'