from django import forms

val=[['Django','Django'],['Python','PYTHON']]

# name must start with h
def check_for_h(value):
    if value[0].lower()!='h':
        raise forms.ValidationError('name should startwith h')

# length of name should be more than 5
def check_for_length(val):
    if len(val)<=5:
        raise forms.ValidationError('length is too samll')


class Crispyform(forms.Form):
    name=forms.CharField(max_length=200,required=True,validators=[check_for_h,check_for_length])
    email=forms.EmailField(required=True)
    reenteremail=forms.EmailField(required=True)
    course=forms.ChoiceField(choices=val,widget=forms.RadioSelect)


    def clean(self):
        e=self.cleaned_data.get('email')
        r=self.cleaned_data.get('reenteremail')
        if e!=r:
            raise forms.ValidationError('emails are not matched')
