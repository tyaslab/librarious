from .models import Member
from django.forms import ModelForm


class MemberForm(ModelForm):
    class Meta:
        model = Member
