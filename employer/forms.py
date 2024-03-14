from .models import Employer
from django import forms


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = "__all__"
