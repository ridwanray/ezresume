from django.forms import ModelForm, Textarea

from .models import Resume
from users.models import Profile


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['name', ]


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'city', 'country', 'phone_number', 'linked_in', 'objective', 'profile_pic', ]
        widgets = {'objective': Textarea(attrs={'class': 'objective-box', 'cols': 50, 'rows': 10}), }
        labels = {"linked_in": "LinkedIn profile",
                  "phone_number": "Mobile number",
                  "profile_pic": "Profile picture",
                  }