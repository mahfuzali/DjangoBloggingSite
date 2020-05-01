from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

from .models import Post


class MeetingForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Post cannot be submitted in the past")
        return d
