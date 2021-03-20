from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    """
    """
    def clean_qq(self):
        clean_data = self.cleaned_data.get("qq")
        if not  clean_data.isdigit():
            raise forms.ValidationError("必须是数字")
        return int(clean_data)

    class Meta:
        model = Student
        fields = (
            "name", "sex", "profession",
            "email", "qq", "phone"
        )
