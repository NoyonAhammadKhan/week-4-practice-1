from django import forms
import datetime


class DetailForm(forms.Form):
    name = forms.CharField(label="Full Name", max_length=50)
    email = forms.EmailField(label="Email", required=True)
    bio = forms.CharField(label="Bio",
                          widget=forms.Textarea(attrs={'rows': 5}))
    dob = forms.DateField(label="Date Of Birth",
                          widget=forms.NumberInput(attrs={'type': 'date'}), initial=datetime.date.today)
    RELIGION_CHOICES = (('ISLAM', 'ISLAM'), ('HINDUISM', 'HINDUISM'),
                        ('CHIRISTIANITY', 'CHIRISTIANITY'), ('BUDHUISM', 'BUDHUISM'))
    siblings = forms.IntegerField(label="Siblings")
    religion = forms.ChoiceField(label="Your Religion",
                                 widget=forms.RadioSelect, choices=RELIGION_CHOICES)
    gpa = forms.DecimalField(label="GPA")

    SUBJECT_CHOICES = (('MATH', 'MATH'), ('PHYSICS',
                       'PHYSICS'), ('CHEMISTRY', 'CHEMISTRY'))
    subject_choices = forms.MultipleChoiceField(label="Subject Preference",
                                                widget=forms.CheckboxSelectMultiple, choices=SUBJECT_CHOICES)
    agree = forms.BooleanField(
        label="I am agree to all terms and conditions", initial=True)
