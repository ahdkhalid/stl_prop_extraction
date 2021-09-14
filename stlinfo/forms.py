from django import forms

from .models import StlInfo

class StlInfoFrom (forms.ModelForm):
    class Meta:
        model = StlInfo
        fields =['stl_file']

    # def clean_content(self):
    #     data = super(StlInfoFrom, self).clean(*args, **kwargs)
    #     filename = stl_file.name
    #     ext = os.path.splitext(filename)[1]
    #     ext = ext.lower()
    #     if ext not in ['stl']:
    #         raise forms.ValidationError("Not allowed filetype!")

# class StlInfoUpdateFrom (forms.ModelForm):
#     class Meta:
#         model = StlInfo
#         fields =['volume','length','width','height','area']
    